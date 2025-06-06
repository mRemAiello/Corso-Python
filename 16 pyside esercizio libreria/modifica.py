from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
import inputdialog as inpd

class ModificaWidget(QWidget):
    main_layout = None
    label1 = None
    label2 = None
    label3 = None
    label4 = None
    label5 = None
    text_input_1 = None
    text_input_2 = None
    text_input_3 = None
    text_input_4 = None
    button = None
    libreria = None

    def __init__(self, main_window, libreria):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Modifica Libro")
        self.resize(400, 300)
        self.libreria = libreria
        self.main_layout = QVBoxLayout()
        self.label1 = QLabel("Cerca ISBN:")
        self.text_input_1 = QLineEdit()
        self.label2 = QLabel("Nuovo Autore Libro:")
        self.text_input_2 = QLineEdit()
        self.label3 = QLabel("Nuovo Titolo Libro (opzionale):")
        self.text_input_3 = QLineEdit()
        self.label4 = QLabel("Anno di pubblicazione (opzionale):")
        self.text_input_4 = QLineEdit()
        self.label5 = QLabel("")
        self.button = QPushButton("Modifica")
        self.button.clicked.connect(self.modifica)
        self.main_layout.addWidget(self.label1)
        self.main_layout.addWidget(self.text_input_1)
        self.main_layout.addWidget(self.label2)
        self.main_layout.addWidget(self.text_input_2)
        self.main_layout.addWidget(self.label3)
        self.main_layout.addWidget(self.text_input_3)
        self.main_layout.addWidget(self.label4)
        self.main_layout.addWidget(self.text_input_4)
        self.main_layout.addWidget(self.label4)
        self.main_layout.addWidget(self.label5)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)

    def modifica(self):
        dialog = inpd.Confirm("Conferma", "Vuoi modificare il libro?")
        if dialog.exec():
            if dialog.risultato:
                isbn = self.text_input_1.text()
                autore = self.text_input_2.text()
                titolo = self.text_input_3.text()
                anno = self.text_input_4.text()
                risultato = self.libreria.modifica(isbn=isbn, autore=autore, titolo=titolo, anno=anno)
                self.label5.setText(risultato)
                self.main_window.riempi_widget()
