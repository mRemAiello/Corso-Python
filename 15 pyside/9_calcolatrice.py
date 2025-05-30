import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class CustomDialog(QDialog):

    text_input = None
    text_input_2 = None
    risultatoLabel = None

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dialogo Personalizzato')

        layout = QVBoxLayout()

        self.label = QLabel('Inserisci il primo numero:')
        layout.addWidget(self.label)

        self.text_input = QLineEdit()
        layout.addWidget(self.text_input)

        self.text_input_2 = QLineEdit()
        layout.addWidget(self.text_input_2)

        self.risultatoLabel = QLabel("")
        layout.addWidget(self.risultatoLabel)

        self.button = QPushButton('Ok')
        self.button.clicked.connect(self.mostra_risultato)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_input(self):
        return self.text_input.text()

    def mostra_risultato(self):
        print("Lancio funzione")
        numero_1 = int(self.text_input.text())
        numero_2 = int(self.text_input_2.text())
        self.risultatoLabel.setText(str(numero_1 + numero_2))
        return


#
app = QApplication(sys.argv)

dialog = CustomDialog()
if dialog.exec():
    print(f"Nome inserito: {dialog.get_input()}")

sys.exit(app.exec())