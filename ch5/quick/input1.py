#!/usr/bin/env python
#-'''- coding: utf-8 -'''-

import sys
from PySide import QtCore, QtGui, QtDeclarative

def Print(s):
    print s

def Clear(root, text):
    Print("accepted textinput: "+text)
    QtCore.QMetaObject.invokeMethod(root, "clear", QtCore.Qt.DirectConnection)


app = QtGui.QApplication(sys.argv)
view = QtDeclarative.QDeclarativeView()
url = QtCore.QUrl('input.qml')
view.setSource(url)

root = view.rootObject()
#/button = root.findChild(QtCore.QObject,"inputButton")
inputButton = root.findChild(QtCore.QObject,"inputbutton")
inputButton.clicked.connect(lambda: Print("clicked button"))
textinput = root.findChild(QtCore.QObject,"textinput")
textinput.accepted.connect(lambda: Clear(root, textinput.property('text')))

view.show()
sys.exit(app.exec_())
