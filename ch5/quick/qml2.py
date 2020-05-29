#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtGui, QtQml

app = QtGui.QGuiApplication(sys.argv)
engine = QtQml.QQmlApplicationEngine()
engine.load(QtCore.QUrl.fromLocalFile('app.qml'))
sys.exit(app.exec_())
