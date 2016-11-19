# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Omer\Dropbox\Project\SSVEP v2.4/UI\frmOperator.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(650, 581)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 10, 413, 103))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.freq_grid = QtGui.QGridLayout(self.layoutWidget)
        self.freq_grid.setMargin(0)
        self.freq_grid.setObjectName(_fromUtf8("freq_grid"))
        self.upFreq = QtGui.QLineEdit(self.layoutWidget)
        self.upFreq.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.upFreq.setObjectName(_fromUtf8("upFreq"))
        self.freq_grid.addWidget(self.upFreq, 0, 1, 1, 1)
        self.leftFreq = QtGui.QLineEdit(self.layoutWidget)
        self.leftFreq.setObjectName(_fromUtf8("leftFreq"))
        self.freq_grid.addWidget(self.leftFreq, 1, 0, 1, 1)
        self.updateButton = QtGui.QPushButton(self.layoutWidget)
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.freq_grid.addWidget(self.updateButton, 3, 1, 1, 1)
        self.rightFreq = QtGui.QLineEdit(self.layoutWidget)
        self.rightFreq.setObjectName(_fromUtf8("rightFreq"))
        self.freq_grid.addWidget(self.rightFreq, 1, 2, 1, 1)
        self.downFreq = QtGui.QLineEdit(self.layoutWidget)
        self.downFreq.setObjectName(_fromUtf8("downFreq"))
        self.freq_grid.addWidget(self.downFreq, 2, 1, 1, 1)
        self.activateButton = QtGui.QPushButton(Form)
        self.activateButton.setGeometry(QtCore.QRect(520, 30, 75, 23))
        self.activateButton.setCheckable(True)
        self.activateButton.setChecked(False)
        self.activateButton.setFlat(False)
        self.activateButton.setObjectName(_fromUtf8("activateButton"))
        self.qwtPlot = Qwt5.QwtPlot(Form)
        self.qwtPlot.setGeometry(QtCore.QRect(0, 150, 581, 201))
        self.qwtPlot.setProperty("propertiesDocument", _fromUtf8(""))
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.TextLabel = Qwt5.QwtTextLabel(Form)
        self.TextLabel.setGeometry(QtCore.QRect(220, 310, 100, 20))
        self.TextLabel.setObjectName(_fromUtf8("TextLabel"))
        self.Dial = Qwt5.QwtDial(Form)
        self.Dial.setGeometry(QtCore.QRect(200, 370, 200, 200))
        self.Dial.setLineWidth(4)
        self.Dial.setObjectName(_fromUtf8("Dial"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.upFreq.setText(_translate("Form", "5", None))
        self.leftFreq.setText(_translate("Form", "15", None))
        self.updateButton.setText(_translate("Form", "Update", None))
        self.rightFreq.setText(_translate("Form", "20", None))
        self.downFreq.setText(_translate("Form", "10", None))
        self.activateButton.setText(_translate("Form", "Activate", None))

from PyQt4 import Qwt5
