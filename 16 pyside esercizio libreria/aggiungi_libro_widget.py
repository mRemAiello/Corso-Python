from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
import libro
import inputdialog as inpd

class Aggiungi_Libro(QWidget):
    main_layout = None
    label1 = None
    label2 = None
    label3 = None
    label4 = None
    text_input_1 = None
    text_input_2 = None
    text_input_3 = None
    text_input_4 = None
    button = None
    libreria = None

    def __init__(self, main_window, libreria):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Aggiungi Libro")
        self.resize(400, 300)
        self.libreria = libreria
        self.main_layout = QVBoxLayout()
        self.label1 = QLabel("ISBN:")
        self.label2 = QLabel("Titolo Libro:")
        self.label3 = QLabel("Autore Libro:")
        self.label4 = QLabel("Anno di pubblicazione:")
        self.button = QPushButton("Aggiungi")
        self.button.clicked.connect(self.clic_add_libro)
        self.text_input_1 = QLineEdit()
        self.text_input_2 = QLineEdit()
        self.text_input_3 = QLineEdit()
        self.text_input_4 = QLineEdit()
        self.main_layout.addWidget(self.label1)
        self.main_layout.addWidget(self.text_input_1)
        self.main_layout.addWidget(self.label2)
        self.main_layout.addWidget(self.text_input_2)
        self.main_layout.addWidget(self.label3)
        self.main_layout.addWidget(self.text_input_3)
        self.main_layout.addWidget(self.label4)
        self.main_layout.addWidget(self.text_input_4)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)

    def clic_add_libro(self):
        dialog = inpd.Confirm("Conferma", "Vuoi aggiungere il libro?")
        if dialog.exec():
            if dialog.risultato:
                librotext = libro.Libro(isbn=self.text_input_1.text(), titolo=self.text_input_2.text(), autore=self.text_input_3.text(), anno=self.text_input_4.text())
                self.libreria.aggiungi_libro(librotext)
                self.main_window.riempi_widget()
                self.close()