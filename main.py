import rsa
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QSpacerItem, \
    QSizePolicy, QPushButton, QScrollArea, QGridLayout
from stegano import lsb
from PyQt6 import *
import sys

'''
(pubkey, privkey) = rsa.newkeys(512)
message = input()
message = message.encode()

# шифруем
crypto = rsa.encrypt(message, pubkey)
print(crypto)
print("\n")
# расшифровываем
message = rsa.decrypt(crypto, privkey)
print(message.decode())
a = open("save_cheto.txt", "w", encoding="UTF-8")
a.write(str(crypto)[2:-1])
a.close()
pub_key_data = pubkey.save_pkcs1().decode('utf-8')
secret_img = lsb.hide("stonks.png", pub_key_data)
secret_img.save("result_with_key.png")
'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("месенджер")
        self.setGeometry(100, 100, 700, 700)

        self.label_input = QLabel("")

        self.label_output = QLabel("сообщения от собеседника")

        self.input = QLineEdit()

        self.button = QPushButton("отправить")
        self.button.setFixedSize(100, 50)
        self.button.clicked.connect(self.click_button)

        self.area_input = QScrollArea()
        self.area_input.setWidget(self.label_input)
        self.area_input.setWidgetResizable(True)

        self.area_output = QScrollArea()
        self.area_output.setWidget(self.label_output)
        self.area_output.setWidgetResizable(True)

        layout = QGridLayout()
        #layout.addStretch(1)

        #layout.addWidget(self.label)
        layout.addWidget(self.area_input, 0, 0)
        layout.addWidget(self.area_output, 0, 1)
        layout.addWidget(self.input, 1, 0)
        layout.addWidget(self.button, 1, 1)


        container = QWidget()
        container.setLayout(layout)


        #self.area.show()


        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)
    def click_button(self):
        a = self.input.text()
        self.label_input.setText(a)
        print(a)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()