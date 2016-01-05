#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

class ButtonWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Button Window")
        self.setGeometry(300, 200, 200, 200)
        vbox = QtGui.QVBoxLayout(self)
        vbox.setContentsMargins(QtCore.QMargins(5,5,5,5))
        vbox.setSpacing(10)
        self.checkbox = QtGui.QCheckBox("CheckButton", self)
        self.checkbox.setObjectName("check")
        vbox.addWidget(self.checkbox)

        buttongroup = QtGui.QButtonGroup()
        self.radiobutton1 = QtGui.QRadioButton("RadioButton1", self)
        self.radiobutton1.setObjectName("radio1")
        buttongroup.addButton(self.radiobutton1)
        vbox.addWidget(self.radiobutton1)
        self.radiobutton2 = QtGui.QRadioButton("RadioButton2", self)
        self.radiobutton2.setObjectName("radio2")
        buttongroup.addButton(self.radiobutton2)
        vbox.addWidget(self.radiobutton2)

        self.button = QtGui.QPushButton("OK", self)
        self.button.setObjectName("button")
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.clicked)

        self.combo = QtGui.QComboBox(self)
        self.combo.setObjectName("combo")
        self.combo.addItem("Apple")
        self.combo.addItem("Banana")
        self.combo.addItem("Grapes")
        vbox.addWidget(self.combo)
        self.combo.activated[str].connect(self.activated)

        self.resize(350, 200)

    def printState(self, button):
        if button.isChecked():
            print button.objectName(), "is checked"
        else :
            print button.objectName(), "is not checked"

    def clicked(self):
        self.printState(self.checkbox)
        self.printState(self.radiobutton1)
        self.printState(self.radiobutton2)

    def activated(self, text):
        print self.combo.objectName(), "is", text

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    #button = QtGui.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    bw = ButtonWindow()
    bw.show()
    sys.exit(app.exec_())
