#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets, QtQuick

def sayThis(s):
    print(s)

class Controller(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.Slot(QtCore.QObject, str)
    def textEnter(self, root, text):
        sayThis("accepted textinput: "+text)
        widgets = root.property('widgets')
        widgets.property('textinput').setProperty('text', '')
        #widgets['textinput'].setProperty('text', '')

    @QtCore.Slot(QtCore.QObject)
    def buttonClick(self, root):
        sayThis("clicked button")

    @QtCore.Slot()
    def init(self):
        sayThis("test function")

app = QtWidgets.QApplication(sys.argv)
view = QtQuick.QQuickView()

ctx = view.rootContext()
con = Controller()
ctx.setContextProperty("con", con)
url = QtCore.QUrl('input2.qml')
view.setSource(url)

view.show()
sys.exit(app.exec_())
