from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QBrush, QColor

class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)
        self.highlightFormat = QTextCharFormat()
        self.highlightFormat.setBackground(QColor("#384063"))

    def highlightBlock(self, text):
        print(self.document().find("test"))

        # pattern = r""
        # expression = QRegExp(pattern)
        # index = text.indexOf(expression)
        # while index >= 0:
        #     length = expression.matchedLength()
        #     setFormat(index, length, myClassFormat)
        #     index = text.indexOf(expression, index + length)