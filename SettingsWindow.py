from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from components.FontSizeOption import FontSizeOption
from components.PrimaryInput import PrimaryInput

class SettingsWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.resize(400, 200)
		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setStyleSheet("background-color: #272d44; color: #8e9fb4;")

		self.title = QLabel("Preferences")
		self.title.setStyleSheet("font-size: 18px;")

		self.fontLabel = QLabel("Font")
		self.fontSizeInput = PrimaryInput("Font size")
		self.fontSizeInput.setText("18")
		self.fontSizeLabel = QLabel("Font size")


		# self.smallFontOption = QWidget()
		# self.smallFontOption.setStyleSheet("QWidget {background-color: #2e3653; color: #8e9fb4; border-radius: 6px; font-size: 28px;}")
		# self.smallFontOption.setFixedWidth(70)
		# self.smallFontOption.setFixedHeight(70)
		# self.fontSmallOptionLayout = QVBoxLayout()
		# self.fontSmallOptionLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		# self.fontSmallLabel = QLabel()
		# self.fontSmallLabel.setText("Aa")
		# self.fontSmallOptionLayout.addWidget(self.fontSmallLabel)
		# self.smallFontOption.setLayout(self.fontSmallOptionLayout)

		self.smallFontOption = FontSizeOption()
		
		layout.addWidget(self.title)
		layout.addWidget(self.fontLabel)
		layout.addWidget(self.fontSizeLabel)
		layout.addWidget(self.smallFontOption)
		self.setLayout(layout)