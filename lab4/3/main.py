import random
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_3 import Ui_MainWindow


class Canvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shapes = []
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def add_shape(self, shape, point):
        self.shapes.append((shape, QtCore.QPoint(point), random.randint(25, 90), QtGui.QColor.fromHsv(random.randint(0, 359), 190, 235)))
        self.update()

    def mousePressEvent(self, event):
        self.setFocus()
        if event.button() == QtCore.Qt.LeftButton:
            self.add_shape('circle', event.pos())
        elif event.button() == QtCore.Qt.RightButton:
            self.add_shape('square', event.pos())

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.add_shape('triangle', self.mapFromGlobal(QtGui.QCursor.pos()))
        else:
            super().keyPressEvent(event)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        for shape, point, size, color in self.shapes:
            painter.setBrush(color)
            painter.setPen(QtGui.QPen(QtCore.Qt.black, 1))
            x, y = point.x(), point.y()
            if shape == 'circle':
                painter.drawEllipse(QtCore.QRect(x - size // 2, y - size // 2, size, size))
            elif shape == 'square':
                painter.drawRect(QtCore.QRect(x - size // 2, y - size // 2, size, size))
            else:
                vertices = [QtCore.QPoint(x, y - size // 2), QtCore.QPoint(x - size // 2, y + size // 2), QtCore.QPoint(x + size // 2, y + size // 2)]
                painter.drawPolygon(QtGui.QPolygon(vertices))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)
        self.canvas.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
