import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout


def on_button_ok_click():
    print(text_input.text())


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Layout Avanzato')
window.resize(200, 100)

main_layout = QVBoxLayout()

# Etichetta
label = QLabel('Nome:')
main_layout.addWidget(label)

# Campo di testo
text_input = QLineEdit()
main_layout.addWidget(text_input)

#
button_ok = QPushButton('OK')
button_cancel = QPushButton('Annulla')
button_ok.clicked.connect(on_button_ok_click)
button_cancel.clicked.connect(on_button_ok_click)

#
button_layout = QHBoxLayout()
button_layout.addWidget(button_ok)
button_layout.addWidget(button_cancel)


# Assegno
main_layout.addLayout(button_layout)

window.setLayout(main_layout)

window.show()

sys.exit(app.exec())
