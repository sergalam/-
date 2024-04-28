from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QHBoxLayout, QVBoxLayout, QComboBox, QLineEdit)
import requests 

'''Функции'''
def get_rate(target_currency):
    url = "https://www.cbr-xml-daily.ru/latest.js"
    response = requests.get(url)
    data = response.json()
    return data['rates'][target_currency]

'''Функция конвертации'''
def convert_currency():
    target_currency = need_currency_list.currentText()
    amount = float(select_value.text())
    exchange_rate = get_rate(target_currency)
    result = amount * exchange_rate
    result_label.setText(f"{result:.2f} {target_currency}")

''' Настройки приложения '''
app = QApplication([])
window = QWidget()
window.setWindowTitle('Заметки')
window.resize(900, 600)

''' Виджеты '''
Sap = QLabel('0.00')
Sap.setStyleSheet("font-size: 20px;")
Def = QComboBox()
Def.addItem('RUB') 
Kap = QComboBox()
Kap.addItems('EUR,KZT,USD') 
Rul = QLineEdit()
Rul.setPlaceholderText('Конвертор валют')
Tank = QPushButton('Конвентировать')

'''Размещение виджетов'''
notes_layout = QHBoxLayout()
col_1 = QVBoxLayout()
row_1 = QHBoxLayout()
row_1.addWidget(Sap, alignment=Qt.AlignCenter)
row_2 = QHBoxLayout()
row_2.addWidget(Def)
row_2.addWidget(Kap)
row_3 = QHBoxLayout()
row_3.addWidget(Rul, alignment=Qt.AlignCenter)
row_4 = QHBoxLayout()
row_4.addWidget(Tank, alignment=Qt.AlignCenter)
col_1.addLayout(row_1)
col_1.addLayout(row_2)
col_1.addLayout(row_3)
col_1.addLayout(row_4)

notes_layout.addLayout(col_1)
notes_layout.addLayout(notes_layout)
window.setLayout(notes_layout)


window.show()
app.exec_()