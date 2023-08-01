from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from components.FindBar import FindBar

class Editor(QWidget):
        def __init__(self, parent=None):
                super().__init__(parent)
                self.editor = QTextEdit()
                self.findOpen = False
                self.editor.setStyleSheet("QTextEdit { padding: 20px; background-color: #272d44; color: #8e9fb4; font-size: 16px; font-family: Courier New; }")
                self.editor.setCursorWidth(3)
                self.editor.setPlaceholderText("Isn't it pretty to think so?")
                
                self.findBar = FindBar(self)
                layout = QVBoxLayout()
                layout.addWidget(self.editor)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)
                layout.addWidget(self.findBar)
                self.findBar.hide()
                self.setLayout(layout)

                
                self.editor.moveCursor