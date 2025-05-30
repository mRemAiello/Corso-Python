import sys
from PySide6.QtWidgets import QApplication, QWidget

print(sys.argv)

app = QApplication(sys.argv)

# Creiamo una finestra
window = QWidget()
window.setWindowTitle('Finestra Vuota')
window.resize(900, 400)
window.show()

# Avvio dell'applicazione
sys.exit(app.exec())