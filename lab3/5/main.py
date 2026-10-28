# -*- coding: utf-8 -*-

import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QInputDialog

import ui_5


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_5.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnGenerate.clicked.connect(self.generate_flag)
    
    def generate_flag(self):
        count, ok = QInputDialog.getInt(
            self, "Количество цветов",
            "Введите количество цветов (2–10):",
            3, 2, 10, 1
        )
        if not ok:
            return
        
        width = 400
        height = 300
        image = QtGui.QImage(width, height, QtGui.QImage.Format_RGB32)
        
        painter = QtGui.QPainter(image)
        
        stripe_height = height / count
        
        for i in range(count):
            color = QtGui.QColor(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            painter.fillRect(
                QtCore.QRectF(0, i * stripe_height, width, stripe_height),
                color
            )
        
        painter.end()
        
        pixmap = QtGui.QPixmap.fromImage(image)
        self.ui.flagLabel.setPixmap(pixmap)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()