import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QTextEdit, QVBoxLayout, QWidget, QFileDialog, QHBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class IDEInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt6 IDE')
        self.setGeometry(100, 100, 1200, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # File Explorer
        self.file_explorer = QWidget()
        self.file_explorer_layout = QVBoxLayout(self.file_explorer)
        self.file_explorer_button = QPushButton('Open File')
        self.file_explorer_button.clicked.connect(self.open_file)
        self.file_explorer_layout.addWidget(self.file_explorer_button)
        self.file_explorer.setLayout(self.file_explorer_layout)
        self.tabs.addTab(self.file_explorer, 'File Explorer')

        # Code Editor
        self.code_editor = QTextEdit()
        self.tabs.addTab(self.code_editor, 'Code Editor')

        # Terminal
        self.terminal = QTextEdit()
        self.terminal.setReadOnly(True)
        self.tabs.addTab(self.terminal, 'Terminal')

        # AI Chat Panel
        self.chat_panel = QTextEdit()
        self.chat_panel.setPlaceholderText('Chat with AI...')
        self.tabs.addTab(self.chat_panel, 'AI Chat')

        self.show()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Python Files (*.py);;All Files (*)')
        if file_name:
            with open(file_name, 'r') as file:
                code = file.read()
                self.code_editor.setPlainText(code)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ide = IDEInterface()
    sys.exit(app.exec())