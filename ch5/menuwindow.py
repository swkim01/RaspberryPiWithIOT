#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtGui, QtWidgets

class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("Menu Window")
        self.setGeometry(300, 200, 300, 300)

    def setMenus(self):
        self.statusBar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.helpMenu = self.menuBar().addMenu("&Help")
        self.newAction = QtWidgets.QAction(QtGui.QIcon('filenew.png'), "&New", self,
                         shortcut=QtGui.QKeySequence.New, statusTip="Create New File",
                         triggered=self.newFile)
        self.openAction = QtWidgets.QAction("&Open", self,
                         shortcut=QtGui.QKeySequence.Open, statusTip="Open File",
                         triggered=self.openFile)
        self.saveAction = QtWidgets.QAction("&Save", self,
                         shortcut=QtGui.QKeySequence.Save, statusTip="Save File")
        self.exitAction = QtWidgets.QAction(QtGui.QIcon('application-exit.png'), "E&xit", self,
                         shortcut="Ctrl+Q", statusTip="Exit Application",
                         triggered=self.close)
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.aboutAction = QtWidgets.QAction("&About", self,
                         statusTip="About Program",
                         triggered=self.aboutProgram)
        self.helpMenu.addAction(self.aboutAction)
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(self.exitAction)
        self.textedit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.textedit)

    def newFile(self):
        self.textedit.setText('')

    def openFile(self):
        self.filename, self.filtername = QtWidgets.QFileDialog.getOpenFileName(self)
        self.textedit.setText(open(self.filename).read())

    def aboutProgram(self):
        QtWidgets.QMessageBox.about(self, "About This Program",
                         "This program tests menus and file dialog")

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    #button = QtWidgets.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    mw = MenuWindow()
    mw.setMenus()
    mw.show()
    sys.exit(app.exec_())
