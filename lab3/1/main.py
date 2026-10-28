# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import ui_1


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_1.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btnLoad.clicked.connect(self.load_file)
        self.ui.btnSave.clicked.connect(self.save_file)
        
        self.numbers = []
    
    def load_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выберите текстовый файл", "", "Текстовые файлы (*.txt)"
        )
        if not path:
            return
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            parts = content.split()
            
            if not parts:
                raise ValueError("Файл пуст")
            
            self.numbers = []
            for p in parts:
                try:
                    self.numbers.append(int(p))
                except ValueError:
                    raise ValueError("Некорректное значение: '{}'".format(p))
            
            self.update_labels()
            
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка формата", str(e))
            self.numbers = []
            self.reset_labels()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", "Не удалось открыть файл:\n{}".format(e))
            self.numbers = []
            self.reset_labels()
    
    def update_labels(self):
        if not self.numbers:
            self.reset_labels()
            return
        
        maximum = max(self.numbers)
        minimum = min(self.numbers)
        average = sum(self.numbers) / len(self.numbers)
        
        self.ui.labelMax.setText("Максимум: {}".format(maximum))
        self.ui.labelMin.setText("Минимум: {}".format(minimum))
        self.ui.labelAvg.setText("Среднее: {:.2f}".format(average))
    
    def reset_labels(self):
        self.ui.labelMax.setText("Максимум: —")
        self.ui.labelMin.setText("Минимум: —")
        self.ui.labelAvg.setText("Среднее: —")
    
    def save_file(self):
        if not self.numbers:
            QMessageBox.warning(self, "Внимание", "Сначала загрузите данные из файла!")
            return
        
        path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить результат", "", "Текстовые файлы (*.txt)"
        )
        if not path:
            return
        
        maximum = max(self.numbers)
        minimum = min(self.numbers)
        average = sum(self.numbers) / len(self.numbers)
        
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write("Максимум: {}\n".format(maximum))
                f.write("Минимум: {}\n".format(minimum))
                f.write("Среднее: {:.2f}\n".format(average))
            
            QMessageBox.information(self, "Готово", "Результат сохранён!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить файл:\n{}".format(e))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()