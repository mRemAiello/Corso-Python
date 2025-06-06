import sys
from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class MySignalEmitter(QObject):
    my_signal = Signal(str)


def on_custom_signal(message):
    print(f"Segnale ricevuto: {message}")
    label.setText(f"Ricevuto: {message}")


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Segnali e Slot')

layout = QVBoxLayout()

label = QLabel('Nessun segnale ricevuto')
layout.addWidget(label)

button = QPushButton('Invia Segnale')
layout.addWidget(button)

# Creiamo un'emettitore di segnali
emitter = MySignalEmitter()
emitter.my_signal.connect(on_custom_signal)

# Collegamento del segnale al click del pulsante
button.clicked.connect(lambda: emitter.my_signal.emit("Segnale Inviato"))

# Prima
# Bottone -> clicked -> modifica / aggiungi

# Dopo
# Bottone -> clicked -> emitter.my_signal.emit("Segnale Inviato")
# Segnale -> Classe 1 -> on_custom_signal(message) -> print + label.setText
# Segnale -> Classe 2 -> on_custom_signal(message) -> altra operazione

# Esempio con Ecommerce
# Ordine -> Pagamento -> Nuovo_ordine database -> Mostra la schermata -> manda_email

# Così con eventi
# Ordine -> Emesso Segnale ordine
# Database -> salva_sul_database
# Pagamento -> elaboro
# Schermata -> mostra_schermata
# Email -> mando_email

window.setLayout(layout)
window.show()

sys.exit(app.exec())
