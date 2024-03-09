from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

class PrimaryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("QPushButton {background-color: #2e3653; color: #8e9fb4; padding-left: 20px; padding-right: 20px; border-radius: 6px;} QPushButton:hover {background-color: #333B5B;} QPushButton:pressed {background-color: #384063;}")
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setFixedHeight(50)
    def setHandler(self, handler):
        self.clicked.connect(handler)

