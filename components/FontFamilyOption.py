from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt
from utilities.Styleable import Styleable

class FontFamilyOption(QWidget, Styleable):
	def __init__(self):
		super().__init__()
		self.style.setIdentifier("QWidget")
		self.style.setRule("background-color", "#2e3653")
		self.style.setRule("color", "#8e9fb4")
		self.style.setRule("border-radius", "6px")
		self.style.setRule("font-family", "Courier New")
		# self.style.setRule("font-weight", "bold")
		self.style.setRule("font-size", "22px")
		self.style.setPseudoRule("hover", "background-color", "#333B5B")
		self.applyStyles()

		self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label = QLabel()
		self.label.setText("Aa")
		self.label.setFixedWidth(80)
		self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.label.setFixedHeight(80)
		layout.addWidget(self.label)
		self.setLayout(layout)
  

