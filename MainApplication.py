"""Chrono GUI.

This is my first attempt to make a GUI for my Keithley application.
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
try:
    import visa
    from keithley import SMUExperiments
except:
    pass
import filemanipulation as fm
import ui_MainWindow
import ui_RunConfiguration

__version__ = "0.1.0"


class RunConfigurationDlg(QDialog,
                          ui_RunConfiguration.Ui_RunConfigurationDlg):

    def __init__(self, KWARGS, RunArgs, parent=None):
        """Initialize dialog."""
        super(RunConfigurationDlg, self).__init__(parent)
        settings = QSettings()
        self._KWARGS = KWARGS
        self._RunArgs = RunArgs

        # Get initial Visa List
        self.setupUi(self)
        # Get VISA list and set values in combo box.
        self.updateVISAListOpen()
        # Connect path button
        self.connect(self.BrowseButton, SIGNAL('clicked()'), self.setPathDlg)
        self.connect(self.SMUAddress, SIGNAL('currentIndexChanged(int)'),
                     self.updateVISAListClick)
        self.connect(self.SourceMode, SIGNAL('currentIndexChanged(int)'),
                     self.updateDict)
        self.connect(self.FrontOrBack, SIGNAL('currentIndexChanged(int)'),
                     self.updateDict)
        self.connect(self.TwoOrFour, SIGNAL('currentIndexChanged(int)'),
                     self.updateDict)
        self.connect(self.NPLC, SIGNAL('valueChanged(double)'),
                     self.updateDict)
        self.connect(self.Compliance, SIGNAL('valueChanged(double)'),
                     self.updateDict)
        self.connect(self.MDelay, SIGNAL('valueChanged(double)'),
                     self.updateDict)
        self.connect(self.SMDelay, SIGNAL('valueChanged(double)'),
                     self.updateDict)

        self.ComplianceLevel = settings.value('ComplianceLevel').toDouble()

        self.updateUI()

    def updateUI(self):
        """Update the window.

        This method updates the UI with the current values in the KWARGS and
        PointDelay dictionary. This method should be called anytime the
        dialog is opened, or a value is changed programatically.
        """
        # QDoubleSpinBox
        # Set NPLC to current value. The min and max are already setup
        # in the autogenerated code.
        settings = QSettings()
        self.NPLC.setProperty("value", self._KWARGS['NPLC'])
        # Compliance Level
        self.Compliance.setProperty("value", self.ComplianceLevel)
        settings.setValue('ComplianceLevel', self.ComplianceLevel)
        self.MDelay.setProperty("value", self._KWARGS['PointDelay'])
        self.SMDelay.setProperty("value", self._KWARGS['ExperimentLength'])
        # QComboBox

        # Source Mode SourceMode
        if self._KWARGS['SourceMode'] == 'CURR':
            idx1 = 0
        elif self._KWARGS['SourceMode'] == 'VOLT':
            idx1 = 1
        self.SourceMode.setCurrentIndex(idx1)
        # Front or back FrontOrBack

        # Two or four termianl TwoOrFour

        # QLineEdit
        # PathDisplay
        self.PathDisplay.setText(self._RunArgs['DataPath'])
        # QPushButton
        # BrowseButton

    def argConvert(self, Qstring):
        """Convert string to dict argument.

        This function converts the text string from a combo box
        into the key equivilent in KWARGS or RunArgs. This is
        because the required value in KWARGS is different from
        the value displayed in the box.
        """
        string = str(Qstring)
        if string == 'Front':
            return 'FRON'
        elif string == 'Back':
            return 'REAR'
        elif string == 'Two Terminal':
            return 'OFF'
        elif string == 'Four Terminal':
            return 'ON'
        elif string == 'Current':
            return 'CURR'
        elif string == 'Voltage':
            return 'VOLT'

    def setPathDlg(self):
        """Open dialog to get folder path location."""
        path = QFileDialog.getExistingDirectory(self, 'Select data directory')
        if path:
            self._RunArgs['DataPath'] = (str(QDir.toNativeSeparators(path)) +
                                         '\\')
            self.updateUI()

    def updateVISAListOpen(self):
        """Get list of connected VISA devices and set combo box."""
        try:
            VISAList = visa.get_instruments_list()
        except NameError:
            VISAList = ('No VISA Drivers Found')
        self.SMUAddress.clear()
        self.SMUAddress.addItems(QStringList(VISAList))

    def updateVISAListClick(self):
        """Update VISA dictionary value when changed."""
        self._KWARGS['GPIBAddr'] = str(self.SMUAddress.currentText())

    def updateDict(self):
        """Update dictionary with current user input values."""
        self._KWARGS['GPIBAddr'] = str(self.SMUAddress.currentText())
        self._KWARGS['SourceMode'] = \
            self.argConvert(self.SourceMode.currentText())
        self._KWARGS['TerminalLocation'] = \
            self.argConvert(self.FrontOrBack.currentText())
        self._KWARGS['FourTerminal'] = \
            self.argConvert(self.TwoOrFour.currentText())
        self._KWARGS['NPLC'] = self.NPLC.value()
        self._KWARGS['PointDelay'] = self.MDelay.value()
        self._KWARGS['ExperimentLength'] = self.SMDelay.value()
        self._KWARGS['ComplianceLevel'] = self.Compliance.value()



class MainWindow(QMainWindow,
                 ui_MainWindow.Ui_MainWindow):

    """Main window class.

    This program runs chronopotentiometry experiments using a Keithley
    2400 source meter. Differnet sweep types and run parameters can be
    changed and the output is formatted with a convinent auto-generated
    header specific to the type of testing I am doing.
    """

    def __init__(self, KWARGS, RunArgs, parent=None):
        """Initialize main window."""
        super(MainWindow, self).__init__(parent)
        self._KWARGS = KWARGS
        self._RunArgs = RunArgs
        settings = QSettings()
        if settings.value('ComplianceLevel'):
            self._KWARGS['ComplianceLevel'] = \
                settings.value('ComplianceLevel').toDouble()
        self.__Sweep = [-0.005, -0.004, -0.003, -0.002, -0.001, 0.001, 0.002,
                        0.003, 0.004, 0.005, 0.006, 0.007, 0.008]
        self.ConfigDlg = RunConfigurationDlg(self._KWARGS, self._RunArgs, self)
        self.setupUi(self)
        self.btnSweepConfig.setDisabled(True)
        self.btnSave.setDisabled(True)
        self.btnRun.setDisabled(True)
        # Connect Buttons
        self.connect(self.btnConfigure, SIGNAL('clicked()'),
                     self._openConfigDlg)
        self.connect(self.btnRun, SIGNAL('clicked()'), self._RunExperiment)
        self.connect(self.btnSave, SIGNAL('clicked()'), self._SaveData)

    def _openConfigDlg(self):
        """Open configuration dialog.

        Note that it deletes any current SMU object before opening
        and recreates it once closed to reflect any changes to the
        SMU object in the dialog (mainly the SMU Address).
        """
        try:
            del self.SMU
        except:
            pass
        self.ConfigDlg.show()
        self.ConfigDlg.exec_()
        self.btnRun.setEnabled(True)
        self.updateArguments()

    def _RunExperiment(self):
        """Run experiment.

        This method is to be connected to the run button and runs the
        experiment based on the current values. Eventually, I would like
        to move this into it's own class so I can run it in a parallel
        process so the UI doesn't hang while running.
        """
        self.updateArguments()
        self.SMU = SMUExperiments(self._KWARGS['GPIBAddr'])
        """self._KWARGS = self.ConfigDlg._KWARGS
        self._RunArgs = self.ConfigDlg._RunArgs"""
        self.SMU.KWARGS = self._KWARGS
        self.SMU.RunArgs = self._RunArgs
        self.Data = self.SMU.slow_chrono(self.__Sweep,
                                         self._KWARGS['ExperimentLength'],
                                         self._KWARGS['PointDelay'])
        self.btnSave.setEnabled(True)

    def updateArguments(self):
        """Run to update KWARGS and RunArgs."""
        try:
            self.ConfigDlg.updateDict()
            self._KWARGS = self.ConfigDlg._KWARGS
            self._RunArgs = self.ConfigDlg._RunArgs
        except NameError:
            print('ConfigDlg Not Run')
        self._RunArgs['Membrane'] = str(self.txtMembraneName.text())
        self._RunArgs['MembraneID'] = str(self.txtMembraneID.text())
        self._RunArgs['User'] = str(self.txtUser.text())
        self._RunArgs['Salt'] = str(self.txtSalt.text())
        self._RunArgs['RunNumber'] = str(self.txtRunNumber.text())
        self._RunArgs['CellDesign'] = str(self.txtCellDesign.text())
        self._RunArgs['HighConcentration'] = str(
            self.txtHInletConcentration.text())
        self._RunArgs['HighConductivityIn'] = str(
            self.txtHInletConductivity.text())
        self._RunArgs['HighTempIn'] = str(self.txtHInletTemp.text())
        self._RunArgs['HighConductivityOut'] = str(
            self.txtHOutletConductivity.text())
        self._RunArgs['HighTempOut'] = str(self.txtHOutletTemp.text())
        self._RunArgs['LowConductivityIn'] = str(
            self.txtLInletConductivity_2.text())
        self._RunArgs['LowTempIn'] = str(self.txtLInletTemp_2.text())
        self._RunArgs['LowConductivityOut'] = str(
            self.txtLOutletConductivity_2.text())
        self._RunArgs['LowTempOut'] = str(self.txtLOutletTemp_2.text())
        self._RunArgs['Comments'] = str(self.txtComments.text())

    def _SaveData(self):
        """Run the save data routiene."""
        self.updateArguments()
        fm.record_data_files(self.Data, self.__Sweep, self._RunArgs)
        self.btnSave.setDisabled(True)


DEFAULT_KWARGS = {'SourceMode': 'CURR',
                  'ComplianceLevel': 200,
                  'NPLC': 1, 'TerminalLocation': 'REAR',
                  'FourTerminal': 'ON', 'TriggerCount': 1,
                  'TriggerDelay': 0, 'SourceDelay': 0,
                  'ExperimentLength': 2, 'PointDelay': 0.1,
                  'GPIBAddr': 'GPIBX::YY'}

DEFAULT_RunArgs = {'Membrane': '', 'MembraneID': '',
                   'Salt': 'Salt', 'HighConcentration': '',
                   'HighConductivityIn': '', 'HighTempIn': '',
                   'LowConcentration': '', 'LowConductivityIn': '',
                   'LowTempIn': '', 'HighConductivityOut': '',
                   'HighTempOut': '',
                   'LowConductivityOut': '', 'LowTempOut': '', 'RunNumber': 1,
                   'SourceMode': 'CURR', 'LowConcT': '', 'HighConcT': '',
                   'DataPath': ('C:\\Users\\Harrison\\Box Sync\\penn_state\\'
                                'hickner\\experiments\\conductivity\\'
                                'max_cell_dc_concentration_gradient\\AmB\\'
                                '1.14-0.01\\14-06-19\\'),
                   'User': '', 'CellDesign': '', 'Comments': ''}


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName('siZors')
    app.setApplicationName('SMUExperiments')
    settings = QSettings()
    window = MainWindow(DEFAULT_KWARGS, DEFAULT_RunArgs)
    window.show()
    app.exec_()
    print window._KWARGS
    print window._RunArgs

if __name__ == '__main__':
    main()
