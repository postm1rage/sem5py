import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Калькулятор')
        self.setFixedSize(300, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 24px;")
        main_layout.addWidget(self.display)
        
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)
        
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)
        ]
        
        for text, row, col in buttons:
            button = QPushButton(text)
            button.setFixedSize(60, 60)
            button.setStyleSheet("font-size: 18px;")
            button.clicked.connect(self.button_click)
            grid_layout.addWidget(button, row, col)
        
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)
        
        self.current_input = ""
        self.first_number = None
        self.operation = None
        self.waiting_for_second = False
        
    def button_click(self):
        button = self.sender()
        text = button.text()
        
        if text == 'C':
            self.clear()
        elif text == '=':
            self.calculate()
        elif text in '0123456789.':
            self.input_digit(text)
        elif text in '+-*/':
            self.input_operation(text)
            
    def clear(self):
        self.current_input = ""
        self.first_number = None
        self.operation = None
        self.waiting_for_second = False
        self.display.setText("")
        
    def input_digit(self, digit):
        if self.waiting_for_second:
            self.current_input = ""
            self.waiting_for_second = False
            
        if digit == '.' and '.' in self.current_input:
            return
            
        self.current_input += digit
        self.display.setText(self.current_input)
        
    def input_operation(self, op):
        if self.current_input:
            if self.first_number is None:
                self.first_number = float(self.current_input)
                self.operation = op
                self.waiting_for_second = True
            else:
                self.calculate()
                self.first_number = float(self.current_input)
                self.operation = op
                self.waiting_for_second = True
                
    def calculate(self):
        if self.first_number is not None and self.operation is not None and self.current_input:
            try:
                second_number = float(self.current_input)
                
                if self.operation == '+':
                    result = self.first_number + second_number
                elif self.operation == '-':
                    result = self.first_number - second_number
                elif self.operation == '*':
                    result = self.first_number * second_number
                elif self.operation == '/':
                    if second_number == 0:
                        self.display.setText("Ошибка: деление на 0")
                        self.clear()
                        return
                    result = self.first_number / second_number
                
                if result == int(result):
                    result = int(result)
                    
                self.display.setText(str(result))
                self.current_input = str(result)
                self.first_number = None
                self.operation = None
                self.waiting_for_second = False
                
            except ValueError:
                self.display.setText("Ошибка")
                self.clear()

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()