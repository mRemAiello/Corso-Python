import sys
import time
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow


class WorkerThread(QThread):
    update_signal = Signal(str)

    def run(self):
        for i in range(1, 6):
            time.sleep(1)  # Simuliamo un'operazione lunga
            self.update_signal.emit(str(i))

        time.sleep(1)
        self.exit(0)

    def exit(self, retcode=0):
        self.update_signal.emit("Processo completato")


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Threading con QThread')
        self.resize(800, 600)

        #
        self.layout = QVBoxLayout()

        self.label = QLabel('In attesa...')
        self.layout.addWidget(self.label)

        self.button = QPushButton('Avvia Operazione')
        self.button.clicked.connect(self.start_thread)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.thread = WorkerThread()
        self.thread.update_signal.connect(self.update_label)

    def start_thread(self):
        self.label.setText('Operazione in corso...')
        self.thread.start()

    def update_label(self, value):
        self.label.setText(f'Progresso: {value}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
