# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Omer\Dropbox\Project\SSVEP v2.4/UI\frmSSVEPTab_old.ui'
#
# Created: Wed Dec 09 19:53:22 2015
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

class Ui_SSVEPTab(object):
    def setupUi(self, SSVEPTab):
        SSVEPTab.setObjectName(_fromUtf8("SSVEPTab"))
        SSVEPTab.resize(991, 673)
        font = QtGui.QFont()
        font.setPointSize(9)
        SSVEPTab.setFont(font)
        self.activateButton = QtGui.QPushButton(SSVEPTab)
        self.activateButton.setGeometry(QtCore.QRect(871, 140, 75, 23))
        self.activateButton.setCheckable(True)
        self.activateButton.setChecked(False)
        self.activateButton.setFlat(False)
        self.activateButton.setObjectName(_fromUtf8("activateButton"))
        self.updateButton = QtGui.QPushButton(SSVEPTab)
        self.updateButton.setGeometry(QtCore.QRect(871, 110, 75, 23))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.layoutWidget = QtGui.QWidget(SSVEPTab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, -10, 551, 551))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.downWidget = BlinkingWidget(self.layoutWidget)
        self.downWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.downWidget.setObjectName(_fromUtf8("downWidget"))
        self.gridLayout.addWidget(self.downWidget, 3, 1, 1, 1)
        self.leftWidget = BlinkingWidget(self.layoutWidget)
        self.leftWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.leftWidget.setObjectName(_fromUtf8("leftWidget"))
        self.gridLayout.addWidget(self.leftWidget, 2, 0, 1, 1)
        self.upWidget = BlinkingWidget(self.layoutWidget)
        self.upWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.upWidget.setObjectName(_fromUtf8("upWidget"))
        self.gridLayout.addWidget(self.upWidget, 1, 1, 1, 1)
        self.rightWidget = BlinkingWidget(self.layoutWidget)
        self.rightWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.rightWidget.setObjectName(_fromUtf8("rightWidget"))
        self.gridLayout.addWidget(self.rightWidget, 2, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.upFreq = QtGui.QLineEdit(SSVEPTab)
        self.upFreq.setGeometry(QtCore.QRect(901, 20, 21, 21))
        self.upFreq.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.upFreq.setObjectName(_fromUtf8("upFreq"))
        self.leftFreq = QtGui.QLineEdit(SSVEPTab)
        self.leftFreq.setGeometry(QtCore.QRect(861, 50, 21, 20))
        self.leftFreq.setObjectName(_fromUtf8("leftFreq"))
        self.rightFreq = QtGui.QLineEdit(SSVEPTab)
        self.rightFreq.setGeometry(QtCore.QRect(931, 50, 21, 20))
        self.rightFreq.setMouseTracking(True)
        self.rightFreq.setObjectName(_fromUtf8("rightFreq"))
        self.downFreq = QtGui.QLineEdit(SSVEPTab)
        self.downFreq.setGeometry(QtCore.QRect(900, 80, 21, 20))
        self.downFreq.setObjectName(_fromUtf8("downFreq"))
        self.listView = QtGui.QListView(SSVEPTab)
        self.listView.setGeometry(QtCore.QRect(870, 200, 81, 291))
        self.listView.setMouseTracking(False)
        self.listView.setFrameShape(QtGui.QFrame.StyledPanel)
        self.listView.setFrameShadow(QtGui.QFrame.Sunken)
        self.listView.setLineWidth(14)
        self.listView.setDragEnabled(False)
        self.listView.setDragDropOverwriteMode(False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setProperty("isWrapping", False)
        self.listView.setLayoutMode(QtGui.QListView.SinglePass)
        self.listView.setUniformItemSizes(False)
        self.listView.setSelectionRectVisible(False)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.checkBox = QtGui.QCheckBox(SSVEPTab)
        self.checkBox.setGeometry(QtCore.QRect(880, 210, 70, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_2.setGeometry(QtCore.QRect(880, 230, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_3.setGeometry(QtCore.QRect(880, 250, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_4.setGeometry(QtCore.QRect(880, 270, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_5.setGeometry(QtCore.QRect(880, 290, 70, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_6.setGeometry(QtCore.QRect(880, 410, 70, 17))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_7.setGeometry(QtCore.QRect(880, 310, 70, 17))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.checkBox_8 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_8.setGeometry(QtCore.QRect(880, 370, 70, 17))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox_9 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_9.setGeometry(QtCore.QRect(880, 330, 70, 17))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_10 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_10.setGeometry(QtCore.QRect(880, 390, 70, 17))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.checkBox_11 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_11.setGeometry(QtCore.QRect(880, 350, 70, 17))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.checkBox_12 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_12.setGeometry(QtCore.QRect(880, 430, 70, 17))
        self.checkBox_12.setObjectName(_fromUtf8("checkBox_12"))
        self.checkBox_13 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_13.setGeometry(QtCore.QRect(880, 450, 70, 17))
        self.checkBox_13.setObjectName(_fromUtf8("checkBox_13"))
        self.checkBox_14 = QtGui.QCheckBox(SSVEPTab)
        self.checkBox_14.setGeometry(QtCore.QRect(880, 470, 70, 17))
        self.checkBox_14.setObjectName(_fromUtf8("checkBox_14"))
        self.ShowButton = QtGui.QPushButton(SSVEPTab)
        self.ShowButton.setGeometry(QtCore.QRect(870, 500, 75, 23))
        self.ShowButton.setObjectName(_fromUtf8("ShowButton"))
        self.label = QtGui.QLabel(SSVEPTab)
        self.label.setGeometry(QtCore.QRect(880, 170, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.discoButton = QtGui.QPushButton(SSVEPTab)
        self.discoButton.setGeometry(QtCore.QRect(770, 450, 91, 23))
        self.discoButton.setObjectName(_fromUtf8("discoButton"))
        self.subjectList = QtGui.QListWidget(SSVEPTab)
        self.subjectList.setGeometry(QtCore.QRect(570, 330, 201, 101))
        self.subjectList.setObjectName(_fromUtf8("subjectList"))
        self.learnButton = QtGui.QPushButton(SSVEPTab)
        self.learnButton.setGeometry(QtCore.QRect(660, 450, 75, 23))
        self.learnButton.setObjectName(_fromUtf8("learnButton"))
        self.refreshButton = QtGui.QPushButton(SSVEPTab)
        self.refreshButton.setGeometry(QtCore.QRect(570, 450, 75, 23))
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))

        self.retranslateUi(SSVEPTab)
        QtCore.QMetaObject.connectSlotsByName(SSVEPTab)

    def retranslateUi(self, SSVEPTab):
        SSVEPTab.setWindowTitle(_translate("SSVEPTab", "Form", None))
        self.activateButton.setText(_translate("SSVEPTab", "Activate", None))
        self.updateButton.setText(_translate("SSVEPTab", "Update", None))
        self.upFreq.setText(_translate("SSVEPTab", "5", None))
        self.leftFreq.setText(_translate("SSVEPTab", "15", None))
        self.rightFreq.setText(_translate("SSVEPTab", "20", None))
        self.downFreq.setText(_translate("SSVEPTab", "10", None))
        self.checkBox.setText(_translate("SSVEPTab", "AF3", None))
        self.checkBox_2.setText(_translate("SSVEPTab", "F7", None))
        self.checkBox_3.setText(_translate("SSVEPTab", "F3", None))
        self.checkBox_4.setText(_translate("SSVEPTab", "FC5", None))
        self.checkBox_5.setText(_translate("SSVEPTab", "T7", None))
        self.checkBox_6.setText(_translate("SSVEPTab", "FC6", None))
        self.checkBox_7.setText(_translate("SSVEPTab", "P7", None))
        self.checkBox_8.setText(_translate("SSVEPTab", "P8", None))
        self.checkBox_9.setText(_translate("SSVEPTab", "O1", None))
        self.checkBox_10.setText(_translate("SSVEPTab", "T8", None))
        self.checkBox_11.setText(_translate("SSVEPTab", "O2", None))
        self.checkBox_12.setText(_translate("SSVEPTab", "F4", None))
        self.checkBox_13.setText(_translate("SSVEPTab", "F8", None))
        self.checkBox_14.setText(_translate("SSVEPTab", "AF4", None))
        self.ShowButton.setText(_translate("SSVEPTab", "Show", None))
        self.label.setText(_translate("SSVEPTab", "DFT", None))
        self.discoButton.setText(_translate("SSVEPTab", "Show Cursor", None))
        self.learnButton.setText(_translate("SSVEPTab", "Learn", None))
        self.refreshButton.setText(_translate("SSVEPTab", "Refresh List", None))

from BlinkingWidget import BlinkingWidget
