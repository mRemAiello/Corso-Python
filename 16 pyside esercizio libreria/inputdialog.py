from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class InputDialog(QDialog):
    def __init__(self, titolo, label):
        super().__init__()

        self.setWindowTitle(titolo)
        layout = QVBoxLayout()

        self.label = QLabel(label)
        layout.addWidget(self.label)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.button = QPushButton('OK')
        self.button.clicked.connect(self.accept)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_input(self):
        return self.text_input.text()

class Confirm(QDialog):
    risultato = None

    def __init__(self, titolo, label):
        super().__init__()
        self.setWindowTitle(titolo)
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.label = QLabel(label)
        layout.addWidget(self.label)
        self.button1 = QPushButton('Sì')
        self.button2 = QPushButton('No')
        self.button1.clicked.connect(self.conferma)
        self.button2.clicked.connect(self.nega)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def conferma(self):
        self.risultato = True
        self.accept()

    def nega(self):
        self.risultato = False
        self.reject()

    def get_risultato(self):
        return self.risultato