from PyQt6.QtWidgets import QTextEdit
from utilities.Styleable import Styleable
from PyQt6.QtCore import QSettings

class TextEditor(QTextEdit, Styleable):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("RAFIKI", "settings")
        self.style.setIdentifier("QTextEdit")
        self.style.setRule("background-color", "#272d44")
        self.style.setRule("color", "#8e9fb4")
        self.style.setRule("padding", "20px")
        self.style.setRule("font-family", "Courier New")
        self.style.setRule("font-size", self.settings.value("font_size"))
        self.applyStyles()

    def renderStyles(self):
        self.style.setRule("font-size", self.settings.value("font_size"))
        self.applyStyles()