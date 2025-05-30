from PySide6.QtWidgets import QApplication, QWidget


# Creazione di una classe per la finestra principale
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finestra Base")
        self.resize(800, 600)


# Inizializzazione dell'applicazione
app = QApplication([])  # Creazione dell'istanza dell'applicazione
window = MainWindow()   # Creazione della finestra
window.show()           # Visualizzazione della finestra
app.exec()              # Esecuzione del loop dell'applicazione

# while True:
# controllo_input
# aggiorno i componenti
# aggiorno l'ui