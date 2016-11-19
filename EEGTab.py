from PyQt4 import QtGui, QtCore
from EEGPlot import EEGPlot

from frmEEGTab import Ui_EEGTab


class MyModel(QtGui.QStandardItemModel):
    def __init__(self, *args):
        QtGui.QStandardItemModel.__init__(self, *args)

    def flags(self, index):
        flags = QtCore.Qt.ItemFlags()

        if index.isValid():
            flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled
        else:
            flags = QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsDropEnabled | QtCore.Qt.ItemIsEnabled

        flags = flags | QtCore.Qt.ItemIsUserCheckable
        return flags


class EEGTab(QtGui.QWidget, Ui_EEGTab):
    def __init__(self, *args):
        QtGui.QWidget.__init__(self, *args)
        self.setupUi(self)

        self.model = MyModel()
        self.plotsToShow = []

        QtCore.QObject.connect(self.reorganizeButton, QtCore.SIGNAL("clicked()"), self.updateElectrodes)
        QtCore.QObject.connect(self.model, QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"),
                               lambda: self.reorganizeButton.setStyleSheet('QPushButton {color: red}'))

    def initUI(self, electrode_names):
        self.electrode_names = electrode_names

        for electrode in self.electrode_names:
            item = QtGui.QStandardItem(electrode)

            item.setCheckState(QtCore.Qt.Checked)
            item.setCheckable(True)
            self.model.appendRow(item)

        self.ElectrodeList.setModel(self.model)

        self.updateElectrodes()

    def updateElectrodes(self):

        self.plotsToShow = []

        for i in range(self.model.rowCount()):
            if (self.model.item(i).checkState() == QtCore.Qt.Checked):
                electrode = self.model.item(i).text()
                self.plotsToShow.append(self.electrode_names.index(electrode))

        for i in range(self.verticalLayout_EEG.count()):
            p = self.verticalLayout_EEG.takeAt(0)
            self.plots.pop(0)
            w = p.widget()
            w.setParent(None)
            w.deleteLater()

        self.plots = []
        for i in self.plotsToShow:
            plot = EEGPlot(i, self.electrode_names[i])
            self.plots.append(plot)
            self.verticalLayout_EEG.addWidget(plot)

        self.reorganizeButton.setStyleSheet('QPushButton {color: black}')

    def updatePlots(self, t, signal):
        for index, item in enumerate(self.plotsToShow):
            self.plots[index].update(t, signal[item, :])

