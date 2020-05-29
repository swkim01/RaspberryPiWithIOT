#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets

class ButtonWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Button Window")
        self.setGeometry(300, 200, 200, 200)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.setContentsMargins(QtCore.QMargins(5,5,5,5))
        vbox.setSpacing(10)
        self.checkbox = QtWidgets.QCheckBox("CheckButton", self)
        self.checkbox.setObjectName("check")
        vbox.addWidget(self.checkbox)

        buttongroup = QtWidgets.QButtonGroup()
        self.radiobutton1 = QtWidgets.QRadioButton("RadioButton1", self)
        self.radiobutton1.setObjectName("radio1")
        buttongroup.addButton(self.radiobutton1)
        vbox.addWidget(self.radiobutton1)
        self.radiobutton2 = QtWidgets.QRadioButton("RadioButton2", self)
        self.radiobutton2.setObjectName("radio2")
        buttongroup.addButton(self.radiobutton2)
        vbox.addWidget(self.radiobutton2)

        self.button = QtWidgets.QPushButton("OK", self)
        self.button.setObjectName("button")
        vbox.addWidget(self.button)
        self.button.clicked.connect(self.clicked)

        self.combo = QtWidgets.QComboBox(self)
        self.combo.setObjectName("combo")
        self.combo.addItem("Apple")
        self.combo.addItem("Banana")
        self.combo.addItem("Grapes")
        vbox.addWidget(self.combo)
        self.combo.activated[str].connect(self.activated)

        self.resize(350, 200)

    def printState(self, button):
        if button.isChecked():
            print(button.objectName(), "is checked")
        else :
            print(button.objectName(), "is not checked")

    def clicked(self):
        self.printState(self.checkbox)
        self.printState(self.radiobutton1)
        self.printState(self.radiobutton2)

    def activated(self, text):
        print(self.combo.objectName(), "is", text)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    #button = QtWidgets.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    bw = ButtonWindow()
    bw.show()
    sys.exit(app.exec_())
