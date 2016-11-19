from PyQt4 import QtGui, QtCore, QtSvg
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QPixmap
from PyQt4.QtCore import QRectF, QPointF
import Connector


class CheckeredArrowWidget(QtGui.QWidget):


    def __init__(self, parent=None, rads=0):

        QtGui.QWidget.__init__(self, parent)

        self.scene = QtGui.QGraphicsScene()
        #self.setScene(self.scene)
        self.type = 0
        self.rads = rads
        self.setFixedSize(170, 170)
        self.frequency = 10
        self.timer = QtCore.QTimer()
        self.pixmap=None
        self.pixmap_black=None
        self.pixmap_green=None
        self.point = QPointF(0.0, 0.0)
        self.status = 0
        self.setStyleSheet("background-color: rgba(0,0,0,0)")


        '''
        self.p=self.palette()
        self.p.setColor(self.backgroundRole(),QtCore.Qt.red)
        self.setPalette(self.p)
        '''
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.changeColor)

        if self.rads is not None:
            self.draw_arrow()

    def changeColor(self):
        if self.type == 0:
            self.pixmap = None
        else:
            if self.frequency == Connector.result:
                self.pixmap = self.pixmap_green
            else:
                self.pixmap = self.pixmap_black
        self.type = 1 - self.type
        self.update()



    def paintEvent(self, event):

        if self.pixmap:

            #self.status = 1 - self.status
            #if self.status:
            self.pixmap = self.pixmap_black
            #else :
                #self.pixmap=self.pixmap_green

            #pixmap = QPixmap("checkered_arrow_3_op.svg")
            #point = QPointF(0.0, 0.0)
            painter = QtGui.QPainter()
            painter.begin(self)
            #painter.setBrush(QtCore.Qt.black)
            painter.drawPixmap(self.point, self.pixmap)

            painter.end()


    @pyqtSlot()
    def flicker(self):
        self.timer.start(500.0 / ((self.frequency)))  # before 1000.0

    def stop(self):
        self.timer.stop()
        self.type = 0
        self.changeColor()

    @pyqtSlot()
    def draw_arrow(self):


        self.scene.setBackgroundBrush(QtGui.QBrush(QtCore.Qt.white, QtCore.Qt.SolidPattern))

        arrow = QtSvg.QGraphicsSvgItem("checkered_arrow_3.svg")
        trans = QtGui.QTransform()
        trans.rotateRadians(self.rads)
        trans.translate(-arrow.boundingRect().width()/2, -arrow.boundingRect().height()/2)
        arrow.setTransform(trans)
        self.scene.addItem(arrow)


