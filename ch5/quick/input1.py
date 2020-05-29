#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets, QtQuick

def Print(s):
    print(s)

def Clear(root, text):
    Print("accepted textinput: "+text)
    QtCore.QMetaObject.invokeMethod(root, "clear", QtCore.Qt.DirectConnection)


app = QtWidgets.QApplication(sys.argv)
view = QtQuick.QQuickView()
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
