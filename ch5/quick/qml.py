#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets, QtQuick

app = QtWidgets.QApplication(sys.argv)
view = QtQuick.QQuickView()
url = QtCore.QUrl('hello.qml')
view.setSource(url)
view.show()
sys.exit(app.exec_())
