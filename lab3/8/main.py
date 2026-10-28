# -*- coding: utf-8 -*-

import sys
import math
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox

import ui_8


class LSystemCanvas(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.axiom = "F"
        self.rules = {}
        self.angle = 72
        self.step = 1
        self.line_length = 10
    
    def set_system(self, axiom, rules, angle, step):
        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.step = step
        self.update()
    
    def generate_string(self, step):
        current = self.axiom
        for _ in range(step):
            result = ""
            for ch in current:
                if ch in self.rules:
                    result += self.rules[ch]
                else:
                    result += ch
            current = result
        return current
    
    def paintEvent(self, event):
        if not self.axiom:
            return
        
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        w = self.width()
        h = self.height()
        
        string = self.generate_string(self.step)
        
        line_length = self.line_length * (0.7 ** self.step)
        
        x = w / 2
        y = h * 0.8
        angle = -90
        
        stack = []
        
        painter.setPen(QtGui.QPen(QtGui.QColor(0, 100, 0), 1.5))
        
        for ch in string:
            if ch == 'F' or ch == 'G':
                nx = x + line_length * math.cos(math.radians(angle))
                ny = y + line_length * math.sin(math.radians(angle))
                painter.drawLine(QtCore.QPointF(x, y), QtCore.QPointF(nx, ny))
                x, y = nx, ny
            elif ch == 'f':
                x += line_length * math.cos(math.radians(angle))
                y += line_length * math.sin(math.radians(angle))
            elif ch == '+':
                angle += self.angle
            elif ch == '-':
                angle -= self.angle
            elif ch == '[':
                stack.append((x, y, angle))
            elif ch == ']':
                if stack:
                    x, y, angle = stack.pop()
        
        painter.end()


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui_8.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.canvas = LSystemCanvas()
        layout = QtWidgets.QVBoxLayout(self.ui.canvasWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        
        self.ui.sliderStep.valueChanged.connect(self.change_step)
        
        self.loaded = False
        
        QtCore.QTimer.singleShot(100, self.open_file)
    
    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Выберите файл с L-системой", "",
            "Текстовые файлы (*.txt);;Все файлы (*)"
        )
        if not path:
            return
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f.readlines()]
            
            lines = [line for line in lines if line]
            
            if len(lines) < 3:
                raise ValueError("Файл должен содержать минимум 3 строки")
            
            title = lines[0]
            angles_count = int(lines[1])
            axiom = lines[2]
            
            if angles_count <= 0:
                raise ValueError("Количество углов должно быть больше 0")
            
            angle = 360 / angles_count
            
            rules = {}
            for line in lines[3:]:
                if '=' in line:
                    parts = line.split('=', 1)
                    rules[parts[0].strip()] = parts[1].strip()
                else:
                    parts = line.split(None, 1)
                    if len(parts) == 2:
                        rules[parts[0].strip()] = parts[1].strip()
            
            self.canvas.set_system(axiom, rules, angle, 1)
            
            self.ui.labelTitle.setText("Название: {}".format(title))
            self.ui.sliderStep.setValue(1)
            
            self.loaded = True
            
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка формата", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", "Не удалось открыть файл:\n{}".format(e))
    
    def change_step(self, value):
        if not self.loaded:
            return
        self.ui.labelStep.setText("Шаг: {}".format(value))
        self.canvas.step = value
        self.canvas.update()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()