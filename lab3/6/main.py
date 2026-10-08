# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QColorDialog

import ui_6


class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color = QtGui.QColor(255, 220, 0)
        self.scale = 100
    
    def set_color(self, color):
        self.color = color
        self.update()
    
    def set_scale(self, scale):
        self.scale = scale
        self.update()
    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        w = self.width()
        h = self.height()
        size = min(w, h) * 0.8 * self.scale / 100
        
        cx = w / 2
        cy = h / 2
        radius = size / 2
        
        painter.setBrush(QtGui.QBrush(self.color))
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 2))
        painter.drawEllipse(QtCore.QPointF(cx, cy), radius, radius)
        
        eye_radius = radius * 0.12
        eye_offset_x = radius * 0.35
        eye_offset_y = radius * 0.3
        
        painter.setBrush(QtGui.QBrush(QtGui.QColor(0, 0, 0)))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawEllipse(
            QtCore.QPointF(cx - eye_offset_x, cy - eye_offset_y),
            eye_radius, eye_radius
        )
        painter.drawEllipse(
            QtCore.QPointF(cx + eye_offset_x, cy - eye_offset_y),
            eye_radius, eye_radius
        )
        
        mouth_rect = QtCore.QRectF(
            cx - radius * 0.5,
            cy - radius * 0.05,
            radius * 1.0,
            radius * 0.7
        )
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 3))
        painter.setBrush(QtCore.Qt.NoBrush)
        painter.drawArc(mouth_rect, 180 * 16, 180 * 16)
        
        painter.end()


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_6.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.canvas = Canvas()
        layout = QtWidgets.QVBoxLayout(self.ui.canvasWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        
        self.ui.btnColor.clicked.connect(self.choose_color)
        self.ui.sliderScale.valueChanged.connect(self.change_scale)
    
    def choose_color(self):
        color = QColorDialog.getColor(self.canvas.color, self, "Выберите цвет смайлика")
        if color.isValid():
            self.canvas.set_color(color)
    
    def change_scale(self):
        scale = self.ui.sliderScale.value()
        self.ui.labelScale.setText("Масштаб: {}%".format(scale))
        self.canvas.set_scale(scale)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()