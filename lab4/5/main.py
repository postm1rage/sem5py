import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_5 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        pixmap = QtGui.QPixmap(80, 50)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtGui.QColor('#38536c'), 2))
        painter.setBrush(QtGui.QColor('#82d6f5'))
        painter.drawEllipse(27, 5, 27, 29)
        painter.setBrush(QtGui.QColor('#647fbd'))
        painter.drawEllipse(6, 22, 68, 23)
        painter.setBrush(QtGui.QColor('#b6ecff'))
        for x in (17, 33, 49, 65):
            painter.drawEllipse(x, 31, 6, 6)
        painter.end()
        self.ui.ufoLabel.setPixmap(pixmap)
        self.step = 20

    def keyPressEvent(self, event):
        directions = {QtCore.Qt.Key_Left: (-1, 0), QtCore.Qt.Key_Right: (1, 0), QtCore.Qt.Key_Up: (0, -1), QtCore.Qt.Key_Down: (0, 1)}
        if event.key() in directions:
            dx, dy = directions[event.key()]
            label = self.ui.ufoLabel
            maximum_x = max(0, self.ui.centralwidget.width() - label.width())
            maximum_y = max(0, self.ui.centralwidget.height() - label.height())
            x = label.x() + dx * self.step
            y = label.y() + dy * self.step
            if x > maximum_x:
                x = 0
            elif x < 0:
                x = maximum_x
            if y > maximum_y:
                y = 0
            elif y < 0:
                y = maximum_y
            label.move(x, y)
        else:
            super().keyPressEvent(event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
