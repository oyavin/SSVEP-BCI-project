__author__ = 'Omer'
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QWidget
from math import pi
from CheckeredArrowWidget import CheckeredArrowWidget
from frmDiscoWindow import Ui_DiscoWindow
from PyQt4.QtCore import QRectF, QPointF
from PyQt4.QtGui import QPixmap

# TODO add blinking effect using BlinkingWidget


class CheckeredArrowGrid(QWidget,Ui_DiscoWindow):
    def __init__(self, parent=None):
        super(CheckeredArrowGrid, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.opened = False
        self.grid = QtGui.QGridLayout()
        self.setLayout(self.grid)

        # self.downlabel = QtGui.QLabel()
        # self.downlabel.setMinimumSize(QtCore.QSize(170, 170))
        # self.gridLayout.addWidget(self.downlabel, 3, 1, 1, 1)
        # self.downlabel.lower()

        rads = [1.5 * pi, pi,  2 * pi, 0.5 * pi]
        positions = [(1, 2), (2, 1), (2, 3), (3, 2)]



        l=QtGui.QLabel()
        pixmap = QPixmap("checkered_arrow_3_right_op.png")
        l.setPixmap(pixmap)


        for position, rotation in zip(positions, rads):
            widget = CheckeredArrowWidget(None, rotation)
            self.grid.addWidget(widget, *position)




    '''
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
        '''
