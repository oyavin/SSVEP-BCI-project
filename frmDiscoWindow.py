# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Omer\Dropbox\Project\SSVEP v2.4/UI\frmDiscoWindow.ui'
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

class Ui_DiscoWindow(object):
    def setupUi(self, DiscoWindow):
        DiscoWindow.setObjectName(_fromUtf8("DiscoWindow"))
        DiscoWindow.resize(1589, 919)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DiscoWindow.sizePolicy().hasHeightForWidth())
        DiscoWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        DiscoWindow.setFont(font)
        DiscoWindow.setMouseTracking(False)
        DiscoWindow.setAutoFillBackground(False)

        self.pic_label = QtGui.QLabel(DiscoWindow)
        self.pic_label.setGeometry(QtCore.QRect(1040, 550, 221, 281))
        self.pic_label.setAcceptDrops(False)
        self.pic_label.setAutoFillBackground(False)
        self.pic_label.setText(_fromUtf8(""))
        self.pic_label.setObjectName(_fromUtf8("pic_label"))

        self.grid_widget = QtGui.QWidget(DiscoWindow)
        self.grid_widget.setGeometry(QtCore.QRect(60, 40, 481, 461))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grid_widget.sizePolicy().hasHeightForWidth())
        self.grid_widget.setSizePolicy(sizePolicy)
        self.grid_widget.setMouseTracking(True)
        self.grid_widget.setObjectName(_fromUtf8("grid_widget"))
        self.gridLayout = QtGui.QGridLayout(self.grid_widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.uplabel = QtGui.QLabel(self.grid_widget)
        self.uplabel.setEnabled(True)
        self.uplabel.setFixedSize(QtCore.QSize(170, 170))
        self.uplabel.setMouseTracking(False)
        self.uplabel.setAutoFillBackground(False)
        self.uplabel.setObjectName(_fromUtf8("uplabel"))
        self.uplabel.setAlignment(QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.uplabel, 1, 1, 1, 1)

        self.leftlabel = QtGui.QLabel(self.grid_widget)
        self.leftlabel.setEnabled(True)
        self.leftlabel.setFixedSize(QtCore.QSize(170, 170))
        self.leftlabel.setMouseTracking(False)
        self.leftlabel.setAutoFillBackground(False)
        self.leftlabel.setObjectName(_fromUtf8("leftlabel"))
        self.leftlabel.setAlignment(QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.leftlabel, 2, 0, 1, 1)

        self.rightlabel = QtGui.QLabel(self.grid_widget)
        self.rightlabel.setEnabled(True)
        self.rightlabel.setFixedSize(QtCore.QSize(170, 170))
        self.rightlabel.setMouseTracking(False)
        self.rightlabel.setAutoFillBackground(False)
        self.rightlabel.setObjectName(_fromUtf8("rightlabel"))
        self.rightlabel.setAlignment(QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.rightlabel, 2, 2, 1, 1)

        self.downlabel = QtGui.QLabel(self.grid_widget)
        self.downlabel.setEnabled(True)
        self.downlabel.setFixedSize(QtCore.QSize(170, 170))
        self.downlabel.setMouseTracking(False)
        self.downlabel.setAutoFillBackground(True)
        self.downlabel.setObjectName(_fromUtf8("downlabel"))
        self.downlabel.setAlignment(QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.downlabel, 3, 1, 1, 1)

        self.midwidget = QtGui.QWidget(self.grid_widget)
        self.midwidget.setObjectName(_fromUtf8("midwidget"))
        self.midlabel = QtGui.QLabel(self.midwidget)
        self.midlabel.setGeometry(QtCore.QRect(0, -10, 171, 191))
        self.midlabel.setText(_fromUtf8(""))
        self.midlabel.setObjectName(_fromUtf8("midlabel"))
        self.gridLayout.addWidget(self.midwidget, 2, 1, 1, 1)
        self.leftWidget = CheckeredArrowWidget(self.grid_widget)
        self.leftWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.leftWidget.setAutoFillBackground(True)
        self.leftWidget.setObjectName(_fromUtf8("leftWidget"))
        self.gridLayout.addWidget(self.leftWidget, 2, 0, 1, 1)
        self.rightWidget = CheckeredArrowWidget(self.grid_widget)
        self.rightWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.rightWidget.setAutoFillBackground(True)
        self.rightWidget.setObjectName(_fromUtf8("rightWidget"))
        self.gridLayout.addWidget(self.rightWidget, 2, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(180, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(180, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.upWidget = CheckeredArrowWidget(self.grid_widget)
        self.upWidget.setEnabled(True)
        self.upWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.upWidget.setAutoFillBackground(True)
        self.upWidget.setObjectName(_fromUtf8("upWidget"))
        self.gridLayout.addWidget(self.upWidget, 1, 1, 1, 1)
        self.downWidget = CheckeredArrowWidget(self.grid_widget)
        self.downWidget.setEnabled(True)
        self.downWidget.setMinimumSize(QtCore.QSize(170, 170))
        self.downWidget.setMouseTracking(False)
        self.downWidget.setAutoFillBackground(True)
        self.downWidget.setObjectName(_fromUtf8("downWidget"))
        self.gridLayout.addWidget(self.downWidget, 3, 1, 1, 1)

        self.SButton = QtGui.QPushButton(DiscoWindow)
        self.SButton.setGeometry(QtCore.QRect(0, 890, 21, 31))
        self.SButton.setObjectName(_fromUtf8("SButton"))

        self.retranslateUi(DiscoWindow)
        QtCore.QMetaObject.connectSlotsByName(DiscoWindow)

    def retranslateUi(self, DiscoWindow):
        DiscoWindow.setWindowTitle(_translate("DiscoWindow", "Form", None))
        self.SButton.setText(_translate("DiscoWindow", "S", None))

from CheckeredArrowWidget import CheckeredArrowWidget
