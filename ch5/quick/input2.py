#!/usr/bin/env python
#-'''- coding: utf-8 -'''-

import sys
from PySide import QtCore, QtGui, QtDeclarative

def sayThis(s):
    print s

class Controller(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)

    @QtCore.Slot(QtCore.QObject, str)
    def textEnter(self, root, text):
        sayThis("accepted textinput: "+text)
        widgets = root.property('widgets')
        widgets['textinput'].setProperty('text', '')

    @QtCore.Slot(QtCore.QObject)
    def buttonClick(self, root):
        sayThis("clicked button")

app = QtGui.QApplication(sys.argv)
view = QtDeclarative.QDeclarativeView()
url = QtCore.QUrl('input2.qml')
view.setSource(url)

ctx = view.rootContext()
con = Controller()
ctx.setContextProperty("con", con)

view.show()
sys.exit(app.exec_())
