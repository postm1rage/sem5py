# -*- coding: utf-8 -*-

import sys
import numpy as np
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import ui_4


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_4.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnOpen.clicked.connect(self.open_image)
        self.ui.sliderAlpha.valueChanged.connect(self.update_opacity)
        
        self.original_image = None
    
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
        
        self.original_image = image.convertToFormat(QtGui.QImage.Format_ARGB32)
        self.update_opacity()
    
    def update_opacity(self):
        if self.original_image is None:
            return
        
        alpha = self.ui.sliderAlpha.value()
        self.ui.labelValue.setText("Прозрачность: {}%".format(alpha))
        
        image = self.original_image.convertToFormat(QtGui.QImage.Format_ARGB32)
        width = image.width()
        height = image.height()
        
        ptr = image.bits()
        ptr.setsize(image.byteCount())
        arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
        
        arr[:, :, 3] = (arr[:, :, 3].astype(np.uint16) * alpha // 100).astype(np.uint8)
        
        pixmap = QtGui.QPixmap.fromImage(image)
        
        label_size = self.ui.imageLabel.size()
        if label_size.width() > 10 and label_size.height() > 10:
            pixmap = pixmap.scaled(
                label_size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation
            )
        
        self.ui.imageLabel.setPixmap(pixmap)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()