from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QListWidget, QLineEdit

class Cerca(QWidget):
    main_layout = None
    label1 = None
    label2 = None
    list_widget = None
    text_input_1 = None
    text_input_2 = None
    button1 = None
    button2 = None
    libreria = None

    def __init__(self, main_window, libreria):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Cerca Autore/Titolo")
        self.resize(400, 300)
        self.libreria = libreria
        self.main_layout = QVBoxLayout()
        self.label1 = QLabel("Autore Libro:")
        self.label2 = QLabel("Titolo Libro:")
        self.list_widget = QListWidget()
        self.bottom_layout = QHBoxLayout()
        self.button1 = QPushButton("Cerca Autore")
        self.button2 = QPushButton("Cerca Titolo")
        self.button1.clicked.connect(self.cerca_autore)
        self.button2.clicked.connect(self.cerca_titolo)
        self.text_input_1 = QLineEdit()
        self.text_input_2 = QLineEdit()
        self.main_layout.addWidget(self.label1)
        self.main_layout.addWidget(self.text_input_1)
        self.main_layout.addWidget(self.label2)
        self.main_layout.addWidget(self.text_input_2)
        self.main_layout.addWidget(self.list_widget)
        self.bottom_layout.addWidget(self.button1)
        self.bottom_layout.addWidget(self.button2)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)

    def cerca_autore(self):
        self.list_widget.clear()
        autore = self.text_input_1.text()
        risult_autore = self.libreria.trova_libro_autore(autore)
        for element in risult_autore:
            self.list_widget.addItem(element.__str__())

    def cerca_titolo(self):
        self.list_widget.clear()
        titolo = self.text_input_2.text()
        risult_libro = self.libreria.trova_libro_titolo(titolo)
        for element in risult_libro:
            self.list_widget.addItem(element.__str__())