# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import ui_3


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_3.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnOpen.clicked.connect(self.open_image)
        self.ui.btnLeft.clicked.connect(self.rotate_left)
        self.ui.btnRight.clicked.connect(self.rotate_right)
        self.ui.btnAll.clicked.connect(lambda: self.set_channel('all'))
        self.ui.btnR.clicked.connect(lambda: self.set_channel('r'))
        self.ui.btnG.clicked.connect(lambda: self.set_channel('g'))
        self.ui.btnB.clicked.connect(lambda: self.set_channel('b'))
        
        self.original_image = None
        self.channel = 'all'
        
        QtCore.QTimer.singleShot(100, self.open_image)
    
    def open_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выберите изображение", "",
            "Изображения (*.png *.jpg *.jpeg *.bmp)"
        )
        if not path:
            return
        
        image = QtGui.QImage(path)
        
        if image.isNull():
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить изображение")
            return
        
        if image.width() != image.height():
            QMessageBox.warning(
                self, "Внимание",
                "Изображение должно быть квадратным!\n"
                "Размер: {}x{}".format(image.width(), image.height())
            )
            return
        
        self.original_image = image
        self.channel = 'all'
        self.update_display()
    
    def rotate_left(self):
        if self.original_image is None:
            return
        transform = QtGui.QTransform().rotate(-90)
        self.original_image = self.original_image.transformed(transform)
        self.update_display()
    
    def rotate_right(self):
        if self.original_image is None:
            return
        transform = QtGui.QTransform().rotate(90)
        self.original_image = self.original_image.transformed(transform)
        self.update_display()
    
    def set_channel(self, channel):
        if self.original_image is None:
            return
        self.channel = channel
        self.update_display()
    
    def update_display(self):
        if self.original_image is None:
            self.ui.imageLabel.setText("Изображение не загружено")
            return
        
        image = self.original_image.copy()
        
        if self.channel != 'all':
            image = self.filter_channel(image, self.channel)
        
        pixmap = QtGui.QPixmap.fromImage(image)
        
        label_size = self.ui.imageLabel.size()
        if label_size.width() > 10 and label_size.height() > 10:
            pixmap = pixmap.scaled(
                label_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
            )
        
        self.ui.imageLabel.setPixmap(pixmap)
    
    def filter_channel(self, image, channel):
        image = image.convertToFormat(QtGui.QImage.Format_RGB32)
        result = QtGui.QImage(image.width(), image.height(), QtGui.QImage.Format_RGB32)
        
        for y in range(image.height()):
            for x in range(image.width()):
                color = image.pixelColor(x, y)
                r = color.red()
                g = color.green()
                b = color.blue()
                
                if channel == 'r':
                    new_color = QtGui.QColor(r, 0, 0)
                elif channel == 'g':
                    new_color = QtGui.QColor(0, g, 0)
                else:
                    new_color = QtGui.QColor(0, 0, b)
                
                result.setPixelColor(x, y, new_color)
        
        return result


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()