# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Omer\Dropbox\Project\SSVEP v2.4/UI\frmEEGPlot.ui'
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

class Ui_EEG_Plot(object):
    def setupUi(self, EEG_Plot):
        EEG_Plot.setObjectName(_fromUtf8("EEG_Plot"))
        EEG_Plot.resize(567, 251)
        self.horizontalLayout = QtGui.QHBoxLayout(EEG_Plot)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(EEG_Plot)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.qwtPlot = Qwt5.QwtPlot(EEG_Plot)
        self.qwtPlot.setObjectName(_fromUtf8("qwtPlot"))
        self.horizontalLayout.addWidget(self.qwtPlot)

        self.retranslateUi(EEG_Plot)
        QtCore.QMetaObject.connectSlotsByName(EEG_Plot)

    def retranslateUi(self, EEG_Plot):
        EEG_Plot.setWindowTitle(_translate("EEG_Plot", "Form", None))
        self.label.setText(_translate("EEG_Plot", "TextLabel", None))

from PyQt4 import Qwt5
