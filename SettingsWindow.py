from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QMouseEvent
from components.FontSizeOption import FontSizeOption
from components.FontFamilyOption import FontFamilyOption


class SettingsWindow(QWidget):
	def __init__(self, window):
		super().__init__()
		self.window = window
		self.resize(400, 200)
		self.settings = QSettings("RAFIKI", "settings")
		layout = QVBoxLayout()
		self.setWindowTitle("Preferences")
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.setStyleSheet("background-color: #272d44; color: #8e9fb4;")

		self.fontLabel = QLabel("Font")
		self.fontSizeLabel = QLabel("Font size")

		fontSizeOptionsLayout = QHBoxLayout()
		fontFamilyOptionsLayout = QHBoxLayout()


		self.smallFontOption = FontSizeOption()
		self.smallFontOption.style.setRule("font-size", "12px")
		self.smallFontOption.mouseReleaseEvent = self.fontSizeChangeHandler("12px")
		self.mediumFontOption = FontSizeOption()
		self.mediumFontOption.style.setRule("font-size", "16px")
		self.mediumFontOption.mouseReleaseEvent = self.fontSizeChangeHandler("16px")
		self.largeFontOption = FontSizeOption()
		self.largeFontOption.style.setRule("font-size", "22px")
		self.largeFontOption.mouseReleaseEvent = self.fontSizeChangeHandler("22px")

		fontSizeOptionsLayout.addWidget(self.smallFontOption)
		fontSizeOptionsLayout.addWidget(self.mediumFontOption)
		fontSizeOptionsLayout.addWidget(self.largeFontOption)

		self.monoFontOption = FontFamilyOption()
		self.monoFontOption.style.setRule("font-family", "Courier New")
		self.monoFontOption.label.setText("Mono")
		# self.smallFontOption.mouseReleaseEvent = self.fontSizeChangeHandler("12px")
		self.serifFontOption = FontFamilyOption()
		self.serifFontOption.style.setRule("font-family", "Georgia")
		self.serifFontOption.label.setText("Serif")

		# self.mediumFontOption.mouseReleaseEvent = self.fontSizeChangeHandler("16px")
		self.sansFontOption = FontFamilyOption()
		self.sansFontOption.style.setRule("font-family", "Arial")
		self.sansFontOption.label.setText("Sans")

		# self.largeFontOption.mouseReleaseEvent = self.fontSizeChangeHandler("22px")
		self.renderOptionsStyle()

		fontFamilyOptionsLayout.addWidget(self.monoFontOption)
		fontFamilyOptionsLayout.addWidget(self.serifFontOption)
		fontFamilyOptionsLayout.addWidget(self.sansFontOption)
		
		layout.addWidget(self.fontLabel)
		layout.addLayout(fontSizeOptionsLayout)
		layout.addWidget(self.fontSizeLabel)
		layout.addLayout(fontFamilyOptionsLayout)
		self.setLayout(layout)
	
	def fontSizeChangeHandler(self, size: str):
		def handle(evnet: QMouseEvent | None) -> None:
			self.settings.setValue("font_size", size)
			self.renderOptionsStyle()
		return handle


	def renderOptionsStyle(self):
		defaultColor = "#2e3653"
		activeColor = "#384063"

		if self.settings.value("font_size") == "12px":
			self.smallFontOption.style.setRule("background-color", activeColor)
		else:
			self.smallFontOption.style.setRule("background-color", defaultColor)

		if self.settings.value("font_size") == "16px":
			self.mediumFontOption.style.setRule("background-color", activeColor)
		else:
			self.mediumFontOption.style.setRule("background-color", defaultColor)

		if self.settings.value("font_size") == "22px":
			self.largeFontOption.style.setRule("background-color", activeColor)
		else:
			self.largeFontOption.style.setRule("background-color", defaultColor)

		self.smallFontOption.applyStyles()
		self.mediumFontOption.applyStyles()
		self.largeFontOption.applyStyles()
		self.monoFontOption.applyStyles()
		self.serifFontOption.applyStyles()
		self.sansFontOption.applyStyles()
		self.window.editor.editor.renderStyles()