import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_4 import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.setMouseTracking(True)
        self.ui.runButton.setMouseTracking(True)
        self.ui.centralwidget.installEventFilter(self)
        self.ui.runButton.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() in (QtCore.QEvent.MouseMove, QtCore.QEvent.Enter):
            point = self.ui.centralwidget.mapFromGlobal(QtGui.QCursor.pos())
            button = self.ui.runButton
            rect = button.geometry()
            close_x = max(rect.left(), min(point.x(), rect.right()))
            close_y = max(rect.top(), min(point.y(), rect.bottom()))
            if abs(point.x() - close_x) < 70 and abs(point.y() - close_y) < 70:
                self.run_away(point)
        return super().eventFilter(obj, event)

    def run_away(self, cursor):
        button = self.ui.runButton
        area = self.ui.centralwidget.rect()
        max_x = max(0, area.width() - button.width())
        max_y = max(0, area.height() - button.height())
        choices = [(0, 0), (max_x, 0), (0, max_y), (max_x, max_y), (max_x // 2, 0), (max_x // 2, max_y)]
        x, y = max(choices, key=lambda p: (p[0] + button.width() / 2 - cursor.x()) ** 2 + (p[1] + button.height() / 2 - cursor.y()) ** 2)
        button.move(x, y)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, 'ui') and hasattr(self.ui, 'runButton'):
            button = self.ui.runButton
            button.move(min(button.x(), max(0, self.ui.centralwidget.width() - button.width())), min(button.y(), max(0, self.ui.centralwidget.height() - button.height())))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
