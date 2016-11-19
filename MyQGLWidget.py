import math
import numpy
from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtOpenGL import *


class MyQGLWidget(QGLWidget):
    def __init__(self, parent):
        '''
        Init routine
        '''

        QGLWidget.__init__(self, parent)

        self.timer = QtCore.QTimer()

        self.speed = 20;

        self.spin = 0.0
        self.doSpin = False
        self.cubeX = 0.0
        self.doXTranslate = False
        self.cubeY = 0.0
        self.doYTranslate = False
        self.cubeZ = 0.0
        self.doZTranslate = False

        self.texcube = 0
        self.texworld = 1

        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.moveCube)

    def loadTexture(self, filename, texid=0):

        img = QtGui.QImage(filename)
        img = QGLWidget.convertToGLFormat(img)

        glBindTexture(GL_TEXTURE_2D, texid)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width(), img.height(),
                     0, GL_RGBA, GL_UNSIGNED_BYTE, img.bits().asstring(img.numBytes()))

        glBindTexture(GL_TEXTURE_2D, texid)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    def drawSkybox(self):
        # Enable/Disable features
        # glPushAttrib(GL_ENABLE_BIT);
        glEnable(GL_TEXTURE_2D)
        glDisable(GL_DEPTH_TEST)
        #        glDisable(GL_LIGHTING);
        #        glDisable(GL_BLEND);

        # Just in case we set all vertices to white.
        glColor4f(1, 1, 1, 1)

        # Render the front quad
        glBindTexture(GL_TEXTURE_2D, self.texworld)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glTexCoord2f(1, 1)
        glVertex3f(-0.5, 0.5, -0.5)
        glTexCoord2f(0, 1)
        glVertex3f(0.5, 0.5, -0.5)
        glEnd()

        # Render the left quad
        glBindTexture(GL_TEXTURE_2D, self.texworld)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(0.5, -0.5, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glTexCoord2f(1, 1)
        glVertex3f(0.5, 0.5, -0.5)
        glTexCoord2f(0, 1)
        glVertex3f(0.5, 0.5, 0.5)
        glEnd()

        # Render the back quad
        glBindTexture(GL_TEXTURE_2D, self.texworld)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.5, -0.5, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(0.5, -0.5, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(0.5, 0.5, 0.5)
        glTexCoord2f(0, 1)
        glVertex3f(-0.5, 0.5, 0.5)

        glEnd()

        # Render the right quad
        glBindTexture(GL_TEXTURE_2D, self.texworld)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glTexCoord2f(1, 0)
        glVertex3f(-0.5, -0.5, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(-0.5, 0.5, 0.5)
        glTexCoord2f(0, 1)
        glVertex3f(-0.5, 0.5, -0.5)
        glEnd()

        # Render the top quad
        glBindTexture(GL_TEXTURE_2D, self.texworld)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 1)
        glVertex3f(-0.5, 0.5, -0.5)
        glTexCoord2f(0, 0)
        glVertex3f(-0.5, 0.5, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(0.5, 0.5, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(0.5, 0.5, -0.5)
        glEnd()

        # Render the bottom quad
        glBindTexture(GL_TEXTURE_2D, self.texworld)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0)
        glVertex3f(-0.5, -0.5, -0.5)
        glTexCoord2f(0, 1)
        glVertex3f(-0.5, -0.5, 0.5)
        glTexCoord2f(1, 1)
        glVertex3f(0.5, -0.5, 0.5)
        glTexCoord2f(1, 0)
        glVertex3f(0.5, -0.5, -0.5)
        glEnd()

        glEnable(GL_DEPTH_TEST)

    def drawWorld(self):

        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texworld)

        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, 1)  # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, 1)  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, 1)  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, 1)  # Top Left Of The Texture and Quad
        glEnd()

        glDisable(GL_TEXTURE_2D)

    def drawCube(self):
        '''
        Draws a textured cube
        '''
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texcube)

        glBegin(GL_QUADS)
        # Front Face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)  # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0)
        glVertex3f(0.5, -0.5, 0.5)  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-0.5, 0.5, 0.5)  # Top Left Of The Texture and Quad
        # Back Face
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-0.5, 0.5, -0.5)  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0)
        glVertex3f(0.5, 0.5, -0.5)  # Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)  # Bottom Left Of The Texture and Quad
        # Top Face
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-0.5, 0.5, -0.5)  # Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.5, 0.5, 0.5)  # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0)
        glVertex3f(0.5, 0.5, 0.5)  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0)
        glVertex3f(0.5, 0.5, -0.5)  # Top Right Of The Texture and Quad
        # Bottom Face
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-0.5, -0.5, -0.5)  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0)
        glVertex3f(0.5, -0.5, -0.5)  # Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0)
        glVertex3f(0.5, -0.5, 0.5)  # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)  # Bottom Right Of The Texture and Quad
        # Right face
        glTexCoord2f(1.0, 0.0)
        glVertex3f(0.5, -0.5, -0.5)  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0)
        glVertex3f(0.5, 0.5, -0.5)  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0)
        glVertex3f(0.5, 0.5, 0.5)  # Top Left Of The Texture and Quad
        glTexCoord2f(0.0, 0.0)
        glVertex3f(0.5, -0.5, 0.5)  # Bottom Left Of The Texture and Quad
        # Left Face
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-0.5, -0.5, -0.5)  # Bottom Left Of The Texture and Quad
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-0.5, -0.5, 0.5)  # Bottom Right Of The Texture and Quad
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-0.5, 0.5, 0.5)  # Top Right Of The Texture and Quad
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-0.5, 0.5, -0.5)  # Top Left Of The Texture and Quad
        glEnd()

        glDisable(GL_TEXTURE_2D)

    @pyqtSlot('int')
    def updateSpeed(self, speed):
        self.speed = speed

    @pyqtSlot('bool')
    def spin(self, value):
        self.doSpin = value

    @pyqtSlot('bool')
    def moveX(self, value):
        self.doXTranslate = value

    @pyqtSlot('bool')
    def moveY(self, value):
        self.doYTranslate = value

    @pyqtSlot('bool')
    def moveZ(self, value):
        self.doZTranslate = value

    def moveCube(self):
        '''
        Update spin angle
        '''

        if self.doSpin:
            self.spin = (self.spin + 3) % 360

        if self.doXTranslate:
            self.cubeX = min(self.cubeX + 0.2, 3)

        if self.doYTranslate:
            self.cubeY = min(self.cubeY + 0.2, 3)

        if self.doZTranslate:
            self.cubeZ = min(self.cubeZ + 0.2, 3)

        self.updateGL()

    def paintGL(self):
        '''
        Drawing routine
        '''

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        s = 2.0
        glScale(s, s, s)
        self.drawSkybox()
        glScale(1 / s, 1 / s, 1 / s)

        glScale(0.3, 0.3, 0.3)
        # self.drawWorld()

        # Move cube

        gravity = -9.81 * self.timer.interval() * self.timer.interval() * 0.000004

        if self.cubeX and abs(self.cubeX) > abs(gravity):
            self.cubeX += cmp(self.cubeX, 0) * gravity
        if self.cubeY and abs(self.cubeY) > abs(gravity):
            self.cubeY += cmp(self.cubeY, 0) * gravity
        if self.cubeZ and abs(self.cubeZ) > abs(gravity):
            self.cubeZ += cmp(self.cubeZ, 0) * gravity

        glTranslatef(self.cubeX, self.cubeY, self.cubeZ)

        glRotatef(20 + self.spin, 0.0, 1.0, 0.0)
        glRotatef(20, 1.0, 1.0, 1.0)

        self.drawCube()

    def resizeGL(self, w, h):
        '''
        Resize the GL window 
        '''

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0, w / h, 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 3, -10, 0, 0, 0, 0, 0, 1)

    def initializeGL(self):
        '''
        Initialize GL
        '''

        self.qglClearColor(QtGui.QColor(0, 0, 150))

        glEnable(GL_CULL_FACE)

        glEnable(GL_TEXTURE_2D)
        self.loadTexture('brain.jpg', self.texcube)
        self.loadTexture('clouds.jpg', self.texworld)
        glShadeModel(GL_SMOOTH)

        glEnable(GL_DEPTH_TEST)

        self.timer.start(50)
