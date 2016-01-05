#!/usr/bin/env python
#-'''- coding: utf-8 -'''-

import sys
from PySide import QtCore, QtGui, QtDeclarative, QtNetwork

def sayThis(s):
    print s

class Controller(QtCore.QObject):
    def __init__(self, ctx):
        QtCore.QObject.__init__(self)
        self.text=""
        self.socket = QtNetwork.QTcpSocket(ctx)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)

    @QtCore.Slot(QtCore.QObject)
    def init(self, root):
        self.root = root

    @QtCore.Slot(QtCore.QObject, str)
    def send(self, root, text):
        #sayThis("clicked sendbutton "+text)
        self.sendmessage("say %s" % (text))
        widgets = root.property('widgets')
        widgets['textinput'].setProperty('text', '')

    @QtCore.Slot(QtCore.QObject)
    def connect(self, root):
        #sayThis("clicked connectbutton")
        widgets = root.property('widgets')
        server=widgets['server'].property('text')
        port=widgets['port'].property('text')
        self.socket.connectToHost(server, int(port))
        if self.socket.waitForConnected(1000):
            self.name = widgets['name'].property('text')
            self.sendmessage("login %s" % self.name)

    def readData(self):
        message = self.socket.readLine().data().decode("utf-8")
        self.text += message + '\r\n'
        #sayThis(self.text)
        widgets = self.root.property('widgets')
        widgets['textedit'].setProperty('text', self.text)

    def sendmessage(self, message):
        self.socket.write(message.encode("utf-8"))

    def displayError(self):
        #QtGui.QMessageBox.information(self.root, "Connection", "Error during connection")
        widgets = self.root.property('widgets')
        QtCore.QMetaObject.invokeMethod(widgets['error'], "show", QtCore.Qt.DirectConnection)

    def closeEvent(self, event):
        self.socket.disconnectFromHost()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    view = QtDeclarative.QDeclarativeView()
    url = QtCore.QUrl('talk.qml')

    ctx = view.rootContext()
    con = Controller(ctx)
    ctx.setContextProperty("con", con)
    view.setSource(url)
    view.show()
    sys.exit(app.exec_())
