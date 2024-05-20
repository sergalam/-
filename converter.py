from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox
    )
import requests 

# Функция для получения курса обмена валюты
def get_rate(target_currency):
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

# Функция конвертации
def convert_currency():
    target_currency = need_currency_list.currentText()
    amount = float(select_value.text())
    exchange_rate = get_rate(target_currency)
    result = amount * exchange_rate
    result_label.setText(f"{result:.2f} {target_currency}")


# screen
app = QApplication([])
screen = QWidget()
screen.setWindowTitle('Конвертер валют')
screen.setFixedSize(400, 200)

# Widgets
result_label = QLabel('0.00 RUB')
result_label.setAlignment(Qt.AlignCenter)
result_label.setStyleSheet("font-size: 20px;")

convert_btn = QPushButton('Конвертировать')

select_value = QLineEdit()
select_value.setFixedWidth(150)

select_currency_list = QComboBox()
select_currency_list.addItem('RUB')
select_currency_list.setStyleSheet("font-size: 16px;")

need_currency_list = QComboBox()
need_currency_list.addItems(['USD', 'EUR', 'KZT', 'BRL', 'CNY', 'RSD', 'KRW', "JPY"])
need_currency_list.setStyleSheet("font-size: 16px;")


# Position Widgets
main_layout = QVBoxLayout()

row1 = QHBoxLayout()
row1.addWidget(select_currency_list)
row1.addWidget(need_currency_list)


main_layout.addWidget(result_label)
main_layout.addLayout(row1)
main_layout.addWidget(select_value, alignment=Qt.AlignCenter)
main_layout.addWidget(convert_btn, alignment=Qt.AlignCenter)

screen.setLayout(main_layout)

# Подключение кнопки к функции конвертации
convert_btn.clicked.connect(convert_currency)

screen.show()
app.exec_()