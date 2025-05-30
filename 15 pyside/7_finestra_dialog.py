import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dialogo Personalizzato')

        layout = QVBoxLayout()

        self.label = QLabel('Inserisci il tuo nome:')
        layout.addWidget(self.label)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.button = QPushButton('Ok')
        self.button.clicked.connect(self.accept)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_input(self):
        return self.text_input.text()


app = QApplication(sys.argv)

dialog = CustomDialog()
if dialog.exec():
    print(f"Nome inserito: {dialog.get_input()}")

sys.exit(app.exec())
