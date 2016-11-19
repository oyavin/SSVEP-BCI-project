# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Omer\Dropbox\Project\SSVEP v2.4/UI\frmEEGTab.ui'
#
# Created: Wed Dec 09 19:53:21 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_EEGTab(object):
    def setupUi(self, EEGTab):
        EEGTab.setObjectName(_fromUtf8("EEGTab"))
        EEGTab.resize(910, 520)
        self.horizontalLayout = QtGui.QHBoxLayout(EEGTab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.scrollArea = QtGui.QScrollArea(EEGTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(800, 0))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 798, 500))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_EEG = QtGui.QVBoxLayout()
        self.verticalLayout_EEG.setObjectName(_fromUtf8("verticalLayout_EEG"))
        self.horizontalLayout_4.addLayout(self.verticalLayout_EEG)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(EEGTab)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.ElectrodeList = QtGui.QListView(EEGTab)
        self.ElectrodeList.setAcceptDrops(False)
        self.ElectrodeList.setDragEnabled(True)
        self.ElectrodeList.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.ElectrodeList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.ElectrodeList.setAlternatingRowColors(True)
        self.ElectrodeList.setObjectName(_fromUtf8("ElectrodeList"))
        self.verticalLayout_5.addWidget(self.ElectrodeList)
        self.reorganizeButton = QtGui.QPushButton(EEGTab)
        self.reorganizeButton.setObjectName(_fromUtf8("reorganizeButton"))
        self.verticalLayout_5.addWidget(self.reorganizeButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.retranslateUi(EEGTab)
        QtCore.QMetaObject.connectSlotsByName(EEGTab)

    def retranslateUi(self, EEGTab):
        EEGTab.setWindowTitle(_translate("EEGTab", "Form", None))
        self.label_3.setText(_translate("EEGTab", "Displayed Electrodes", None))
        self.reorganizeButton.setText(_translate("EEGTab", "Apply", None))

