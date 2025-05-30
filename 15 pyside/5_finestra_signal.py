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

# Bottone -> clicked -> emitter.my_signal.emit("Segnale Inviato") -> on_custom_signal(message) -> print + label.setText

window.setLayout(layout)
window.show()

sys.exit(app.exec())
