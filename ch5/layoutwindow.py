#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

class LayoutWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Layout Window")
        hbox = QtGui.QHBoxLayout(self)
        vbox = QtGui.QVBoxLayout()
        label1 = QtGui.QLabel("Top", self, 0)
        label2 = QtGui.QLabel("Bottom", self, 0)
        label3 = QtGui.QLabel("Right", self, 0)
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        hbox.addLayout(vbox)
        hbox.addWidget(label3)
        self.resize(150, 100)

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    #button = QtGui.QPushButton('Hello')
    #button.clicked.connect(hello)
    #button.show()
    lw = LayoutWindow()
    lw.show()
    sys.exit(app.exec_())
