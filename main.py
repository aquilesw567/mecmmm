# Full IDEInterface implementation with corrected PyQt6 imports

from PyQt6.QtWidgets import QApplication, QMainWindow, QAction, QStatusBar
from PyQt6.QtGui import QIcon

class IDEInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IDE Interface')
        self.setGeometry(100, 100, 800, 600)

        # Creating a status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Creating a menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('File')

        # Adding actions to the file menu
        open_action = QAction(QIcon('open.png'), 'Open', self)
        file_menu.addAction(open_action)

        save_action = QAction(QIcon('save.png'), 'Save', self)
        file_menu.addAction(save_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        self.show()