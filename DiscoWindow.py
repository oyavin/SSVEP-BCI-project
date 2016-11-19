__author__ = 'Omer'
from PyQt4 import QtGui
from frmDiscoWindow import Ui_DiscoWindow


class DiscoWindow(QtGui.QWidget, Ui_DiscoWindow,):

    def __init__(self, *args):
        QtGui.QWidget.__init__(self, *args)
        self.setupUi(self)
        super(DiscoWindow, self).__init__()
        # self.parent = parent
        self.opened = False