#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

class ButtonWindow(QtGui.QWidget):
    def __init__(self, msg):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Click Window")
        self.setGeometry(300, 200, 200, 200)
        self.button = QtGui.QPushButton(msg, self)
        self.button.setGeometry(50, 30, 100, 30)
        self.button.clicked.connect(self.hello)
        #QtCore.QObject.connect(self.button, QtCore.SIGNAL('clicked()'), self.hello)

    def hello(self):
        print 'Hello World'

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    #button = QtGui.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    bw = ButtonWindow("Click me!")
    bw.show()
    sys.exit(app.exec_())
