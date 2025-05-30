import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QLabel, QComboBox, QTableView
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem


# Classe base per la gestione dei dati
class Dati:
    def __init__(self):
        self.df = None

    def carica_dati(self, file_path):
        self.df = pd.read_csv(file_path)


# Sottoclasse che estende Dati e implementa metodi di analisi
class AnalisiDati(Dati):
    def calcola_media(self, colonna):
        return self.df[colonna].mean()

    def calcola_massimo(self, colonna):
        return self.df[colonna].max()

    def calcola_minimo(self, colonna):
        return self.df[colonna].min()


# Interfaccia grafica con PySide6
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.analisi = AnalisiDati()

        self.setWindowTitle("Analisi Dati CSV")
        self.setGeometry(100, 100, 800, 600)

        # Layout principale
        layout = QVBoxLayout()

        # Bottoni e widget
        self.carica_button = QPushButton("Carica CSV")
        self.carica_button.clicked.connect(self.carica_csv)
        
        self.combo_colonne = QComboBox()
        self.combo_colonne.currentIndexChanged.connect(self.aggiorna_analisi)
        self.combo_colonne.setEnabled(False)

        self.tabella_view = QTableView()

        self.label_media = QLabel("Media: ")
        self.label_massimo = QLabel("Massimo: ")
        self.label_minimo = QLabel("Minimo: ")

        # Aggiunta widget al layout
        layout.addWidget(self.carica_button)
        layout.addWidget(self.combo_colonne)
        layout.addWidget(self.tabella_view)
        layout.addWidget(self.label_media)
        layout.addWidget(self.label_massimo)
        layout.addWidget(self.label_minimo)

        # Impostazione layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Carica file CSV e popola la tabella
    def carica_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Carica File CSV", "", "CSV Files (*.csv)")
        if file_path:
            self.analisi.carica_dati(file_path)
            self.popola_tabella()
            self.combo_colonne.addItems(self.analisi.df.columns)
            self.combo_colonne.setEnabled(True)

    # Popola la tabella con i dati del CSV
    def popola_tabella(self):
        model = QStandardItemModel()
        colonne = list(self.analisi.df.columns)

        # Imposta intestazioni delle colonne
        model.setHorizontalHeaderLabels(colonne)

        # Popola i dati
        for row in self.analisi.df.itertuples():
            items = [QStandardItem(str(getattr(row, col))) for col in colonne]
            model.appendRow(items)

        self.tabella_view.setModel(model)

    # Aggiorna i valori di media, massimo e minimo in base alla colonna selezionata
    def aggiorna_analisi(self):
        colonna = self.combo_colonne.currentText()
        if colonna:
            media = self.analisi.calcola_media(colonna)
            massimo = self.analisi.calcola_massimo(colonna)
            minimo = self.analisi.calcola_minimo(colonna)

            self.label_media.setText(f"Media: {media}")
            self.label_massimo.setText(f"Massimo: {massimo}")
            self.label_minimo.setText(f"Minimo: {minimo}")


# Avvio dell'applicazione
app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())