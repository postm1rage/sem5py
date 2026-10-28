import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel, QLineEdit, QPushButton, QTextEdit

class CheckBoxDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Управление виджетами через чекбоксы')
        self.setFixedSize(500, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        self.widgets = []
        self.checkboxes = []
        
        # QLabel
        widget1_layout = QHBoxLayout()
        label = QLabel("Текстовый виджет QLabel")
        label.setFixedHeight(50)
        label.setStyleSheet("background-color: lightblue; border: 1px solid black;")
        widget1_layout.addWidget(label)
        
        checkbox1 = QCheckBox("Показать")
        checkbox1.setChecked(True)
        checkbox1.stateChanged.connect(self.toggle_widget)
        widget1_layout.addWidget(checkbox1)
        main_layout.addLayout(widget1_layout)
        
        self.widgets.append(label)
        self.checkboxes.append(checkbox1)
        
        # QLineEdit
        widget2_layout = QHBoxLayout()
        line_edit = QLineEdit("Поле для ввода текста")
        line_edit.setFixedHeight(50)
        line_edit.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        widget2_layout.addWidget(line_edit)
        
        checkbox2 = QCheckBox("Показать")
        checkbox2.setChecked(True)
        checkbox2.stateChanged.connect(self.toggle_widget)
        widget2_layout.addWidget(checkbox2)
        main_layout.addLayout(widget2_layout)
        
        self.widgets.append(line_edit)
        self.checkboxes.append(checkbox2)
        
        # QPushButton
        widget3_layout = QHBoxLayout()
        button = QPushButton("Кнопка")
        button.setFixedHeight(50)
        button.setStyleSheet("background-color: lightcoral; border: 1px solid black;")
        widget3_layout.addWidget(button)
        
        checkbox3 = QCheckBox("Показать")
        checkbox3.setChecked(True)
        checkbox3.stateChanged.connect(self.toggle_widget)
        widget3_layout.addWidget(checkbox3)
        main_layout.addLayout(widget3_layout)
        
        self.widgets.append(button)
        self.checkboxes.append(checkbox3)
        
        # Виджет 4: QTextEdit
        widget4_layout = QHBoxLayout()
        text_edit = QTextEdit()
        text_edit.setPlainText("Многострочный текст\nВторая строка")
        text_edit.setFixedHeight(80)
        text_edit.setStyleSheet("background-color: lightyellow; border: 1px solid black;")
        widget4_layout.addWidget(text_edit)
        
        checkbox4 = QCheckBox("Показать")
        checkbox4.setChecked(True)
        checkbox4.stateChanged.connect(self.toggle_widget)
        widget4_layout.addWidget(checkbox4)
        main_layout.addLayout(widget4_layout)
        
        self.widgets.append(text_edit)
        self.checkboxes.append(checkbox4)
        
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
    def toggle_widget(self):
        for widget, checkbox in zip(self.widgets, self.checkboxes):
            if checkbox.isChecked():
                widget.show()
            else:
                widget.hide()

def main():
    app = QApplication(sys.argv)
    window = CheckBoxDemo()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()