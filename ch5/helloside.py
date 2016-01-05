#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

app = QtGui.QApplication(sys.argv)
label = QtGui.QLabel("Hello World")
#label = QtGui.QLabel("<h2>Hello World</h2>")
#label = QtGui.QLabel("<font color=blue size=40>Hello World</font>")
label.show()
app.exec_()
sys.exit()
