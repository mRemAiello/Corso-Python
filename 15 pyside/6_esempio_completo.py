import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Impostazioni della finestra principale
        self.setWindowTitle('QMainWindow con Menu e Toolbar')
        self.resize(600, 400)

        # Aggiungiamo un widget centrale
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # Creiamo la barra dei menu
        menu = self.menuBar()
        file_menu = menu.addMenu('File')
        edit_menu = menu.addMenu("Edit")
        view_menu = menu.addMenu("View")

        # Creiamo un'azione per il menu
        save_action = QAction('Salva', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        #
        undo_action = QAction("Undo", self)
        redo_action = QAction("Redo", self)
        edit_menu.addAction(undo_action)
        edit_menu.addAction(redo_action)

        # Creiamo una toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addAction(save_action)

    def save_file(self):
        print("Salvataggio del file...")
        # Logica per il salvataggio del file


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
