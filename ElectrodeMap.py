from PyQt4 import Qt, QtGui, QtCore, QtSvg


class ElectrodeMap(QtGui.QGraphicsView):
    def __init__(self, parent):
        QtGui.QGraphicsView.__init__(self, parent)

        self.renderer = QtSvg.QSvgRenderer('electrodes.svg')
        # self.pixmap = QtGui.QPixmap(900,900)
        #        self.pixmap.fill(QtCore.Qt.transparent)
        self.scene = QtGui.QGraphicsScene()
        self.setScene(self.scene)

    def initUI(self, electrode_names, electrode_quality):
        self.electrode_names = electrode_names[:]
        self.electrode_quality = electrode_quality[:]

        self.drawMap()

    def update(self, electrode_quality):
        if self.electrode_quality != electrode_quality:
            self.electrode_quality = electrode_quality[:]
            self.drawMap()

    def drawMap(self):
        self.scene.clear()

        font = QtGui.QFont('Times', 8, QtGui.QFont.Bold);

        # svg = QtSvg.QGraphicsSvgItem('electrodes.svg')
        #
        #        painter = QtGui.QPainter(self.pixmap)
        #
        #        QtSvg.QGraphicsSvgItem.paint(svg, painter, QtGui.QStyleOptionGraphicsItem())
        #
        #        for item in svg.childItems():
        #            print item.elementId()
        #            QtSvg.QGraphicsSvgItem.paint(item, painter, QtGui.QStyleOptionGraphicsItem())

        # Background
        for i in range(8):
            line = QtSvg.QGraphicsSvgItem()
            line.setSharedRenderer(self.renderer)
            line.setElementId('line' + str(i))
            br = self.renderer.boundsOnElement('line' + str(i))
            qtr = QtGui.QTransform()
            qtr.translate(br.x(), br.y())

            line.setTransform(qtr)

            #QtSvg.QGraphicsSvgItem.paint(line, painter, QtGui.QStyleOptionGraphicsItem()) 
            self.scene.addItem(line)
            #self.renderer.render(painter,line.boundingRect()); 

        # Electrodes
        for electrode, quality in zip(self.electrode_names, self.electrode_quality):
            elec_circle = QtSvg.QGraphicsSvgItem()
            elec_circle.setSharedRenderer(self.renderer)
            elec_circle.setElementId(electrode + '_circle')
            br = self.renderer.boundsOnElement(electrode + '_circle')
            #qtr = QtGui.QTransform()
            #qtr.translate(br.x(), br.y())
            #elec_circle.setTransform(qtr)

            elec_bg = QtGui.QGraphicsEllipseItem(br)
            elec_bg.setBrush(QtGui.QBrush(QtGui.QColor(255, 255, 255)))

            elec_color = QtGui.QGraphicsEllipseItem(br)
            elec_color.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 2))

            if quality == 0:
                color = QtGui.QColor(255, 0, 0, 128)
            elif quality == 1:
                color = QtGui.QColor(255, 255, 0, 128)
            elif quality == 2:
                color = QtGui.QColor(0, 255, 0, 128)
            else:
                color = QtGui.QColor(255, 153, 0, 128)

            elec_color.setBrush(QtGui.QBrush(color))

            elec_text = QtGui.QGraphicsTextItem()
            elec_text.setFont(font)
            elec_text.setPlainText(electrode)
            x = br.x() + br.width() / 2 - elec_text.boundingRect().width() / 2
            y = br.y() + br.height() / 2 - elec_text.boundingRect().height() / 2
            elec_text.setPos(x, y)

            self.scene.addItem(elec_bg)
            self.scene.addItem(elec_color)
            #self.scene.addItem(elec_circle)
            self.scene.addItem(elec_text)
