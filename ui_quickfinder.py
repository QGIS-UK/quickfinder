# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_quickfinder.ui'
#
# Created: Fri Mar  1 14:20:33 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_quickFinder(object):
    def setupUi(self, quickFinder):
        quickFinder.setObjectName(_fromUtf8("quickFinder"))
        quickFinder.resize(268, 218)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(self.dockWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setMargin(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.modeWidgetGroup = QtGui.QWidget(self.frame)
        self.modeWidgetGroup.setObjectName(_fromUtf8("modeWidgetGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.modeWidgetGroup)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.fieldButton = QtGui.QRadioButton(self.modeWidgetGroup)
        self.fieldButton.setChecked(False)
        self.fieldButton.setObjectName(_fromUtf8("fieldButton"))
        self.modeButtonGroup = QtGui.QButtonGroup(quickFinder)
        self.modeButtonGroup.setObjectName(_fromUtf8("modeButtonGroup"))
        self.modeButtonGroup.addButton(self.fieldButton)
        self.gridLayout_5.addWidget(self.fieldButton, 0, 2, 1, 1)
        self.idButton = QtGui.QRadioButton(self.modeWidgetGroup)
        self.idButton.setChecked(True)
        self.idButton.setObjectName(_fromUtf8("idButton"))
        self.modeButtonGroup.addButton(self.idButton)
        self.gridLayout_5.addWidget(self.idButton, 0, 0, 1, 1)
        self.fieldCombo = QtGui.QComboBox(self.modeWidgetGroup)
        self.fieldCombo.setEnabled(False)
        self.fieldCombo.setObjectName(_fromUtf8("fieldCombo"))
        self.gridLayout_5.addWidget(self.fieldCombo, 0, 3, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.modeWidgetGroup, 2, 0, 1, 2)
        self.layerWidgetGroup = QtGui.QWidget(self.frame)
        self.layerWidgetGroup.setObjectName(_fromUtf8("layerWidgetGroup"))
        self.gridLayout = QtGui.QGridLayout(self.layerWidgetGroup)
        self.gridLayout.setMargin(0)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.layerWidgetGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.layerCombo = QtGui.QComboBox(self.layerWidgetGroup)
        self.layerCombo.setObjectName(_fromUtf8("layerCombo"))
        self.gridLayout.addWidget(self.layerCombo, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.layerWidgetGroup, 1, 0, 1, 2)
        self.searchWidgetGroup = QtGui.QWidget(self.frame)
        self.searchWidgetGroup.setObjectName(_fromUtf8("searchWidgetGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.searchWidgetGroup)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 3, 2, 1, 1)
        self.goButton = QtGui.QPushButton(self.searchWidgetGroup)
        self.goButton.setEnabled(True)
        self.goButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.gridLayout_4.addWidget(self.goButton, 3, 3, 1, 1)
        self.widget_2 = QtGui.QWidget(self.searchWidgetGroup)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_8.setMargin(3)
        self.gridLayout_8.setSpacing(3)
        self.gridLayout_8.setMargin(0)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.selectBox = QtGui.QCheckBox(self.widget_2)
        self.selectBox.setEnabled(True)
        self.selectBox.setChecked(True)
        self.selectBox.setObjectName(_fromUtf8("selectBox"))
        self.gridLayout_8.addWidget(self.selectBox, 0, 0, 1, 1)
        self.formBox = QtGui.QCheckBox(self.widget_2)
        self.formBox.setEnabled(True)
        self.formBox.setObjectName(_fromUtf8("formBox"))
        self.gridLayout_8.addWidget(self.formBox, 2, 0, 1, 2)
        self.panBox = QtGui.QCheckBox(self.widget_2)
        self.panBox.setEnabled(True)
        self.panBox.setChecked(True)
        self.panBox.setObjectName(_fromUtf8("panBox"))
        self.gridLayout_8.addWidget(self.panBox, 0, 1, 1, 1)
        self.scaleBox = QtGui.QCheckBox(self.widget_2)
        self.scaleBox.setObjectName(_fromUtf8("scaleBox"))
        self.gridLayout_8.addWidget(self.scaleBox, 0, 2, 1, 1)
        self.gridLayout_4.addWidget(self.widget_2, 3, 0, 1, 1)
        self.widget = QtGui.QWidget(self.searchWidgetGroup)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.widget)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setMargin(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.operatorBox = QtGui.QComboBox(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.operatorBox.sizePolicy().hasHeightForWidth())
        self.operatorBox.setSizePolicy(sizePolicy)
        self.operatorBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.operatorBox.setObjectName(_fromUtf8("operatorBox"))
        self.operatorBox.addItem(_fromUtf8(""))
        self.operatorBox.addItem(_fromUtf8(""))
        self.operatorBox.addItem(_fromUtf8(""))
        self.operatorBox.addItem(_fromUtf8(""))
        self.operatorBox.addItem(_fromUtf8(""))
        self.operatorBox.addItem(_fromUtf8(""))
        self.operatorBox.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.operatorBox, 0, 0, 1, 1)
        self.idLine = QtGui.QLineEdit(self.widget)
        self.idLine.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idLine.sizePolicy().hasHeightForWidth())
        self.idLine.setSizePolicy(sizePolicy)
        self.idLine.setObjectName(_fromUtf8("idLine"))
        self.gridLayout_7.addWidget(self.idLine, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 4)
        self.gridLayout_3.addWidget(self.searchWidgetGroup, 4, 0, 1, 2)
        self.processWidgetGroup = QtGui.QWidget(self.frame)
        self.processWidgetGroup.setObjectName(_fromUtf8("processWidgetGroup"))
        self.gridLayout_6 = QtGui.QGridLayout(self.processWidgetGroup)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.progressBar = QtGui.QProgressBar(self.processWidgetGroup)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_6.addWidget(self.progressBar, 0, 0, 1, 1)
        self.cancelButton = QtGui.QPushButton(self.processWidgetGroup)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout_6.addWidget(self.cancelButton, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.processWidgetGroup, 5, 0, 1, 2)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        quickFinder.setWidget(self.dockWidgetContents)

        self.retranslateUi(quickFinder)
        QtCore.QObject.connect(self.idLine, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.goButton.click)
        QtCore.QObject.connect(self.fieldButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.fieldCombo.setEnabled)
        QtCore.QObject.connect(self.idButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.fieldCombo.setDisabled)
        QtCore.QObject.connect(self.idButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.operatorBox.hide)
        QtCore.QObject.connect(self.fieldButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.operatorBox.show)
        QtCore.QMetaObject.connectSlotsByName(quickFinder)

    def retranslateUi(self, quickFinder):
        quickFinder.setWindowTitle(QtGui.QApplication.translate("quickFinder", "Quick Finder", None, QtGui.QApplication.UnicodeUTF8))
        self.fieldButton.setText(QtGui.QApplication.translate("quickFinder", "Field", None, QtGui.QApplication.UnicodeUTF8))
        self.idButton.setText(QtGui.QApplication.translate("quickFinder", "ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("quickFinder", "Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setText(QtGui.QApplication.translate("quickFinder", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.selectBox.setText(QtGui.QApplication.translate("quickFinder", "select", None, QtGui.QApplication.UnicodeUTF8))
        self.formBox.setText(QtGui.QApplication.translate("quickFinder", "open form", None, QtGui.QApplication.UnicodeUTF8))
        self.panBox.setText(QtGui.QApplication.translate("quickFinder", "pan", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleBox.setText(QtGui.QApplication.translate("quickFinder", "scale", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorBox.setItemText(0, QtGui.QApplication.translate("quickFinder", "IS", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorBox.setItemText(1, QtGui.QApplication.translate("quickFinder", "=   [numeric]", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorBox.setItemText(2, QtGui.QApplication.translate("quickFinder", "<= [numeric]", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorBox.setItemText(3, QtGui.QApplication.translate("quickFinder", ">= [numeric]", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorBox.setItemText(4, QtGui.QApplication.translate("quickFinder", "<   [numeric]", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorBox.setItemText(5, QtGui.QApplication.translate("quickFinder", ">   [numeric]", None, QtGui.QApplication.UnicodeUTF8))
        self.operatorBox.setItemText(6, QtGui.QApplication.translate("quickFinder", "LIKE [text]", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("quickFinder", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

