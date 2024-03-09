from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout
from PyQt6.QtCore import QSettings
from components.FindBar import FindBar
from utilities.Styleable import Styleable, StyleSheet
from TextEditor import TextEditor

class Editor(QWidget, Styleable):
	def __init__(self, window):
		super().__init__()
		self.editor = TextEditor()
		self.window = window
		self.settings = QSettings("RAFIKI", "settings")
		self.findOpen = False
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

		
		# self.editor.moveCursor