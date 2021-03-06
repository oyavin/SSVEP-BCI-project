# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Omer\Dropbox\Project\SSVEP v2.4/UI\frmSSVEPTab.ui'
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

class Ui_SSVEPTab(object):
    def setupUi(self, SSVEPTab):
        SSVEPTab.setObjectName(_fromUtf8("SSVEPTab"))
        SSVEPTab.resize(991, 673)
        font = QtGui.QFont()
        font.setPointSize(9)
        SSVEPTab.setFont(font)
        self.activateButton = QtGui.QPushButton(SSVEPTab)
        self.activateButton.setGeometry(QtCore.QRect(870, 170, 81, 31))
        self.activateButton.setCheckable(True)
        self.activateButton.setChecked(False)
        self.activateButton.setFlat(False)
        self.activateButton.setObjectName(_fromUtf8("activateButton"))
        self.updateButton = QtGui.QPushButton(SSVEPTab)
        self.updateButton.setGeometry(QtCore.QRect(871, 110, 81, 31))
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.layoutWidget = QtGui.QWidget(SSVEPTab)
        self.layoutWidget.setGeometry(QtCore.QRect(590, 450, 51, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.downWidget = BlinkingWidget(self.layoutWidget)
        self.downWidget.setEnabled(True)
        self.downWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.downWidget.setAutoFillBackground(False)
        self.downWidget.setObjectName(_fromUtf8("downWidget"))
        self.gridLayout.addWidget(self.downWidget, 3, 1, 1, 1)
        self.leftWidget = BlinkingWidget(self.layoutWidget)
        self.leftWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.leftWidget.setObjectName(_fromUtf8("leftWidget"))
        self.gridLayout.addWidget(self.leftWidget, 2, 0, 1, 1)
        self.rightWidget = BlinkingWidget(self.layoutWidget)
        self.rightWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.rightWidget.setObjectName(_fromUtf8("rightWidget"))
        self.gridLayout.addWidget(self.rightWidget, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.upWidget = BlinkingWidget(self.layoutWidget)
        self.upWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.upWidget.setAutoFillBackground(False)
        self.upWidget.setObjectName(_fromUtf8("upWidget"))
        self.gridLayout.addWidget(self.upWidget, 1, 1, 1, 1)
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
        self.ShowButton = QtGui.QPushButton(SSVEPTab)
        self.ShowButton.setGeometry(QtCore.QRect(880, 500, 75, 23))
        self.ShowButton.setObjectName(_fromUtf8("ShowButton"))
        self.freq = QtGui.QPlainTextEdit(SSVEPTab)
        self.freq.setGeometry(QtCore.QRect(580, 100, 91, 31))
        self.freq.setObjectName(_fromUtf8("freq"))
        self.label_2 = QtGui.QLabel(SSVEPTab)
        self.label_2.setGeometry(QtCore.QRect(580, 80, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.recordButton = QtGui.QPushButton(SSVEPTab)
        self.recordButton.setGeometry(QtCore.QRect(710, 60, 81, 31))
        self.recordButton.setObjectName(_fromUtf8("recordButton"))
        self.trainButton = QtGui.QPushButton(SSVEPTab)
        self.trainButton.setGeometry(QtCore.QRect(710, 210, 81, 31))
        self.trainButton.setObjectName(_fromUtf8("trainButton"))
        self.discoButton = QtGui.QPushButton(SSVEPTab)
        self.discoButton.setGeometry(QtCore.QRect(870, 140, 81, 31))
        self.discoButton.setObjectName(_fromUtf8("discoButton"))
        self.subname = QtGui.QPlainTextEdit(SSVEPTab)
        self.subname.setGeometry(QtCore.QRect(580, 40, 121, 31))
        self.subname.setObjectName(_fromUtf8("subname"))
        self.label_3 = QtGui.QLabel(SSVEPTab)
        self.label_3.setGeometry(QtCore.QRect(580, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.refreshButton = QtGui.QPushButton(SSVEPTab)
        self.refreshButton.setGeometry(QtCore.QRect(710, 170, 81, 31))
        self.refreshButton.setObjectName(_fromUtf8("refreshButton"))
        self.line = QtGui.QFrame(SSVEPTab)
        self.line.setGeometry(QtCore.QRect(570, 280, 241, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(SSVEPTab)
        self.line_2.setGeometry(QtCore.QRect(570, 140, 241, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(SSVEPTab)
        self.line_3.setGeometry(QtCore.QRect(570, 140, 241, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(SSVEPTab)
        self.line_4.setGeometry(QtCore.QRect(800, 150, 20, 141))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(SSVEPTab)
        self.line_5.setGeometry(QtCore.QRect(560, 150, 20, 141))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.line_6 = QtGui.QFrame(SSVEPTab)
        self.line_6.setGeometry(QtCore.QRect(570, 0, 241, 20))
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.line_7 = QtGui.QFrame(SSVEPTab)
        self.line_7.setGeometry(QtCore.QRect(800, 10, 20, 141))
        self.line_7.setFrameShape(QtGui.QFrame.VLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(SSVEPTab)
        self.line_8.setGeometry(QtCore.QRect(560, 10, 20, 141))
        self.line_8.setFrameShape(QtGui.QFrame.VLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.subjectList = QtGui.QListWidget(SSVEPTab)
        self.subjectList.setGeometry(QtCore.QRect(580, 160, 111, 121))
        self.subjectList.setObjectName(_fromUtf8("subjectList"))
        self.EvaluationButton = QtGui.QPushButton(SSVEPTab)
        self.EvaluationButton.setGeometry(QtCore.QRect(710, 350, 81, 31))
        self.EvaluationButton.setObjectName(_fromUtf8("EvaluationButton"))
        self.DFTPlot = Qwt5.QwtPlot(SSVEPTab)
        self.DFTPlot.setGeometry(QtCore.QRect(10, 30, 531, 301))
        self.DFTPlot.setProperty("propertiesDocument", _fromUtf8(""))
        self.DFTPlot.setObjectName(_fromUtf8("DFTPlot"))
        self.RunButton = QtGui.QPushButton(SSVEPTab)
        self.RunButton.setGeometry(QtCore.QRect(870, 200, 81, 31))
        self.RunButton.setObjectName(_fromUtf8("RunButton"))
        self.freq_2 = QtGui.QPlainTextEdit(SSVEPTab)
        self.freq_2.setGeometry(QtCore.QRect(40, 420, 101, 31))
        self.freq_2.setObjectName(_fromUtf8("freq_2"))
        self.freq_3 = QtGui.QPlainTextEdit(SSVEPTab)
        self.freq_3.setGeometry(QtCore.QRect(40, 480, 531, 51))
        self.freq_3.setObjectName(_fromUtf8("freq_3"))
        self.decision = QtGui.QLabel(SSVEPTab)
        self.decision.setGeometry(QtCore.QRect(40, 420, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.decision.setFont(font)
        self.decision.setText(_fromUtf8(""))
        self.decision.setObjectName(_fromUtf8("decision"))
        self.decision_func = QtGui.QLabel(SSVEPTab)
        self.decision_func.setGeometry(QtCore.QRect(40, 480, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.decision_func.setFont(font)
        self.decision_func.setText(_fromUtf8(""))
        self.decision_func.setObjectName(_fromUtf8("decision_func"))
        self.decision_2 = QtGui.QLabel(SSVEPTab)
        self.decision_2.setGeometry(QtCore.QRect(40, 390, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.decision_2.setFont(font)
        self.decision_2.setObjectName(_fromUtf8("decision_2"))
        self.decision_3 = QtGui.QLabel(SSVEPTab)
        self.decision_3.setGeometry(QtCore.QRect(40, 450, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.decision_3.setFont(font)
        self.decision_3.setObjectName(_fromUtf8("decision_3"))
        self.record_Eval_Button = QtGui.QPushButton(SSVEPTab)
        self.record_Eval_Button.setGeometry(QtCore.QRect(710, 100, 81, 31))
        self.record_Eval_Button.setObjectName(_fromUtf8("record_Eval_Button"))
        self.line_9 = QtGui.QFrame(SSVEPTab)
        self.line_9.setGeometry(QtCore.QRect(570, 420, 241, 20))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.subjectList_2 = QtGui.QListWidget(SSVEPTab)
        self.subjectList_2.setGeometry(QtCore.QRect(580, 300, 111, 121))
        self.subjectList_2.setObjectName(_fromUtf8("subjectList_2"))
        self.line_10 = QtGui.QFrame(SSVEPTab)
        self.line_10.setGeometry(QtCore.QRect(800, 290, 20, 141))
        self.line_10.setFrameShape(QtGui.QFrame.VLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.line_11 = QtGui.QFrame(SSVEPTab)
        self.line_11.setGeometry(QtCore.QRect(570, 280, 241, 20))
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.line_12 = QtGui.QFrame(SSVEPTab)
        self.line_12.setGeometry(QtCore.QRect(560, 290, 20, 141))
        self.line_12.setFrameShape(QtGui.QFrame.VLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.refreshButton_2 = QtGui.QPushButton(SSVEPTab)
        self.refreshButton_2.setGeometry(QtCore.QRect(710, 310, 81, 31))
        self.refreshButton_2.setObjectName(_fromUtf8("refreshButton_2"))
        self.radioRaw = QtGui.QRadioButton(SSVEPTab)
        self.radioRaw.setGeometry(QtCore.QRect(850, 260, 82, 17))
        self.radioRaw.setObjectName(_fromUtf8("radioRaw"))
        self.radioDC = QtGui.QRadioButton(SSVEPTab)
        self.radioDC.setGeometry(QtCore.QRect(850, 290, 82, 17))
        self.radioDC.setObjectName(_fromUtf8("radioDC"))
        self.radioHPF = QtGui.QRadioButton(SSVEPTab)
        self.radioHPF.setGeometry(QtCore.QRect(850, 320, 82, 17))
        self.radioHPF.setObjectName(_fromUtf8("radioHPF"))
        self.radioFinal = QtGui.QRadioButton(SSVEPTab)
        self.radioFinal.setGeometry(QtCore.QRect(850, 350, 131, 17))
        self.radioFinal.setChecked(True)
        self.radioFinal.setObjectName(_fromUtf8("radioFinal"))

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
        self.ShowButton.setText(_translate("SSVEPTab", "Optimise", None))
        self.label_2.setText(_translate("SSVEPTab", "Frequency", None))
        self.recordButton.setText(_translate("SSVEPTab", "Record", None))
        self.trainButton.setText(_translate("SSVEPTab", "Train", None))
        self.discoButton.setText(_translate("SSVEPTab", "Show Cursor", None))
        self.label_3.setText(_translate("SSVEPTab", "Subject Name", None))
        self.refreshButton.setText(_translate("SSVEPTab", "Refresh List", None))
        self.EvaluationButton.setText(_translate("SSVEPTab", "Evaluation", None))
        self.RunButton.setText(_translate("SSVEPTab", "Plot", None))
        self.decision_2.setText(_translate("SSVEPTab", "Decision", None))
        self.decision_3.setText(_translate("SSVEPTab", "Decision function vector", None))
        self.record_Eval_Button.setText(_translate("SSVEPTab", "Record Eval", None))
        self.refreshButton_2.setText(_translate("SSVEPTab", "Refresh List", None))
        self.radioRaw.setText(_translate("SSVEPTab", "Raw Signal", None))
        self.radioDC.setText(_translate("SSVEPTab", "DC filtered", None))
        self.radioHPF.setText(_translate("SSVEPTab", "HP filtered", None))
        self.radioFinal.setText(_translate("SSVEPTab", "Final Signal (Welch)", None))

from PyQt4 import Qwt5
from BlinkingWidget import BlinkingWidget
