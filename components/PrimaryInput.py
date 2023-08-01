from PyQt6.QtWidgets import QLineEdit

class PrimaryInput(QLineEdit):
    def __init__(self, placeholder, parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setFixedWidth(200)
        self.setStyleSheet("QLineEdit {background-color: #2e3653; color: #8e9fb4; padding: 12px 20px; border-radius: 6px;} QPushButton:focus {background-color: #333B5B;}")

