""" This program will open and run a program on a Keithley2400."""

import visa
import numpy as np
import time
import filemanipulation as fm

class error(Exception):

    """ Custom error class for error handling.

    This class will return whatever string is fed to it along while
    raising an error.
    """

    def __init__(self, string):
        """Initialize error message."""
        Exception.__init__()
        self.ErrorMsg = string

    def __str__(self):
        """Return error message."""
        return self.ErrorMsg


class SourceMeter(object):

    """ This class defines a Keithley SMU experiment object.

    This program will make a Keithley SMU object that can run specific
    tests related to chronopotentiometry. View the dictionary KWARGS
    to view the current set parameters for the source meter. If you
    would like to change the run parameters, use the function
    change_argument to modify. Make sure to reinitilize the object
    before running any programs.
    """

    DEFAULT_KWARGS = {'SourceMode': 'CURR',
                      'ComplianceLevel': 200,
                      'NPLC': 1, 'TerminalLocation': 'FRON',
                      'FourTerminal': 'OFF', 'TriggerCount': 1,
                      'TriggerDelay': 0, 'SourceDelay': 0,
                      'ExperimentLength': 2, 'PointDelay': 0.1,
                      'BufferSize': 2500}

    def __init__(self, smu_address='GPIB0::25'):
        """Initialize the object.

        This makes the source meter recource manager for the PyVISA
        protocall. It also makes the local KWARGS dictionary for this
        instance and runs an initilization routiene that does not depend
        on KWARGS (to give a chance for the user to change KWARGS later.
        """
        self.rm = visa.ResourceManager()
        self.KWARGS = dict(self.DEFAULT_KWARGS)
        self.k2400 = self.rm.get_instrument(smu_address)
        self.setup_connection()
        self.initialize_SRQ()

    def setup_connection(self):
        """ Setup the souzrce meter to take measurements.

        This block runs any setup routines that are independent of
        the parameters in KWARGS. Mostly this includes setting the unit
        to send data in the right format and setting up SRQ's.
        """
        self.k2400.write(':*RST')
        # Configure device to output single floating points instead of ASCII
        self.k2400.values_format = 5
        self.k2400.write(':FORM:DATA SRE')
        # Time setup
        self.k2400.write(':SYST:TIME:RES')
        self.k2400.write(':SYST:TIME:RES:AUTO OFF')
        self.k2400.write('TRAC:TST:FORM ABS')  # Set timestamp format
        # Turn off source delay
        self.k2400.write('SOUR:DEL:AUTO OFF')  # Turn off auto source delay
        self.k2400.write(':SOUR:DEL 0.0')  # No source delay
        # Configure measurements
        self.k2400.write(':SENS:FUNC:CONC ON')  # Concurrent measurements
        self.k2400.write(':SENS:FUNC:ON "VOLT","CURR"')
        self.k2400.write(':SENS:FUNC:OFF "RES"')  # Don't measure resistance
        self.k2400.write(':FORM:ELEM:SENS VOLT,CURR,TIME')
        # Enable below once testing is done
        self.k2400.write(':SYST:BEEP:STAT OFF')  # Turn off beeper

    def initialize_SRQ(self, OperationComplete='True', BufferFull='True',
                       Compliance='False', OutputEnable='False',
                       MeasurementSRQ='True', EventSRQ='True'):
        """Initialize K2400 SRQ.

        This function sets up the SRQ and event registers for the
        SMU. The events that can be enabled (and their default values)
        are: OperationComplete=(True), BufferFull=(True), Compliance=(False)
        OutputEnable=(False).

        The enabled events can be set up to generate an SRQ. The operation
        complete is on its own SRQ which can be called with EventSRQ=(True)
        while the buffer full, compliance and output events are on the
        measurement SRQ buffer, MeasurementSRQ=(True).

        If you would like to change the event system and SRQ's, feed the
        above with strings of either 'True' or 'False' to modify the subsystem
        as you please.
        """
        EventBuffer = 0
        MeasurementBuffer = 0
        SRQBuffer = 0
        if OperationComplete == 'True':
            EventBuffer += 1
        if BufferFull == 'True':
            MeasurementBuffer += 512
        if Compliance == 'True':
            MeasurementBuffer += 16384
        if OutputEnable == 'True':
            MeasurementBuffer += 2048
        if MeasurementSRQ == 'True':
            SRQBuffer += 1
        if EventSRQ == 'True':
            SRQBuffer += 32
        self.k2400.write(':FORM:SREG BIN')  # Binary format to read registers
        self.k2400.write(':*SRE '+str(SRQBuffer))
        self.k2400.write(':STAT:MEAS:ENAB '+str(MeasurementBuffer))
        self.k2400.write(':*ESE '+str(EventBuffer))
        self.k2400.write(':*CLS')  # Clear event registers

    def _buffer_bin_to_dec(self, inputStr):
        r"""Convert binary output of buffer to decimal.

        This program takes the string output of a function such as
        ask('*ESE?') in bianary format and converts it into the
        decimal equivilent. For example, u'#B0000000000110001\n' would
        output 49. The input must be a 16 digit string of bianary
        numbers starting with the header #B.
        """
        exponents = (15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
        numStr = inputStr[2:18]
        numList = []
        decNum = 0
        for val in numStr:
            numList.append(int(val))
        for idx, val in enumerate(numList):
            decNum += (val*2)**(exponents[idx])
        return decNum

    def configure_source(self):
        """Set up the source to take measurements.

        This function will configure the source to source what is defined
        to be sourced in KWARGS and measure both (basically telling it to
        measure what is not being sourced since what is being sourced is
        already being measured. It also sets the NPLC since this must
        be defined opposite of whatever is being sourced.
        """
        # Check KWARGS
        self._check_kwargs()
        # Extract measurement mode (opposite if source mode)
        if self.KWARGS['SourceMode'] == 'CURR':
            MeasureMode = 'VOLT'
        elif self.KWARGS['SourceMode'] == 'VOLT':
            MeasureMode = 'CURR'
        else:
            raise error("'Source Mode' in KWARGS not propertly set.")

        # Configure source and measurement
        self.k2400.write(':SOUR:FUNC:MODE '+self.KWARGS['SourceMode'])
        self.k2400.write(':SENS:' + MeasureMode + ':PROT:LEV ' +
                         str(self.KWARGS['ComplianceLevel']))
        # Configure NPLC
        self.k2400.write(':SENS:' + MeasureMode + ':NPLC ' +
                         str(self.KWARGS['NPLC']))
        # Setup measure with front or rear terminals
        self.k2400.write(':ROUT:TERM ' + self.KWARGS['TerminalLocation'])
        # Local or remote sensing (Four temrinal or two terminal)
        self.k2400.write(':SYST:RSEN ' + self.KWARGS['FourTerminal'])

    def reset_buffer(self):
        """Empty the buffer and set to defined buffer size.

        Empties and resets the buffer. The buffer size defaults to the
        maximum size (2500) but can be modified by feeding the
        BufferSize=(2500) value into the function.
        """
        BufferSize = self.KWARGS['BufferSize']
        self.k2400.write(':TRAC:FEED:CONT NEV')
        self.k2400.write(':TRAC:CLE')
        self.k2400.write(':TRAC:POIN ' + str(BufferSize))
        self.k2400.write(':TRAC:FEED:CONT NEXT')

    def configure_chrono_trigger(self):
        """Define simple trigger for chrono measurements.

        This function configures a the trigger count and trigger delay
        for the SMU. Set the parameters TriggerCount=(1) and
        TriggerDelay=(0) SourceDelay=(0) in KWARGS to change the trigger.

        The source delay is the delay between when the output is set and
        the SMU takes a reading. This will be very useful.

        The trigger delay is prehaps less useful, and defines the time
        between when the input trigger is sent and the output is sourced.

        The trigger count gives the number of measurements that will be
        given with the above parameters.
        """
        self.k2400.write(':TRIG:COUN ' + str(self.KWARGS['TriggerCount']))
        self.k2400.write(':TRIG:DEL ' + str(self.KWARGS['TriggerDelay']))
        self.k2400.write(':SOUR:DEl ' + str(self.KWARGS['SourceDelay']))

    def set_output(self, SetPoint=0):
        """Set output level of SMU (in A or V) depending on mode."""
        self.k2400.write(':SOUR:CURR:LEV:TRIG ' + str(SetPoint))

    def source_on(self, state='OFF'):
        """Turn on or off the SMU.

        Pass the string 'ON' to turn on output. Pass the string 'OFF'
        to turn off output. Function will default OFF with no parameters.
        """
        self.k2400.write(':OUTP ' + state)

    def take_points(self):
        """Take points as defined by the Trigger.

        If the operation complete and event SRQ are not set this
        function will enable them as it relies on the SRQ generated by
        the operation complete command. Note that any other event that
        generates an SRQ will trigger a read and may cause an error.
        A buffer full SRQ most likely will not generate a read error
        as this SRQ will correspond to the end of a read event and a
        simultanious OPC event.
        """
        self.reset_buffer()
        # Check that OPC SRQ event is enabled. If not, enable
        # eventEnable = self.k2400.ask('*ESE?')
        # if int(eventEnable[-2]) == 0:
        #     newESE = self.buffer_bin_to_dec(eventEnable) + 1
        #     self.k2400.write('*ESE ' + str(newESE))
        # eventSRQ = self.k2400.ask('*SRE?')
        # if int(eventSRQ[-7]) == 0:
        #     newSRQ = self.buffer_bin_to_dec(eventEnable) + 32
        #     self.k2400.write('*SRE ' + str(newSRQ))
        self.k2400.write('*CLS')  # Clear SRQ
        self.k2400.write(':INIT')
        self.k2400.write('*OPC')
        self.k2400.wait_for_srq(None)
        # Ask for values and format in 2D numpy array.
        Data = np.array(self.k2400.ask_for_values(':TRAC:DATA?'))
        DataOut = np.array((Data[0::3], Data[1::3], Data[2::3]))
        return DataOut

    def setup_simple_experiment(self, SetPoint=0):
        """Setup simple experiment.

        This function sets up a simple experiment with the most basic
        parameters. This is useful for the creation of basic experiments,
        although for more complex runs you will probably want to make
        your own combination of the fundamental commands.
        """
        self.configure_source()
        self.configure_chrono_trigger()
        self.reset_buffer()
        self.set_output(SetPoint)
        self.source_on('ON')

    def reset_device(self):
        """Reset device before power down."""
        self.k2400.write(':*RST')
        self.k2400.write(':*CLS')
        self.k2400.write(':*SRE 0')

    def _check_kwargs(self):
        """Check values of the KWARGS dictionary.

        This function checks KWARGS to make sure the values are set
        within the proper ranges. If it finds values that will cause
        the source meter to error (ie. out of range) it will return
        an error.
        """
        # Check that compliance level is in range for defined source mode.
        if self.KWARGS['SourceMode'] == 'CURR':
            if -210 < self.KWARGS['ComplianceLevel'] <= 210:
                pass
            else:
                raise error('Compliaince level set outside of range. ' +
                            'Must be defined between 0 and 200 V.')
        elif self.KWARGS['SourceMode'] == 'VOLT':
            if -1.05 < self.KWARGS['ComplianceLevel'] <= 1.05:
                pass
            else:
                raise error('Compliance level set outside of range. ' +
                            'Must be defined between 0 and 1.05 A.')
        else:
            raise error("'SourceMode' not set correctly in KWARGS.")
        # Check that NPLC is in possible range of NPLC's
        if 0.01 <= self.KWARGS['NPLC'] <= 10:
            pass
        else:
            raise error('NPLC set outside of range. Must be set ' +
                        'between 0.01 and 10.')


class SMUExperiments(SourceMeter):

    """This class runs SMU experiments."""
    DEFAULT_RUNARGS = {
        'Membrane': 'MembraneName', 'MembraneID': '2000',
        'Salt': 'Salt', 'HighConcentration': 0.5,
        'HighConductivity': 0.0, 'LowConcentration': 0.1,
        'LowConductivity': 0.0, 'RunNumber': 1,
        'SourceMode': 'CURR', 'LowConcT': 25,
        'HighConcT': 25, 'LabTemp': 'NA', 'HighSolutionID': 'NA',
        'LowSolutionID': 'NA',
        'DataPath': ('C:\\Users\\Harrison\\Box Sync\\penn_state\\' +
                     'hickner\\experiments\\conductivity\\' +
                     'max_cell_dc_concentration_gradient\\AmB\\1.14-0.01' +
                     '\\14-06-19\\')}

    def __init__(self, smu_address='GPIB0::25'):
        """Run initilization."""
        SourceMeter.__init__(self, smu_address)
        self.RunArgs = dict(self.DEFAULT_RUNARGS)

    def _format_raw_data(self, inputData):
        """Format data from instrument.

        This program takes the raw data output from a Keithley instrument
        in bianary format and converts it into a three dimentional Python
        list with the format [ [voltage] [current] [time] ].

        The input list must be in the numerical format:
        [ v1, c1, t1, v2, c2, t2, ....... ]
        """
        outputList = [inputData[0::3],
                      inputData[1::3],
                      inputData[2::3]]
        return outputList

    def simple_sweep(self, SweepPath):
        """Perform a simple sweep.

        This program performes a simple sweep as defined by the input
        sweep path. The sweep path is a list that defines the source
        values that will be swept.

        The function will output a list of numpy arrays with the
        volt, current and time from the SMU. The index of the
        output list is the values at each of the index of the input
        sweep. So output[0] corresponds to the points taken at
        SweepPath[0].
        """
        data = []
        SourceMeter.setup_simple_experiment(self)
        for i in SweepPath:
            SourceMeter.set_output(self, i)
            data.append(SourceMeter.take_points(self))
        SourceMeter.source_on(self, 'OFF')
        return data

    def slow_chrono(self, SweepPath, ExperimentLength=None, PointDelay=None,
                    RecordData='No'):
        """Perform a (slow) chrono measurement.

        This function inputs a setpoint, experiment length and
        (non-SMU) internal trigger delay and performs either a
        chronopotentriomitric or chronovoltaic experiment.

        The program will wait PointDelay seconds from the end of
        the last measurement before asking for another. This means
        there will be one data point for every TriggerDelay + NPLC/60 +
        SMUInternal Source and Trigger Delay + Overhead for data transfer.
        Once the experiment has gone for the length, it will terminate
        and return a numpy array with the format
        [voltage, current, time, globalTime].

        Note that the time in this output is the time from the program,
        not the SMU as the SMU timer resets for each trigger. Therefore
        this value is replaced with a computed value from the program.
        This value is not as accurate as if it came from the meter,
        but there is no way around that at this time.

        The advantage if this program over simple_sweep is that it
        is not limited to 2500 data points. It takes data slower,
        but can run indefinatly (limited by the preallocation which
        currently is set to 1,000,000 points, but can be changed to
        any value if needed.)
        """

        if ExperimentLength:
            self.KWARGS['ExperimentLength'] = ExperimentLength
        if PointDelay:
            self.KWARGS['PointDelay'] = PointDelay

        # Make sure the trigger count is one.
        self.KWARGS['TriggerCount'] = 1
        self.setup_simple_experiment()
        globalStartTime = time.time()
        self.RunArgs['SourceMode'] = self.KWARGS['SourceMode']

        def take_points_(setPoint):
            """Take points in the slow chrono way."""
            DataBin = np.zeros((1000000, 4))  # Preallocate 1,000,000 points.
            count = -1
            StartTime = time.time()
            self.set_output(setPoint)
            while time.time() - StartTime < self.KWARGS['ExperimentLength']:
                count += 1
                # Time block
                now = time.time()
                currTime = now - StartTime
                currGlobalTime = now - globalStartTime
                # Data block                now = time.time()
                DataBin[count] = np.append(self.take_points(),
                                           currGlobalTime)

                DataBin[count, 2] = currTime
                time.sleep(self.KWARGS['PointDelay'])
            # Remove zeros from array
            count += 1
            DataBin = DataBin[0:count, :]
            return DataBin

        data = []
        for i in SweepPath:
            data.append(take_points_(i))
        self.source_on('OFF')
        if RecordData == "Yes":
            fm.record_data_files(data, SweepPath, self.RunArgs)
        else:
            return data
