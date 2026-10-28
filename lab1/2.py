import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Калькулятор выражений')
        self.setFixedSize(500, 200)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        label1 = QLabel("Введите выражение:")
        main_layout.addWidget(label1)
        
        self.input_expr = QLineEdit()
        self.input_expr.setFixedHeight(35)
        main_layout.addWidget(self.input_expr)
        
        self.calc_button = QPushButton("Вычислить")
        self.calc_button.setFixedHeight(35)
        self.calc_button.clicked.connect(self.calculate)
        main_layout.addWidget(self.calc_button)
        
        label2 = QLabel("Результат:")
        main_layout.addWidget(label2)
        
        self.result = QLineEdit()
        self.result.setFixedHeight(35)
        self.result.setReadOnly(True)
        main_layout.addWidget(self.result)
        
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)
        
    def calculate(self):
        expr = self.input_expr.text()
        if expr:
            result = eval(expr)
            self.result.setText(str(result))

def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()