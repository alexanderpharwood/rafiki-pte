from utilities.StyleSheet import StyleSheet

class Styleable:
	def __init__(self):
		super().__init__()
		self.style = StyleSheet()

	def applyStyles(self):
		self.setStyleSheet(self.style.compile())
