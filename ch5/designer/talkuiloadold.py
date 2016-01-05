#!/usr/bin/env python
# -*- coding: utf-8 -*

import sys
from PySide import QtCore, QtGui, QtNetwork, QtUiTools

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

class TalkMainWindow(object):
    def __init__(self, uifile):
        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(uifile)
        self.connectButton = self.ui.findChild(QtGui.QWidget, "connectButton")
        self.talkMain = self.ui.findChild(QtGui.QWidget, "talkMain")
        self.messageEdit = self.ui.findChild(QtGui.QWidget, "messageEdit")
        self.sendButton = self.ui.findChild(QtGui.QWidget, "sendButton")

        self.connectButton.clicked.connect(self.connect)
        self.ui.closeEvent = self.closeEvent

        self.socket = QtNetwork.QTcpSocket(self.ui)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)

    def connect(self):
        cw = ConnectWindow(self.ui)
        if cw.exec_() == QtGui.QDialog.Accepted:
            self.socket.connectToHost(cw.server.text(), int(cw.port.text()))
            if self.socket.waitForConnected(1000):
                self.name = cw.name.text()
                self.send("login %s" % self.name)
                self.sendButton.clicked.connect(self.sendClick)
                self.messageEdit.returnPressed.connect(self.sendClick)
                self.messageEdit.setFocus()

    def readData(self):
        message = self.socket.readLine().data().decode("utf-8")
        self.talkMain.append(message)

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendClick(self):
        self.send("say %s" % (self.messageEdit.text()))
        self.messageEdit.clear()
        self.messageEdit.setFocus()

    def displayError(self):
        QtGui.QMessageBox.information(self.ui, "Connection", "Error during connection")

    def closeEvent(self, event):
        self.socket.disconnectFromHost()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    tmw = TalkMainWindow("talk.ui")
    tmw.ui.show()
    sys.exit(app.exec_())
