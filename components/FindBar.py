from PyQt6.QtWidgets import QWidget, QHBoxLayout, QApplication, QLabel
from PyQt6.QtGui import QTextCharFormat, QColor, QTextCursor, QTextDocument
from PyQt6.QtCore import Qt
from components.PrimaryInput import PrimaryInput

class FindBar(QWidget):
    def __init__(self, editor):
        super().__init__()
        self.editor = editor
        self.findCursor = None
        findBarLayout = QHBoxLayout()
        self.input = PrimaryInput("Search for something")
        self.noResultsLabel = QLabel()
        self.noResultsLabel.setStyleSheet("color: #8e9fb4;")
        self.noResultsLabel.hide()
        self.noResultsLabel.setText("No results found")
        self.input.returnPressed.connect(self.onSearch)
        self.setFixedHeight(65)
        findBarLayout.addWidget(self.input)
        findBarLayout.addWidget(self.noResultsLabel)
        findBarLayout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.setLayout(findBarLayout)

    def onSearch(self):
        text = self.input.text()
        if text == "":
            return
        if self.findCursor != None:
           self.resetHighlightFormatting() 
        self.initialCursor = self.editor.editor.textCursor()
        modifiers = QApplication.keyboardModifiers()
        findOptions = QTextDocument.FindFlag(0)
        if modifiers == Qt.KeyboardModifier.ShiftModifier:
            findOptions = QTextDocument.FindFlag(1)
        self.findCursor = self.editor.editor.document().find(text, self.initialCursor, findOptions)
        if self.findCursor.isNull() == True:
            self.noResultsLabel.show()
        else:
            self.noResultsLabel.hide()
            cursorAfterFind = self.findCursor.selectionEnd() - self.initialCursor.position()
            cursorMoveDirection = QTextCursor.MoveOperation.Right
            if modifiers == Qt.KeyboardModifier.ShiftModifier:
                cursorMoveDirection = QTextCursor.MoveOperation.Left
                cursorAfterFind = self.initialCursor.position() - self.findCursor.selectionStart()
            format = QTextCharFormat()
            format.setBackground(QColor("#384063"))
            format.setForeground(QColor("#efefef"))
            self.findCursor.setCharFormat(format)
            self.initialCursor.movePosition(cursorMoveDirection, QTextCursor.MoveMode.MoveAnchor, cursorAfterFind)
            self.editor.editor.setTextCursor(self.initialCursor)
   
    def resetHighlightFormatting(self):
        default = QTextCharFormat()
        charFormat = self.findCursor.charFormat()
        charFormat.setBackground(default.background())
        charFormat.setForeground(default.foreground())
        self.findCursor.mergeCharFormat(charFormat)

    def clearValue(self):
        self.input.clear()