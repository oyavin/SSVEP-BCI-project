from PyQt4 import Qt, QtGui, QtCore,QtSvg
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtCore import QRectF, QPointF
from PyQt4.QtGui import QPixmap, QPicture
import Connector
from PIL import Image
from numpy import array
import numpy as np
import math




class BlinkingWidget(QtGui.QWidget):
    def __init__(self, rads=0,  parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.checkerboard = array([[0, 255, 255, 255],
                              [255, 0, 255, 255],
                              [0, 255, 0, 255],
                              [255, 0, 255, 0],
                              [0, 255, 0, 255],
                              [255, 0, 255, 255],
                              [0, 255, 255, 255]])

        im = Image.fromarray(self.checkerboard)
        im.save('arrow.png')


        self.scene = QtGui.QGraphicsScene()
        self.head = QtSvg.QGraphicsSvgItem("checkered_arrow_3_op.svg")
        trans = QtGui.QTransform()
        trans.translate(-self.head.boundingRect().width()/2, -self.head.boundingRect().height()/2)
        self.head.setTransform(trans)


        self.type = 0
        self.size = 170
        self.color = None
        self.frequency = 10
        self.rads = rads
        self.timer = QtCore.QTimer()
        self.pixmap=None
        self.pixmap_black=None
        self.pixmap_green=None
        self.point = QPointF(0.0, 0.0)

        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.changeColor)


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
        '''
        if self.pixmap:
            x = (self.width() - self.size) / 2
            y = (self.height() - self.size) / 2


            target = QRectF(10.0, 20.0, 80.0, 60.0)
            source = QRectF(0.0, 0.0, 70.0, 40.0)
            #pixmap = QPixmap("checkered_arrow_3.svg")
            point = QPointF(90.0, 80.0)
            #picture = QPicture()
            #picture.load("image.pic")

            #self.scene.addItem(self.head)
            painter = QtGui.QPainter()
            painter.begin(self)
            #painter.setBrush(self.color)
            painter.drawPixmap(self.point, self.pixmap )
            #painter.drawEllipse(x, y, self.size, self.size)
            #r.drawPicture(0,0, picture)
            painter.end()

            '''




    @pyqtSlot()
    def flicker(self):

        self.timer.start(500.0 / self.frequency)  # before 1000.0

    def stop(self):
        self.timer.stop()
        self.type = 0
        self.changeColor()



