import random
import sys

from PyQt4 import Qt, QtGui, QtCore
import PyQt4.Qwt5 as Qwt
from numpy import zeros

from frmEEGPlot import Ui_EEG_Plot


class EEGPlot(QtGui.QWidget, Ui_EEG_Plot):

    def __init__(self, channel, title, *args):
        Qwt.QwtPlot.__init__(self, *args)
        self.setupUi(self)
        
        self.setMinimumHeight(100)
        
        self.title = title
        self.channel = channel
        
        self.label.setText(title)
        
        self.setupPlot()

    # __init__()
    
    def setupPlot(self):
        self.qwtPlot.setCanvasBackground(Qt.Qt.white)
        self.alignScales()

        # self.qwtPlot.enableAxis(Qwt.QwtPlot.xBottom, False)
        # self.qwtPlot.enableAxis(Qwt.QwtPlot.yLeft, False) TODO Check why this was here at all
        
        self.qwtPlot.CurveSignal = Qwt.QwtPlotCurve("EEG Signal")
        self.qwtPlot.CurveSignal.attach(self.qwtPlot)
        self.qwtPlot.CurveSignal.setPen(Qt.QPen(Qt.Qt.blue))

        mY = Qwt.QwtPlotMarker()
        mY.setLabelAlignment(Qt.Qt.AlignRight | Qt.Qt.AlignTop)
        mY.setLineStyle(Qwt.QwtPlotMarker.HLine)
        mY.setYValue(0.0)
        mY.attach(self.qwtPlot)

        # grid
        self.qwtPlot.grid = Qwt.QwtPlotGrid()
        self.qwtPlot.grid.enableY(False)
        self.qwtPlot.grid.enableX(True)
        self.qwtPlot.grid.enableXMin(True)
        self.qwtPlot.grid.setMajPen(Qt.QPen(Qt.Qt.gray, 0, Qt.Qt.SolidLine))
        self.qwtPlot.grid.setMinPen(Qt.QPen(Qt.Qt.gray, 0, Qt.Qt.DashLine))
        self.qwtPlot.grid.attach(self.qwtPlot)
    
        self.qwtPlot.startTimer(50)
        self.qwtPlot.phase = 0.0

    # setUpPlot()
    
    def alignScales(self):
        self.qwtPlot.canvas().setFrameStyle(Qt.QFrame.Box | Qt.QFrame.Plain)
        self.qwtPlot.canvas().setLineWidth(1)
        for i in range(Qwt.QwtPlot.axisCnt):
            scaleWidget = self.qwtPlot.axisWidget(i)
            if scaleWidget:
                scaleWidget.setMargin(0)
            scaleDraw = self.qwtPlot.axisScaleDraw(i)
            if scaleDraw:
                scaleDraw.enableComponent(
                    Qwt.QwtAbstractScaleDraw.Backbone, False)

    # alignScales()
    
    def update(self, x, y):

        self.qwtPlot.CurveSignal.setData(x, y)

        self.qwtPlot.replot()

    # update()
