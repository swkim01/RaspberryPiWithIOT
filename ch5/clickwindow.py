#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets

class ButtonWindow(QtWidgets.QWidget):
    def __init__(self, msg):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Click Window")
        self.setGeometry(300, 200, 200, 200)
        self.button = QtWidgets.QPushButton(msg, self)
        self.button.setGeometry(50, 30, 100, 30)
        self.button.clicked.connect(self.hello)
        #QtCore.QObject.connect(self.button, QtCore.SIGNAL('clicked()'), self.hello)

    def hello(self):
        print('Hello World')

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    #button = QtWidgets.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    bw = ButtonWindow("Click me!")
    bw.show()
    sys.exit(app.exec_())
