import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def on_button_click():
    print("Pulsante cliccato!")


app = QApplication(sys.argv)

# Creo finestra
window = QWidget()
window.setWindowTitle('Finestra con Pulsante')

# Creo un Layout Box
layout = QVBoxLayout()

# Creiamo un pulsante
button = QPushButton('Cliccami')
# button -> clicked -> on_button_click()
button.clicked.connect(on_button_click)

# Creiamo un secondo pulsante
button2 = QPushButton("Secondo")
button2.clicked.connect(on_button_click)

#
layout.addWidget(button)
layout.addWidget(button2)

#
window.setLayout(layout)
window.resize(800, 400)
window.show()

# Avvia l'applicazione e gestisci l'uscita
sys.exit(app.exec())