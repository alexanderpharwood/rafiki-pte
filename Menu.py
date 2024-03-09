from PyQt6.QtWidgets import QMenuBar, QMenu, QFileDialog
from PyQt6.QtGui import QKeySequence
from SettingsWindow import SettingsWindow


class Menu(QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.window = parent
        self.settingsWindow = None
        fileMenu = QMenu("&File", self)
        editMenu = QMenu("&Edit", self)
        preferencesAction = editMenu.addAction("Preferences")
        findAction = editMenu.addAction("Find")
        findAction.setShortcut(QKeySequence("Ctrl+f"))

        newAction = fileMenu.addAction("New")
        openAction = fileMenu.addAction("Open")
        saveAction = fileMenu.addAction("Save")
        newAction.setShortcut(QKeySequence("Ctrl+n"))
        openAction.setShortcut(QKeySequence("Ctrl+o"))
        saveAction.setShortcut(QKeySequence("Ctrl+s"))

        saveAction.triggered.connect(self.saveActionHandler)
        openAction.triggered.connect(self.openActionHandler)
        preferencesAction.triggered.connect(self.openPreferencesHandler)
        findAction.triggered.connect(self.openFindHandler)

        self.addMenu(fileMenu)
        self.addMenu(editMenu)
    
    def saveActionHandler(self):
        content = self.window.editor.editor.toPlainText()
        if self.window.workingFileLocation == None:
            newFileName, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text files (*.txt)")
            if newFileName == "":
                return
        else:
            newFileName = self.window.workingFileLocation
        with open(newFileName, 'w') as file:
            file.write(content)
        self.window.workingFileLocation = newFileName

    def openActionHandler(self):
        openFileName, _ = QFileDialog.getOpenFileName(self, "Open file")
        if openFileName == "":
            return
        openFile = open(openFileName,'r')
        with openFile:
            data = openFile.read()
            self.window.editor.editor.setPlainText(data)
        self.window.workingFileLocation = openFileName
        self.window.setCentralWidget(self.window.editor)
        self.window.editor.show()

    def openPreferencesHandler(self):
       self.settingsWindow = SettingsWindow(self.window)
       self.settingsWindow.show()

    def openFindHandler(self):
        if self.window.editor.isHidden() == True:
            return
        
        if  self.window.editor.findOpen == False:
            self.window.editor.findBar.show()
            self.window.editor.findBar.input.setFocus()
            self.window.editor.findOpen = True
        else:
            self.window.editor.findBar.resetHighlightFormatting()
            self.window.editor.findBar.hide()
            self.window.editor.findBar.clearValue()
            self.window.editor.findOpen = False
            
            