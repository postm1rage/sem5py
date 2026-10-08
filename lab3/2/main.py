# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import ui_2


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_2.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnNew.clicked.connect(self.new_file)
        self.ui.btnOpen.clicked.connect(self.open_file)
        self.ui.btnSave.clicked.connect(self.save_file)
        
        self.current_path = None
    
    def new_file(self):
        self.ui.textEdit.clear()
        self.current_path = None
        self.setWindowTitle("Текстовый редактор — Новый файл")
    
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Открыть файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if not path:
            return
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.ui.textEdit.setPlainText(content)
            self.current_path = path
            self.setWindowTitle("Текстовый редактор — {}".format(path))
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", "Не удалось открыть файл:\n{}".format(e))
    
    def save_file(self):
        if self.current_path is None:
            path, _ = QFileDialog.getSaveFileName(
                self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)"
            )
            if not path:
                return
            self.current_path = path
        
        try:
            with open(self.current_path, 'w', encoding='utf-8') as f:
                f.write(self.ui.textEdit.toPlainText())
            
            self.setWindowTitle("Текстовый редактор — {}".format(self.current_path))
            QMessageBox.information(self, "Готово", "Файл сохранён!")
            
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить файл:\n{}".format(e))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()