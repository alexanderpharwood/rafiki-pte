from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QCursor

from PyQt6.QtCore import Qt

class FontSizeOption(QWidget):
	def __init__(self):
		super().__init__()
		self.setStyleSheet("QWidget {background-color: #2e3653; color: #8e9fb4; border-radius: 6px; font-size: 28px;} QWidget:hover {background-color: #333B5B;}")
		self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label = QLabel()
		self.label.setText("Aa")
		self.label.setFixedWidth(80)
		self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label.setFixedHeight(80)
		self.layout.addWidget(self.label)
		self.setLayout(self.layout)
  

