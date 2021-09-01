#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets, QtNetwork
from talk import *
from connect import *

class ConnectWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ConnectWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class TalkMainWindow(QtWidgets.QMainWindow):
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
            if cw.exec_() == QtWidgets.QDialog.Accepted:
                self.socket.connectToHost(cw.ui.server.text(), int(cw.ui.port.text()))
                if self.socket.waitForConnected(1000):
                    self.name = cw.ui.name.text()
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
        self.send("msg %s" % (self.ui.messageEdit.text()))
        self.ui.messageEdit.clear()
        self.ui.messageEdit.setFocus()

    def displayError(self):
        QtWidgets.QMessageBox.information(self, "Connection", "Error during connection")

    def closeEvent(self, event):
        self.socket.disconnectFromHost()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tmw = TalkMainWindow()
    tmw.show()
    sys.exit(app.exec_())
