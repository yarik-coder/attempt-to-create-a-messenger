import rsa
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QScrollArea, QGridLayout
from PyQt6 import QtCore  # Импортируем QtCore для доступа к Qt.AlignmentFlag
import sys


class MainWindow(QMainWindow):
    def __init__(self):  # Исправлено на __init__
        super().__init__()

        self.setWindowTitle("месенджер")
        self.setGeometry(100, 100, 700, 700)

        self.input = QLineEdit()
        self.button = QPushButton("отправить")
        self.button.setFixedSize(100, 50)
        self.button.clicked.connect(self.click_button)

        # Создаем QScrollArea для ввода и вывода
        self.area_input = QScrollArea()
        self.area_input.setWidgetResizable(True)

        self.area_output = QScrollArea()
        self.area_output.setWidgetResizable(True)

        # Создаем виджет для ввода сообщений
        self.input_widget = QWidget()
        self.input_layout = QVBoxLayout(self.input_widget)
        self.input_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)  # Выравниваем по верху

        # Устанавливаем виджет для ввода в QScrollArea
        self.area_input.setWidget(self.input_widget)

        # Создаем виджет для вывода сообщений
        self.output_widget = QWidget()
        self.output_layout = QVBoxLayout(self.output_widget)
        self.output_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)  # Выравниваем по верху

        # Устанавливаем виджет для вывода в QScrollArea
        self.area_output.setWidget(self.output_widget)

        layout = QGridLayout()
        layout.addWidget(self.area_input, 0, 0)  # Ввод сообщений слева
        layout.addWidget(self.area_output, 0, 1)  # Вывод сообщений справа
        layout.addWidget(self.input, 1, 0)
        layout.addWidget(self.button, 1, 1)

        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    def click_button(self):
        message = self.input.text()
        if message:
            # Создаем новый QLabel для сообщения и добавляем его в layout input_area
            message_label = QLabel(message)
            message_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # Выравниваем сообщение влево
            self.input_layout.addWidget(message_label)  # Добавляем сообщение в input_area
            self.input.clear()  # Очищаем поле ввода


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
