#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
from PySide import QtCore, QtGui, QtNetwork
from talk import *

class ConnectWindow(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        #QtGui.QDialog.__init__(parent)
        self.setWindowTitle("Connect Window")
        vbox = QtGui.QVBoxLayout(self)
        hbox1 = QtGui.QHBoxLayout()
        hbox2 = QtGui.QHBoxLayout()
        hbox3 = QtGui.QHBoxLayout()
        hbox4 = QtGui.QHBoxLayout()
        self.server = QtGui.QLineEdit()
        self.server.setText("localhost")
        self.port = QtGui.QLineEdit()
        self.port.setText("8080")
        self.name = QtGui.QLineEdit()
        self.name.setText(u'홍길동')
        self.ok = QtGui.QPushButton("OK", self)
        self.cancel = QtGui.QPushButton("Cancel", self)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        hbox1.addWidget(QtGui.QLabel("Server:", self))
        hbox1.addWidget(self.server)
        hbox2.addWidget(QtGui.QLabel("Port:", self))
        hbox2.addWidget(self.port)
        hbox3.addWidget(QtGui.QLabel("Name:", self))
        hbox3.addWidget(self.name)
        hbox4.addWidget(self.ok)
        hbox4.addWidget(self.cancel)
        self.ok.clicked.connect(self.accept)
        self.cancel.clicked.connect(self.reject)

class TalkMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TalkMainWindow, self).__init__(parent)
        self.ui = Ui_TalkWindow()
        self.ui.setupUi(self)
        self.ui.connectButton.clicked.connect(self.connect)

        self.socket = QtNetwork.QTcpSocket(self)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)
        self.connectState = False

    def connect(self):
        if not self.connectState:
            cw = ConnectWindow()
            if cw.exec_() == QtGui.QDialog.Accepted:
                self.socket.connectToHost(cw.server.text(), int(cw.port.text()))
                if self.socket.waitForConnected(1000):
                    self.name = cw.name.text()
                    self.send("login %s" % self.name)
                    self.ui.sendButton.clicked.connect(self.sendClick)
                    self.ui.messageEdit.returnPressed.connect(self.sendClick)
                    self.ui.messageEdit.setFocus()
                    self.ui.connectButton.setText("Disconnect")
                    self.connectState = True
        else:
            self.socket.disconnectFromHost()
            self.ui.connectButton.setText("Connect")
            self.connectState = False

    def readData(self):
        message = self.socket.readLine().data().decode("utf-8")
        self.ui.talkMain.append(message)

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendClick(self):
        self.send("say %s" % (self.ui.messageEdit.text()))
        self.ui.messageEdit.clear()
        self.ui.messageEdit.setFocus()

    def displayError(self):
        QtGui.QMessageBox.information(self, "Connection", "Error during connection")

    def closeEvent(self, event):
        self.socket.disconnectFromHost()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    tmw = TalkMainWindow()
    tmw.show()
    sys.exit(app.exec_())
