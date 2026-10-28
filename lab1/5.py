import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QCheckBox, QSpinBox, QPushButton, QPlainTextEdit, QLabel
from PyQt5.QtCore import Qt

class RestaurantOrder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Заказ в ресторане')
        self.setFixedSize(700, 600)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        label = QLabel("Выберите блюда:")
        label.setStyleSheet("font-size: 14px; font-weight: bold;")
        main_layout.addWidget(label)
        
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)
        
        self.dishes = []
        
        menu = [
            ('Пицца Маргарита', 450),
            ('Паста Карбонара', 380),
            ('Салат Цезарь', 320),
            ('Стейк Рибай', 650),
            ('Суп Томатный', 250),
            ('Десерт Тирамису', 280),
            ('Чай', 120),
            ('Кофе', 150)
        ]
        
        for i, (name, price) in enumerate(menu):
            checkbox = QCheckBox(name)
            checkbox.stateChanged.connect(self.update_receipt)
            grid_layout.addWidget(checkbox, i, 0)
            
            price_label = QLabel(f"{price} ₽")
            grid_layout.addWidget(price_label, i, 1)
            
            spinbox = QSpinBox()
            spinbox.setRange(0, 99)
            spinbox.setValue(1)
            spinbox.setEnabled(False)
            spinbox.valueChanged.connect(self.update_receipt)
            grid_layout.addWidget(spinbox, i, 2)
            
            checkbox.stateChanged.connect(lambda state, sb=spinbox, cb=checkbox: self.toggle_spinbox(state, sb, cb))
            
            self.dishes.append({
                'name': name,
                'price': price,
                'checkbox': checkbox,
                'spinbox': spinbox
            })
        
        self.receipt_text = QPlainTextEdit()
        self.receipt_text.setReadOnly(True)
        self.receipt_text.setPlaceholderText("Чек будет сформирован здесь...")
        self.receipt_text.setFixedHeight(250)
        main_layout.addWidget(self.receipt_text)
        
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
    def toggle_spinbox(self, state, spinbox, checkbox):
        if state == Qt.Checked:
            spinbox.setEnabled(True)
            spinbox.setValue(1)
        else:
            spinbox.setEnabled(False)
            spinbox.setValue(0)
        self.update_receipt()
        
    def update_receipt(self):
        receipt = []
        receipt.append("=" * 50)
        receipt.append("                 ЧЕК")
        receipt.append("=" * 50)
        receipt.append("")
        
        total_sum = 0
        has_items = False
        
        for dish in self.dishes:
            if dish['checkbox'].isChecked():
                quantity = dish['spinbox'].value()
                if quantity > 0:
                    has_items = True
                    total_price = dish['price'] * quantity
                    total_sum += total_price
                    receipt.append(f"{dish['name']}")
                    receipt.append(f"  {quantity} шт. x {dish['price']} ₽ = {total_price} ₽")
                    receipt.append("")
        
        if not has_items:
            receipt.append("Заказ пуст")
            receipt.append("")
        else:
            receipt.append("-" * 50)
            receipt.append(f"ИТОГО: {total_sum} ₽")
            receipt.append("")
            receipt.append("Спасибо за заказ!")
        
        receipt.append("=" * 50)
        
        self.receipt_text.setPlainText("\n".join(receipt))

def main():
    app = QApplication(sys.argv)
    window = RestaurantOrder()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()