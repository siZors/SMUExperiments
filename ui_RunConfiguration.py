# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Harrison\Box Sync\penn_state\hickner\computer\python\keithleyUI\RunConfiguration.ui'
#
# Created: Tue Jun 24 20:08:24 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RunConfigurationDlg(object):
    def setupUi(self, RunConfigurationDlg):
        RunConfigurationDlg.setObjectName(_fromUtf8("RunConfigurationDlg"))
        RunConfigurationDlg.resize(557, 392)
        self.gridLayout = QtGui.QGridLayout(RunConfigurationDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.PathLbl = QtGui.QLabel(RunConfigurationDlg)
        self.PathLbl.setObjectName(_fromUtf8("PathLbl"))
        self.gridLayout.addWidget(self.PathLbl, 0, 0, 1, 1)
        self.PathDisplay = QtGui.QLineEdit(RunConfigurationDlg)
        self.PathDisplay.setReadOnly(True)
        self.PathDisplay.setObjectName(_fromUtf8("PathDisplay"))
        self.gridLayout.addWidget(self.PathDisplay, 0, 1, 1, 4)
        self.BrowseButton = QtGui.QPushButton(RunConfigurationDlg)
        self.BrowseButton.setObjectName(_fromUtf8("BrowseButton"))
        self.gridLayout.addWidget(self.BrowseButton, 0, 5, 1, 1)
        self.SMUAddressLbl = QtGui.QLabel(RunConfigurationDlg)
        self.SMUAddressLbl.setObjectName(_fromUtf8("SMUAddressLbl"))
        self.gridLayout.addWidget(self.SMUAddressLbl, 1, 0, 1, 1)
        self.SMUAddress = QtGui.QComboBox(RunConfigurationDlg)
        self.SMUAddress.setObjectName(_fromUtf8("SMUAddress"))
        self.gridLayout.addWidget(self.SMUAddress, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(462, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.NPLCLbl = QtGui.QLabel(RunConfigurationDlg)
        self.NPLCLbl.setObjectName(_fromUtf8("NPLCLbl"))
        self.gridLayout.addWidget(self.NPLCLbl, 1, 3, 1, 1)
        self.SourceModeLbl = QtGui.QLabel(RunConfigurationDlg)
        self.SourceModeLbl.setObjectName(_fromUtf8("SourceModeLbl"))
        self.gridLayout.addWidget(self.SourceModeLbl, 2, 0, 1, 1)
        self.SourceMode = QtGui.QComboBox(RunConfigurationDlg)
        self.SourceMode.setObjectName(_fromUtf8("SourceMode"))
        self.gridLayout.addWidget(self.SourceMode, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(183, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 2, 1, 1)
        self.ComplianceLbl = QtGui.QLabel(RunConfigurationDlg)
        self.ComplianceLbl.setObjectName(_fromUtf8("ComplianceLbl"))
        self.gridLayout.addWidget(self.ComplianceLbl, 2, 3, 1, 2)
        self.Compliance = QtGui.QDoubleSpinBox(RunConfigurationDlg)
        self.Compliance.setMaximum(210.0)
        self.Compliance.setProperty("value", 200.0)
        self.Compliance.setObjectName(_fromUtf8("Compliance"))
        self.gridLayout.addWidget(self.Compliance, 2, 5, 1, 1)
        self.FrontOrBackLbl = QtGui.QLabel(RunConfigurationDlg)
        self.FrontOrBackLbl.setObjectName(_fromUtf8("FrontOrBackLbl"))
        self.gridLayout.addWidget(self.FrontOrBackLbl, 3, 0, 1, 1)
        self.FrontOrBack = QtGui.QComboBox(RunConfigurationDlg)
        self.FrontOrBack.setObjectName(_fromUtf8("FrontOrBack"))
        self.gridLayout.addWidget(self.FrontOrBack, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(183, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.MDelayLbl = QtGui.QLabel(RunConfigurationDlg)
        self.MDelayLbl.setObjectName(_fromUtf8("MDelayLbl"))
        self.gridLayout.addWidget(self.MDelayLbl, 3, 3, 1, 2)
        self.MDelay = QtGui.QDoubleSpinBox(RunConfigurationDlg)
        self.MDelay.setSingleStep(0.1)
        self.MDelay.setProperty("value", 0.2)
        self.MDelay.setObjectName(_fromUtf8("MDelay"))
        self.gridLayout.addWidget(self.MDelay, 3, 5, 1, 1)
        self.TwoOrFourLbl = QtGui.QLabel(RunConfigurationDlg)
        self.TwoOrFourLbl.setObjectName(_fromUtf8("TwoOrFourLbl"))
        self.gridLayout.addWidget(self.TwoOrFourLbl, 4, 0, 1, 1)
        self.TwoOrFour = QtGui.QComboBox(RunConfigurationDlg)
        self.TwoOrFour.setObjectName(_fromUtf8("TwoOrFour"))
        self.gridLayout.addWidget(self.TwoOrFour, 4, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(183, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 2, 1, 1)
        self.SMDelayLbl = QtGui.QLabel(RunConfigurationDlg)
        self.SMDelayLbl.setObjectName(_fromUtf8("SMDelayLbl"))
        self.gridLayout.addWidget(self.SMDelayLbl, 4, 3, 1, 2)
        self.SMDelay = QtGui.QDoubleSpinBox(RunConfigurationDlg)
        self.SMDelay.setMinimum(0.1)
        self.SMDelay.setMaximum(100000.0)
        self.SMDelay.setProperty("value", 2.0)
        self.SMDelay.setObjectName(_fromUtf8("SMDelay"))
        self.gridLayout.addWidget(self.SMDelay, 4, 5, 1, 1)
        self.OKCancel = QtGui.QDialogButtonBox(RunConfigurationDlg)
        self.OKCancel.setOrientation(QtCore.Qt.Horizontal)
        self.OKCancel.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.OKCancel.setObjectName(_fromUtf8("OKCancel"))
        self.gridLayout.addWidget(self.OKCancel, 5, 4, 1, 2)
        self.NPLC = QtGui.QDoubleSpinBox(RunConfigurationDlg)
        self.NPLC.setMinimum(0.01)
        self.NPLC.setMaximum(10.0)
        self.NPLC.setSingleStep(0.1)
        self.NPLC.setProperty("value", 1.0)
        self.NPLC.setObjectName(_fromUtf8("NPLC"))
        self.gridLayout.addWidget(self.NPLC, 1, 5, 1, 1)
        self.PathLbl.setBuddy(self.BrowseButton)
        self.SMUAddressLbl.setBuddy(self.SMUAddress)
        self.NPLCLbl.setBuddy(self.NPLC)
        self.SourceModeLbl.setBuddy(self.SourceMode)
        self.ComplianceLbl.setBuddy(self.Compliance)
        self.FrontOrBackLbl.setBuddy(self.FrontOrBack)
        self.MDelayLbl.setBuddy(self.MDelay)
        self.TwoOrFourLbl.setBuddy(self.TwoOrFour)
        self.SMDelayLbl.setBuddy(self.SMDelay)

        self.retranslateUi(RunConfigurationDlg)
        QtCore.QObject.connect(self.OKCancel, QtCore.SIGNAL(_fromUtf8("accepted()")), RunConfigurationDlg.accept)
        QtCore.QObject.connect(self.OKCancel, QtCore.SIGNAL(_fromUtf8("rejected()")), RunConfigurationDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(RunConfigurationDlg)

    def retranslateUi(self, RunConfigurationDlg):
        RunConfigurationDlg.setWindowTitle(_translate("RunConfigurationDlg", "Dialog", None))
        self.PathLbl.setText(_translate("RunConfigurationDlg", "Data Path", None))
        self.BrowseButton.setText(_translate("RunConfigurationDlg", "&Browse", None))
        self.SMUAddressLbl.setText(_translate("RunConfigurationDlg", "&SMU Address", None))
        self.NPLCLbl.setText(_translate("RunConfigurationDlg", "&NPLC", None))
        self.SourceModeLbl.setText(_translate("RunConfigurationDlg", "Sou&rce Mode", None))
        self.ComplianceLbl.setText(_translate("RunConfigurationDlg", "&Compliance\n"
"Level", None))
        self.FrontOrBackLbl.setText(_translate("RunConfigurationDlg", "Front or Back", None))
        self.MDelayLbl.setText(_translate("RunConfigurationDlg", "Measurement\n"
"De&lay", None))
        self.TwoOrFourLbl.setText(_translate("RunConfigurationDlg", "Two or\n"
"Four Terminal", None))
        self.SMDelayLbl.setText(_translate("RunConfigurationDlg", "Source Measure\n"
"&Delay", None))

