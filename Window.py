from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from Editor import Editor
from Menu import Menu
from components.PrimaryButton import PrimaryButton

class Window(QMainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.workingFileLocation = None
		self.setWindowTitle("RAFIKI PTE")
		self.resize(800, 600)
		self.setStyleSheet("QMainWindow { background-color: #272d44; color: #8e9fb4;}")

		layout = QVBoxLayout()
		subLayout = QHBoxLayout()
		layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
		subLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

		layout.addStretch()
		splashHeader = QLabel()
		splashHeader.setText("R A F I K I")
		splashHeader.setStyleSheet("font-size: 60px; font-family: Georgia; color: #1D2235")
		splashHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)

		splashDescription = QLabel()
		splashDescription.setAlignment(Qt.AlignmentFlag.AlignCenter)
		splashDescription.setText("The simple and pretty plain text editor")
		splashDescription.setStyleSheet("font-size: 14px; font-family: Georgia; color: #8e9fb4")

		splashFooter = QLabel()
		splashFooter.setAlignment(Qt.AlignmentFlag.AlignCenter)
		splashFooter.setText("Rafiki v0.0.1 by @alexanderpharwood")
		splashFooter.setStyleSheet("font-size: 11px; font-family: Georgia; color: #8e9fb4")

		newFileButton = PrimaryButton("New", self)
		newFileButton.setHandler(self.loadEditor)
		openFileButton = PrimaryButton("Open", self)
		openFileButton.setHandler(self.loadEditorWithFile)

		self.editor = Editor()
		layout.addWidget(splashHeader)
		layout.addWidget(splashDescription)
		layout.addSpacing(20)


		subLayout.addWidget(newFileButton)
		subLayout.addWidget(openFileButton)

		
		layout.addLayout(subLayout)
		layout.addStretch()

		layout.addWidget(splashFooter)

		widget = QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
		self.menu = Menu(self)
		self.setMenuBar(self.menu)

	def loadEditor(self):
		self.setCentralWidget(self.editor)

	def loadEditorWithFile(self):
		self.menu.openActionHandler()
