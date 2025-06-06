from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
import inputdialog as inpd

class Rimuovi_Libro(QWidget):
    main_layout = None
    label1 = None
    label2 = None
    text_input = None
    button = None
    libreria = None

    def __init__(self, main_window, libreria):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Rimuovi Libro")
        self.resize(400, 300)
        self.libreria = libreria
        self.main_layout = QVBoxLayout()
        self.label1 = QLabel("Inserisci ISBN Libro:")
        self.label2 = QLabel("")
        self.button = QPushButton("Rimuovi")
        self.button.clicked.connect(self.clic_del_libro)
        self.text_input = QLineEdit()
        self.main_layout.addWidget(self.label1)
        self.main_layout.addWidget(self.text_input)
        self.main_layout.addWidget(self.label2)
        self.main_layout.addWidget(self.button)
        self.setLayout(self.main_layout)

    def clic_del_libro(self):
        dialog = inpd.Confirm("Conferma", "Vuoi rimuovere il libro?")
        if dialog.exec():
            if dialog.risultato:
                libroisbn = self.text_input.text()
                if self.libreria.trova_libro(libroisbn):
                    self.libreria.rimuovi_libro(libroisbn)
                    self.main_window.riempi_widget()
                    self.close()
                else:
                    self.label2.setText("Il libro non è presente")
