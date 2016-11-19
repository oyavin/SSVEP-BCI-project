import sys
from Connector import Connector

from PyQt4 import QtCore
from PyQt4.QtGui import QMainWindow, QApplication, QHBoxLayout, QLabel, QIcon
import pyglet
from frmMain import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, mode='online'):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon('app_icon.png'))

        QtCore.QObject.connect(self.speedSlider, QtCore.SIGNAL("valueChanged (int)"), self.MyCube,
                               QtCore.SLOT("updateSpeed(int)"))
        QtCore.QObject.connect(self.pushButton_Spin, QtCore.SIGNAL("clicked(bool)"), self.MyCube,
                               QtCore.SLOT("spin(bool)"))
        QtCore.QObject.connect(self.pushButton_X, QtCore.SIGNAL("clicked(bool)"), self.MyCube,
                               QtCore.SLOT("moveX(bool)"))
        QtCore.QObject.connect(self.pushButton_Y, QtCore.SIGNAL("clicked(bool)"), self.MyCube,
                               QtCore.SLOT("moveY(bool)"))
        QtCore.QObject.connect(self.pushButton_Z, QtCore.SIGNAL("clicked(bool)"), self.MyCube,
                               QtCore.SLOT("moveZ(bool)"))

        self.myConnector = Connector(self, mode=mode)



        self.timer = QtCore.QTimer()
        QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.myConnector.update)

        self.timer.start(50)  # cycle time in ms (50)

    def close(self):
        self.myConnector.close()


if __name__ == '__main__':
    App = QApplication(sys.argv)

    if "offline" in str(sys.argv):
        mode = 'offline'
    else:
        mode = 'online'
    my_window = MyWindow(mode=mode)

    my_window.show()

    App.connect(App, QtCore.SIGNAL("aboutToQuit()"), my_window.close)
    sys.exit(App.exec_())
