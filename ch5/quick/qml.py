#!/usr/bin/env python
#-'''- coding: utf-8 -'''-

import sys
from PySide import QtCore, QtGui, QtDeclarative

app = QtGui.QApplication(sys.argv)
view = QtDeclarative.QDeclarativeView()
url = QtCore.QUrl('hello.qml')
view.setSource(url)
view.show()
sys.exit(app.exec_())
