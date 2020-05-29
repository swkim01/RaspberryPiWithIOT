#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
#label = QtWidgets.QLabel("Hello World")
label = QtWidgets.QLabel("<h2>Hello World</h2>")
#label = QtWidgets.QLabel("<font color=blue size=40>Hello World</font>")
label.show()
app.exec_()
sys.exit()
