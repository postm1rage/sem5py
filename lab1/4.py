import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class MorseCode(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Азбука Морзе')
        self.setFixedSize(500, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Код Морзе появится здесь...")
        self.input_field.setFixedHeight(40)
        self.input_field.setReadOnly(True)
        main_layout.addWidget(self.input_field)
        
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)
        
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'
        }
        
        row = 0
        col = 0
        for letter, code in morse_dict.items():
            button = QPushButton(f"{letter}\n{code}")
            button.setFixedSize(60, 60)
            button.clicked.connect(lambda checked, l=letter, c=code: self.add_morse(l, c))
            grid_layout.addWidget(button, row, col)
            
            col += 1
            if col > 5:
                col = 0
                row += 1
        
        clear_button = QPushButton("Очистить")
        clear_button.setFixedHeight(40)
        clear_button.clicked.connect(self.clear_field)
        main_layout.addWidget(clear_button)
        
    def add_morse(self, letter, code):
        current_text = self.input_field.text()
        if current_text:
            self.input_field.setText(f"{current_text} {code}")
        else:
            self.input_field.setText(code)
    
    def clear_field(self):
        self.input_field.clear()

def main():
    app = QApplication(sys.argv)
    window = MorseCode()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()