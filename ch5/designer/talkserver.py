#!/usr/bin/env python
#-*-coding: utf-8-*-

import random
from PySide import QtCore, QtNetwork

class Server(QtNetwork.QTcpServer):
    def __init__(self, parent=None):
        super(Server, self).__init__(parent)
        self.newConnection.connect(self.newClient)

        self.clients = {}

    def newClient(self):
        socket = self.nextPendingConnection()
        socket.readyRead.connect(self.readData)
        socket.disconnected.connect(self.disconnectClient)
        self.clients[socket] = {}
        self.clients[socket]["name"] = u"손님-%d" % random.randint(1, 100)

    def disconnectClient(self):
        socket = self.sender()
        self.sendAll(u"<em>%s 님이 나가셨습니다.</em>" % self.clients[socket]["name"])
        self.clients.pop(socket)

    def readData(self):
        socket = self.sender()
        line = socket.readLine().data().decode("utf-8")
        cmd, value = line.split(" ", 1)
        if cmd == "login":
            if self.Exist(value):
                name = self.clients[socket]["name"]
                self.send(socket, u"<em>이름이 이미 존재합니다. 자동으로 설정합니다...</em>")
            else:
                name = value
                self.clients[socket]["name"] = name
            self.sendAll(u"<em>%s 님이 들어왔습니다.</em>" % name)
        elif cmd == "say":
            message = "<%s> : %s" % (self.clients[socket]["name"], value)
            self.sendAll(message)

    def send(self, socket, message):
        socket.write(message.encode("utf-8"))

    def sendAll(self, message):
        for c in self.clients:
            self.send(c, message)

    def Exist(self, name):
        for c in self.clients:
            if name == self.clients[c]["name"]:
                return True

if __name__ == '__main__':

    import sys, signal
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = QtCore.QCoreApplication(sys.argv)
    #QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("eucKR"))
    serv = Server()
    port = 8080
    serv.listen(port=port)
    print("The server is running with port %d" % port)
    sys.exit(app.exec_())
