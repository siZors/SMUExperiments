"""
Created on Tue Jun 17 20:49:57 2014

@author: Harrison
"""

import numpy as np
import time
import os


def load_args():
    RunArgs = {
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
    return RunArgs


def make_filenames(SweepList, RunArgs):
    """Make list of chrono filenames for chrono sweep.

    This program inputs a sweep list and returns a list of filenames.
    The returned list is in the format List[0] = filename for steady
    state file. List[1] = List of filenames for the chrono files
    with the key of the list equal to the key of the input chrono
    sweep. List[2] is the name of the subdirectory that the chrono
    files are to be placed in.
    """
    timeStr = time.strftime('%y%m%d%H%M', time.localtime())
    # Make string depending on SourceMode
    if RunArgs['SourceMode'] == 'CURR':
        unit = 'mA'
        unitX = 1000
        SMRep = 'i'
    elif RunArgs['SourceMode'] == 'VOLT':
        unit = 'V'
        unitX = 1
        SMRep = 'v'
    else:
        raise Exception(KeyError)
    # Make front and back end of string. A piece will be put in the
    # middle of this to differentiate each individual chrono run.
    FrontStr = (timeStr + SMRep + '_')
    BackStr = ('_%s_%s_%sp%s_%02d.txt' % (RunArgs['MembraneID'],
                                          RunArgs['Salt'],
                                          str(RunArgs['HighConcentration']),
                                          str(RunArgs['LowConcentration']),
                                          RunArgs['RunNumber']))
    # Make path for chrono files.
    CRDir = RunArgs['DataPath'] + FrontStr + 'CR' + BackStr[:-4] + '\\'
    SSFilename = (RunArgs['DataPath'] + FrontStr + 'SS' + BackStr)
    # Make list of filenames for chrono run.
    filenameList = []
    RunNo = 1
    for value in SweepList:
        MiddleStr = 'CR%02d_%s%s' % (RunNo, str(value*unitX), unit)
        RunNo += 1
        Name = CRDir + FrontStr + MiddleStr + BackStr
        filenameList.append(Name)
    # Make directory name for chrono files.
    ListOut = [SSFilename, filenameList]
    return ListOut


def ensure_dir(Input, isfile='Yes'):
    """Check if file directory exists. If not, create directory.

    Check if a directory exists. If it does not exist, it will
    create the directory. Can feed either a file or a directory.
    If you feed a directory add the argument isfile='No' to the
    input.
    """
    if isfile == 'Yes':
        d = os.path.dirname(Input)
    else:
        d = Input
    if not os.path.exists(d):
        os.makedirs(d)


def write_data(filename, data, RunArgs, SetPoint='NA', SweepPath=[]):
    # Generate file header.
    if RunArgs['SourceMode'] == 'CURR':
        SourceMode = 'Current'
        SourceUnit = 'A'
    elif RunArgs['SourceMode'] == 'VOLT':
        SourceMode = 'Voltage'
        SourceUnit = 'V'
    else:
        raise Exception(KeyError)

    if SetPoint == 'NA':
        Type = 'Steady State File'
    else:
        Type = 'Chrono File'

    baseFilename = os.path.basename(filename)  # Filename without path
    header = (
        baseFilename + '\n' +
        'Date' + '\t' + time.strftime('%m/%d/%Y', time.localtime()) + '\n' +
        'Time\t%s:%s\n' % (baseFilename[6:8], baseFilename[8:10]) +
        'Data Type\t%s\n' % (Type) +
        'Source Mode\t%s\n' % (SourceMode) +
        'Setpoint (%s)\t%s\n' % (SourceUnit, str(SetPoint)) +
        'Sweep Path\t%s\n' % (str(SweepPath)[1:-1]) +
        'Run\t%02d\n' % (RunArgs['RunNumber']) +
        'Membrane\t%s\n' % (RunArgs['Membrane']) +
        'Membrane ID\t%s\n' % (str(RunArgs['MembraneID'])) +
        'Salt\t%s\n' % (RunArgs['Salt']) +
        'High Solution ID\t%s\n' % (RunArgs['HighSolutionID']) +
        'High Concentration (M)\t%s\n' % (str(RunArgs['HighConcentration'])) +
        'High Conductivity (mS/cm)\t%s\n' % (str(RunArgs['HighConductivity'])) +
        'High Solution T (C)\t%s\n' % (str(RunArgs['HighConcT'])) +
        'Low Solution ID\t%s\n' % (RunArgs['LowSolutionID']) +
        'Low Concentration (M)\t%s\n' % (str(RunArgs['LowConcentration'])) +
        'Low Conductivity (mS/cm)\t%s\n' % (str(RunArgs['LowConductivity'])) +
        'Low Solution T (C)\t%s\n' % (str(RunArgs['LowConcT'])) +
        'Lab Temperature (F)\t%s\n' % (str(RunArgs['LabTemp'])) +
        'SMU Voltage (V)\tSMU Current(A)\tLocal Time (s)\tGlobal Time (s)')
    # Write file
    ensure_dir(filename)
    np.savetxt(filename, data, delimiter='\t', header=header, comments='')


def generate_ss_array(data, nPoints=1):
    """Generate SS array from output of the chrono sweep.

    Inputs the list of numpy arrays from the chrono sweep and extracts
    the final values to generate the steady state chart.
    """
    nPoints = nPoints * -1
    nPoints = len(data)
    ssArray = np.zeros((nPoints, 4))
    for key, table in enumerate(data):
        ssArray[key, 0] = np.average(table[-2:, 0])
        ssArray[key, 1] = np.average(table[-2:, 1])
        ssArray[key, 2] = np.median(table[-2:, 2])
        ssArray[key, 3] = np.median(table[-2:, 3])
    return ssArray


def record_data_files(Data, SweepPath, RunArgs):
    """Record data."""
    filenames = make_filenames(SweepPath, RunArgs)
    # Write SS File.
    SSArray = generate_ss_array(Data)
    write_data(filenames[0], SSArray, RunArgs, SweepPath=SweepPath)
    # Write Chrono Files
    for key, fn in enumerate(filenames[1]):
        write_data(fn, Data[key], RunArgs, SetPoint=SweepPath[key],
                   SweepPath=SweepPath)
