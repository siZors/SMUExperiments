# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Harrison\Box Sync\penn_state\hickner\computer\python\active\SMUExperiments (hjc137@psu.edu)\MainWindow.ui'
#
# Created: Sun Jul 06 17:01:00 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(537, 665)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.fmMain = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmMain.sizePolicy().hasHeightForWidth())
        self.fmMain.setSizePolicy(sizePolicy)
        self.fmMain.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmMain.setFrameShadow(QtGui.QFrame.Raised)
        self.fmMain.setObjectName(_fromUtf8("fmMain"))
        self.verticalLayout = QtGui.QVBoxLayout(self.fmMain)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget_2 = QtGui.QWidget(self.fmMain)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(151, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_22 = QtGui.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_3.addWidget(self.label_22)
        spacerItem1 = QtGui.QSpacerItem(150, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_2)
        self.fmGeneral = QtGui.QFrame(self.fmMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmGeneral.sizePolicy().hasHeightForWidth())
        self.fmGeneral.setSizePolicy(sizePolicy)
        self.fmGeneral.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmGeneral.setFrameShadow(QtGui.QFrame.Raised)
        self.fmGeneral.setObjectName(_fromUtf8("fmGeneral"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.fmGeneral)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fmName = QtGui.QFrame(self.fmGeneral)
        self.fmName.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmName.setFrameShadow(QtGui.QFrame.Raised)
        self.fmName.setObjectName(_fromUtf8("fmName"))
        self.formLayout_4 = QtGui.QFormLayout(self.fmName)
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.label = QtGui.QLabel(self.fmName)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.txtMembraneName = QtGui.QLineEdit(self.fmName)
        self.txtMembraneName.setObjectName(_fromUtf8("txtMembraneName"))
        self.formLayout_4.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtMembraneName)
        self.label_2 = QtGui.QLabel(self.fmName)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtMembraneID = QtGui.QLineEdit(self.fmName)
        self.txtMembraneID.setObjectName(_fromUtf8("txtMembraneID"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtMembraneID)
        self.label_27 = QtGui.QLabel(self.fmName)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.formLayout_4.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_27)
        self.txtUser = QtGui.QLineEdit(self.fmName)
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.formLayout_4.setWidget(6, QtGui.QFormLayout.FieldRole, self.txtUser)
        self.horizontalLayout_4.addWidget(self.fmName)
        self.fmSaltRunCell = QtGui.QFrame(self.fmGeneral)
        self.fmSaltRunCell.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmSaltRunCell.setFrameShadow(QtGui.QFrame.Raised)
        self.fmSaltRunCell.setObjectName(_fromUtf8("fmSaltRunCell"))
        self.formLayout_5 = QtGui.QFormLayout(self.fmSaltRunCell)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.label_23 = QtGui.QLabel(self.fmSaltRunCell)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_23)
        self.txtSalt = QtGui.QLineEdit(self.fmSaltRunCell)
        self.txtSalt.setObjectName(_fromUtf8("txtSalt"))
        self.formLayout_5.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtSalt)
        self.label_24 = QtGui.QLabel(self.fmSaltRunCell)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_24)
        self.txtRunNumber = QtGui.QLineEdit(self.fmSaltRunCell)
        self.txtRunNumber.setObjectName(_fromUtf8("txtRunNumber"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtRunNumber)
        self.label_25 = QtGui.QLabel(self.fmSaltRunCell)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.formLayout_5.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_25)
        self.txtCellDesign = QtGui.QLineEdit(self.fmSaltRunCell)
        self.txtCellDesign.setObjectName(_fromUtf8("txtCellDesign"))
        self.formLayout_5.setWidget(7, QtGui.QFormLayout.FieldRole, self.txtCellDesign)
        self.horizontalLayout_4.addWidget(self.fmSaltRunCell)
        self.verticalLayout.addWidget(self.fmGeneral)
        self.widget = QtGui.QWidget(self.fmMain)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(146, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(145, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.widget)
        self.fmSolution = QtGui.QFrame(self.fmMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmSolution.sizePolicy().hasHeightForWidth())
        self.fmSolution.setSizePolicy(sizePolicy)
        self.fmSolution.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmSolution.setFrameShadow(QtGui.QFrame.Raised)
        self.fmSolution.setObjectName(_fromUtf8("fmSolution"))
        self.gridLayout = QtGui.QGridLayout(self.fmSolution)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fmHighConcentration = QtGui.QFrame(self.fmSolution)
        self.fmHighConcentration.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmHighConcentration.setFrameShadow(QtGui.QFrame.Raised)
        self.fmHighConcentration.setObjectName(_fromUtf8("fmHighConcentration"))
        self.formLayout_2 = QtGui.QFormLayout(self.fmHighConcentration)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.fmHighConcentration)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_4)
        self.label_9 = QtGui.QLabel(self.fmHighConcentration)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_9)
        self.label_7 = QtGui.QLabel(self.fmHighConcentration)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtHInletConductivity = QtGui.QLineEdit(self.fmHighConcentration)
        self.txtHInletConductivity.setObjectName(_fromUtf8("txtHInletConductivity"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtHInletConductivity)
        self.label_8 = QtGui.QLabel(self.fmHighConcentration)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_8)
        self.txtHInletTemp = QtGui.QLineEdit(self.fmHighConcentration)
        self.txtHInletTemp.setObjectName(_fromUtf8("txtHInletTemp"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.txtHInletTemp)
        self.label_10 = QtGui.QLabel(self.fmHighConcentration)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.label_10)
        self.label_12 = QtGui.QLabel(self.fmHighConcentration)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_12)
        self.txtHOutletConductivity = QtGui.QLineEdit(self.fmHighConcentration)
        self.txtHOutletConductivity.setObjectName(_fromUtf8("txtHOutletConductivity"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.txtHOutletConductivity)
        self.label_13 = QtGui.QLabel(self.fmHighConcentration)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_13)
        self.txtHOutletTemp = QtGui.QLineEdit(self.fmHighConcentration)
        self.txtHOutletTemp.setObjectName(_fromUtf8("txtHOutletTemp"))
        self.formLayout_2.setWidget(8, QtGui.QFormLayout.FieldRole, self.txtHOutletTemp)
        self.txtHInletConcentration = QtGui.QLineEdit(self.fmHighConcentration)
        self.txtHInletConcentration.setObjectName(_fromUtf8("txtHInletConcentration"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtHInletConcentration)
        self.label_6 = QtGui.QLabel(self.fmHighConcentration)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.gridLayout.addWidget(self.fmHighConcentration, 0, 0, 1, 1)
        self.fmLowConcentration = QtGui.QFrame(self.fmSolution)
        self.fmLowConcentration.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmLowConcentration.setFrameShadow(QtGui.QFrame.Raised)
        self.fmLowConcentration.setObjectName(_fromUtf8("fmLowConcentration"))
        self.formLayout_3 = QtGui.QFormLayout(self.fmLowConcentration)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_5 = QtGui.QLabel(self.fmLowConcentration)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.label_5)
        self.label_14 = QtGui.QLabel(self.fmLowConcentration)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.label_14)
        self.label_16 = QtGui.QLabel(self.fmLowConcentration)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_16)
        self.txtLInletConductivity_2 = QtGui.QLineEdit(self.fmLowConcentration)
        self.txtLInletConductivity_2.setObjectName(_fromUtf8("txtLInletConductivity_2"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtLInletConductivity_2)
        self.label_17 = QtGui.QLabel(self.fmLowConcentration)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_17)
        self.txtLInletTemp_2 = QtGui.QLineEdit(self.fmLowConcentration)
        self.txtLInletTemp_2.setObjectName(_fromUtf8("txtLInletTemp_2"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.txtLInletTemp_2)
        self.label_18 = QtGui.QLabel(self.fmLowConcentration)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_3.setWidget(6, QtGui.QFormLayout.FieldRole, self.label_18)
        self.label_20 = QtGui.QLabel(self.fmLowConcentration)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_20)
        self.txtLOutletConductivity_2 = QtGui.QLineEdit(self.fmLowConcentration)
        self.txtLOutletConductivity_2.setObjectName(_fromUtf8("txtLOutletConductivity_2"))
        self.formLayout_3.setWidget(7, QtGui.QFormLayout.FieldRole, self.txtLOutletConductivity_2)
        self.label_21 = QtGui.QLabel(self.fmLowConcentration)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_21)
        self.txtLOutletTemp_2 = QtGui.QLineEdit(self.fmLowConcentration)
        self.txtLOutletTemp_2.setObjectName(_fromUtf8("txtLOutletTemp_2"))
        self.formLayout_3.setWidget(8, QtGui.QFormLayout.FieldRole, self.txtLOutletTemp_2)
        self.txtLInletConcentration_2 = QtGui.QLineEdit(self.fmLowConcentration)
        self.txtLInletConcentration_2.setObjectName(_fromUtf8("txtLInletConcentration_2"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.txtLInletConcentration_2)
        self.label_15 = QtGui.QLabel(self.fmLowConcentration)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_15)
        self.gridLayout.addWidget(self.fmLowConcentration, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.fmSolution)
        self.fmComments = QtGui.QFrame(self.fmMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmComments.sizePolicy().hasHeightForWidth())
        self.fmComments.setSizePolicy(sizePolicy)
        self.fmComments.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmComments.setFrameShadow(QtGui.QFrame.Raised)
        self.fmComments.setObjectName(_fromUtf8("fmComments"))
        self.formLayout = QtGui.QFormLayout(self.fmComments)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_26 = QtGui.QLabel(self.fmComments)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_26)
        self.txtComments = QtGui.QLineEdit(self.fmComments)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtComments.sizePolicy().hasHeightForWidth())
        self.txtComments.setSizePolicy(sizePolicy)
        self.txtComments.setObjectName(_fromUtf8("txtComments"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txtComments)
        self.verticalLayout.addWidget(self.fmComments)
        self.fmButtons = QtGui.QFrame(self.fmMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmButtons.sizePolicy().hasHeightForWidth())
        self.fmButtons.setSizePolicy(sizePolicy)
        self.fmButtons.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fmButtons.setFrameShadow(QtGui.QFrame.Raised)
        self.fmButtons.setObjectName(_fromUtf8("fmButtons"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fmButtons)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.btnConfigure = QtGui.QPushButton(self.fmButtons)
        self.btnConfigure.setObjectName(_fromUtf8("btnConfigure"))
        self.horizontalLayout.addWidget(self.btnConfigure)
        self.btnSweepConfig = QtGui.QPushButton(self.fmButtons)
        self.btnSweepConfig.setObjectName(_fromUtf8("btnSweepConfig"))
        self.horizontalLayout.addWidget(self.btnSweepConfig)
        self.btnRun = QtGui.QPushButton(self.fmButtons)
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.horizontalLayout.addWidget(self.btnRun)
        self.btnSave = QtGui.QPushButton(self.fmButtons)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.horizontalLayout.addWidget(self.btnSave)
        self.verticalLayout.addWidget(self.fmButtons)
        self.verticalLayout_2.addWidget(self.fmMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.label.setBuddy(self.txtMembraneName)
        self.label_2.setBuddy(self.txtMembraneID)
        self.label_27.setBuddy(self.txtUser)
        self.label_23.setBuddy(self.txtSalt)
        self.label_24.setBuddy(self.txtRunNumber)
        self.label_25.setBuddy(self.txtCellDesign)
        self.label_4.setBuddy(self.txtHInletConcentration)
        self.label_7.setBuddy(self.txtHInletConductivity)
        self.label_8.setBuddy(self.txtHInletTemp)
        self.label_12.setBuddy(self.txtHOutletConductivity)
        self.label_13.setBuddy(self.txtHOutletTemp)
        self.label_6.setBuddy(self.txtHInletConcentration)
        self.label_5.setBuddy(self.txtLInletConcentration_2)
        self.label_16.setBuddy(self.txtLInletConductivity_2)
        self.label_17.setBuddy(self.txtLInletTemp_2)
        self.label_20.setBuddy(self.txtLOutletConductivity_2)
        self.label_21.setBuddy(self.txtLOutletTemp_2)
        self.label_15.setBuddy(self.txtLInletConcentration_2)
        self.label_26.setBuddy(self.txtComments)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.txtMembraneName, self.txtMembraneID)
        MainWindow.setTabOrder(self.txtMembraneID, self.txtUser)
        MainWindow.setTabOrder(self.txtUser, self.txtSalt)
        MainWindow.setTabOrder(self.txtSalt, self.txtRunNumber)
        MainWindow.setTabOrder(self.txtRunNumber, self.txtCellDesign)
        MainWindow.setTabOrder(self.txtCellDesign, self.txtHInletConcentration)
        MainWindow.setTabOrder(self.txtHInletConcentration, self.txtHInletConductivity)
        MainWindow.setTabOrder(self.txtHInletConductivity, self.txtHInletTemp)
        MainWindow.setTabOrder(self.txtHInletTemp, self.txtLInletConcentration_2)
        MainWindow.setTabOrder(self.txtLInletConcentration_2, self.txtLInletConductivity_2)
        MainWindow.setTabOrder(self.txtLInletConductivity_2, self.txtLInletTemp_2)
        MainWindow.setTabOrder(self.txtLInletTemp_2, self.txtHOutletConductivity)
        MainWindow.setTabOrder(self.txtHOutletConductivity, self.txtHOutletTemp)
        MainWindow.setTabOrder(self.txtHOutletTemp, self.txtLOutletConductivity_2)
        MainWindow.setTabOrder(self.txtLOutletConductivity_2, self.txtLOutletTemp_2)
        MainWindow.setTabOrder(self.txtLOutletTemp_2, self.txtComments)
        MainWindow.setTabOrder(self.txtComments, self.btnConfigure)
        MainWindow.setTabOrder(self.btnConfigure, self.btnSweepConfig)
        MainWindow.setTabOrder(self.btnSweepConfig, self.btnRun)
        MainWindow.setTabOrder(self.btnRun, self.btnSave)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_22.setText(_translate("MainWindow", "General Properties", None))
        self.label.setText(_translate("MainWindow", "&Membrane Name", None))
        self.label_2.setText(_translate("MainWindow", "Membrane &ID", None))
        self.label_27.setText(_translate("MainWindow", "User", None))
        self.label_23.setText(_translate("MainWindow", "Salt", None))
        self.label_24.setText(_translate("MainWindow", "Run Numer     ", None))
        self.label_25.setText(_translate("MainWindow", "Cell Design", None))
        self.label_3.setText(_translate("MainWindow", "Solution Properties", None))
        self.label_4.setText(_translate("MainWindow", "&High Concentration", None))
        self.label_9.setText(_translate("MainWindow", "Inlet", None))
        self.label_7.setText(_translate("MainWindow", "Conductivity", None))
        self.label_8.setText(_translate("MainWindow", "Temperature", None))
        self.label_10.setText(_translate("MainWindow", "Outlet", None))
        self.label_12.setText(_translate("MainWindow", "Conductivity", None))
        self.label_13.setText(_translate("MainWindow", "Temperature", None))
        self.label_6.setText(_translate("MainWindow", "Concentration  ", None))
        self.label_5.setText(_translate("MainWindow", "&Low Concentration", None))
        self.label_14.setText(_translate("MainWindow", "Inlet", None))
        self.label_16.setText(_translate("MainWindow", "Conductivity", None))
        self.label_17.setText(_translate("MainWindow", "Temperature", None))
        self.label_18.setText(_translate("MainWindow", "Outlet", None))
        self.label_20.setText(_translate("MainWindow", "Conductivity", None))
        self.label_21.setText(_translate("MainWindow", "Temperature", None))
        self.label_15.setText(_translate("MainWindow", "Concentration", None))
        self.label_26.setText(_translate("MainWindow", "    &Comments       ", None))
        self.btnConfigure.setText(_translate("MainWindow", "Configure", None))
        self.btnSweepConfig.setText(_translate("MainWindow", "Sweep Config", None))
        self.btnRun.setText(_translate("MainWindow", "&Run", None))
        self.btnSave.setText(_translate("MainWindow", "&Save Data", None))

