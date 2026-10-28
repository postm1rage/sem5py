import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class WordTosser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Перекидыватель слов')
        self.setFixedSize(500, 200)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        h_layout = QHBoxLayout()
        main_layout.addLayout(h_layout)
        
        self.input1 = QLineEdit()
        self.input1.setFixedHeight(40)
        h_layout.addWidget(self.input1)
        
        self.button = QPushButton("→")
        self.button.setFixedSize(60, 40)
        self.button.setFont(QFont("Arial", 16, QFont.Bold))
        self.button.clicked.connect(self.toss_word)
        h_layout.addWidget(self.button)
        
        self.input2 = QLineEdit()
        self.input2.setFixedHeight(40)
        self.input2.setReadOnly(True)
        h_layout.addWidget(self.input2)
        
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        self.text_in_first = True
        
    def toss_word(self):
        if self.text_in_first:
            text = self.input1.text()
            if text:
                self.input2.setText(text)
                self.input1.clear()
                self.button.setText("←")
                self.text_in_first = False
        else:
            text = self.input2.text()
            if text:
                self.input1.setText(text)
                self.input2.clear()
                self.button.setText("→")
                self.text_in_first = True

def main():
    app = QApplication(sys.argv)
    window = WordTosser()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()