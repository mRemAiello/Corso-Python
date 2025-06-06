from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QListWidget, QHBoxLayout
import libreria
import aggiungi_libro_widget as addw
import rimuovi_libro_widget as delw
import cerca
import modifica
import os

class MainWidget(QWidget):
    main_layout = None
    list_widget = None
    button1 = None
    button2 = None
    button3 = None
    button4 = None
    libreria = None
    window_add = None
    window_del = None
    window_cerca = None
    window_modifica = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Libreria")
        self.resize(800, 600)
        self.libreria = libreria.Libreria()
        self.main_layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.main_layout.addWidget(self.list_widget)
        self.riempi_widget()
        self.bottom_layout = QHBoxLayout()
        self.button1 = QPushButton("Aggiungi Libro")
        self.button2 = QPushButton("Rimuovi Libro")
        self.button3 = QPushButton("Cerca")
        self.button4 = QPushButton("Modifica")
        self.button1.clicked.connect(self.mostra_aggiungi_libro)
        self.button2.clicked.connect(self.mostra_rimuovi_libro)
        self.button3.clicked.connect(self.mostra_cerca)
        self.button4.clicked.connect(self.mostra_modifica)
        self.bottom_layout.addWidget(self.button1)
        self.bottom_layout.addWidget(self.button2)
        self.bottom_layout.addWidget(self.button3)
        self.bottom_layout.addWidget(self.button4)
        self.main_layout.addLayout(self.bottom_layout)
        self.setLayout(self.main_layout)

    def riempi_widget(self):
        self.list_widget.clear()
        for libro in self.libreria.getLibri().values():
            self.list_widget.addItem(libro.__str__())
            print(libro)

    def mostra_aggiungi_libro(self):
        self.window_add = addw.Aggiungi_Libro(self, self.libreria)
        self.window_add.show()

    def mostra_rimuovi_libro(self):
        self.window_del = delw.Rimuovi_Libro(self, self.libreria)
        self.window_del.show()

    def mostra_cerca(self):
        self.window_cerca = cerca.Cerca(self, self.libreria)
        self.window_cerca.show()

    def mostra_modifica(self):
        self.window_modifica = modifica.ModificaWidget(self, self.libreria)
        self.window_modifica.show()

    def set_filename(self, file):
        self.libreria.percorso_file(file)
        self.riempi_widget()

    def load_filename(self, file):
        if os.path.exists(file):
            self.set_filename(file)
        else:
            print(f"Il file {file} non esiste")
