from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow
import mainwidget as mw
import inputdialog as inpd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Libreria")
        self.resize(800, 600)
        self.mainwidget = mw.MainWidget()
        menu = self.menuBar()
        self.setCentralWidget(self.mainwidget)
        file_menu = menu.addMenu('File')
        new_action = QAction('Nuovo', self)
        load_action = QAction('Carica', self)
        exit_action = QAction('Esci', self)
        file_menu.addAction(new_action)
        file_menu.addAction(load_action)
        file_menu.addAction(exit_action)
        new_action.triggered.connect(self.new_file)
        load_action.triggered.connect(self.load_file)
        exit_action.triggered.connect(self.exit_file)

    def new_file(self):
        dialog = inpd.InputDialog("Crea Nuovo File", "Scrivi il nome del file")
        if dialog.exec():
            self.mainwidget.set_filename(dialog.get_input() + ".txt")

    def load_file(self):
        dialog = inpd.InputDialog("Carica un File", "Scrivi il nome del file")
        if dialog.exec():
            self.mainwidget.load_filename(dialog.get_input() + ".txt")

    def exit_file(self):
        self.close()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()