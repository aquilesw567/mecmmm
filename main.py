import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QVBoxLayout, QWidget, QTabWidget, QMenuBar, QAction, QTreeView, QLineEdit, QHBoxLayout

class IDE(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 IDE')
        self.setGeometry(100, 100, 800, 600)

        # Create menu bar
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')
        self.edit_menu = self.menu.addMenu('Edit')
        self.create_actions()

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create tabs
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Create file explorer
        self.file_explorer = QTreeView()
        self.tabs.addTab(self.file_explorer, 'File Explorer')

        # Create code editor
        self.code_editor = QTextEdit()
        self.tabs.addTab(self.code_editor, 'Code Editor')

        # Create terminal
        self.terminal = QLineEdit()
        self.terminal.setPlaceholderText('Terminal...')
        self.layout.addWidget(self.terminal)

        # Create project management section
        self.project_manager = QTextEdit()
        self.tabs.addTab(self.project_manager, 'Project Management')

    def create_actions(self):
        # File actions
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        self.file_menu.addAction(open_action)

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        self.file_menu.addAction(save_action)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File')
        if file_name:
            with open(file_name, 'r') as file:
                content = file.read()
                self.code_editor.setText(content)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File')
        if file_name:
            with open(file_name, 'w') as file:
                content = self.code_editor.toPlainText()
                file.write(content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ide = IDE()
    ide.show()
    sys.exit(app.exec())