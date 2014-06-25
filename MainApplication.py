"""Chrono GUI.

This is my first attempt to make a GUI for my Keithley application.
"""

import os
import platform
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from keithley import SMUExperiments as smu
import filemanipulation as fm
import ui_RunConfiguration

__version__ = "0.0.1"

class RunConfigurationDlg(QDialog,
                          ui_RunConfiguration.Ui_RunConfigurationDlg):

    def __init__(self, KWARGS, RunArgs, parent=None):
        super(RunConfigurationDlg, self).__init__(parent)
        self.__KWARGS = KWARGS
        self.__RunArgs = RunArgs
        self.setupUi(self)

#class MainWindow(QMainWindow):
#    """Main window for my application.
#
#    This application is will run chronopotentiostatic runs
#    and output data.
#    """
#
#    def __init__(self, parent=None):
#        super(MainWindow, self).__init__(parent)
#        self.KWARGS = {}
#        self.RunArgs = {}