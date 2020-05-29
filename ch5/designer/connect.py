# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui',
# licensing of 'connect.ui' applies.
#
# Created: Wed Aug 28 17:40:14 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(252, 150)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 110, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 231, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.server = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.server.setObjectName("server")
        self.gridLayout.addWidget(self.server, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.port = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Connect", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Server:", None, -1))
        self.server.setText(QtWidgets.QApplication.translate("Dialog", "localhost", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Port:", None, -1))
        self.port.setText(QtWidgets.QApplication.translate("Dialog", "8080", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Name:", None, -1))
        self.name.setText(QtWidgets.QApplication.translate("Dialog", "홍길동", None, -1))

