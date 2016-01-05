# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talk.ui'
#
# Created: Wed Jul 22 21:01:52 2015
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TalkWindow(object):
    def setupUi(self, TalkWindow):
        TalkWindow.setObjectName("TalkWindow")
        TalkWindow.resize(300, 300)
        self.centralwidget = QtGui.QWidget(TalkWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.connectButton = QtGui.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.verticalLayout.addWidget(self.connectButton)
        self.talkMain = QtGui.QTextEdit(self.centralwidget)
        self.talkMain.setObjectName("talkMain")
        self.verticalLayout.addWidget(self.talkMain)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageEdit = QtGui.QLineEdit(self.centralwidget)
        self.messageEdit.setObjectName("messageEdit")
        self.horizontalLayout.addWidget(self.messageEdit)
        self.sendButton = QtGui.QPushButton(self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        TalkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TalkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 19))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TalkWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TalkWindow)
        self.statusbar.setObjectName("statusbar")
        TalkWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(TalkWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(TalkWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("activated()"), TalkWindow.close)
        QtCore.QMetaObject.connectSlotsByName(TalkWindow)

    def retranslateUi(self, TalkWindow):
        TalkWindow.setWindowTitle(QtGui.QApplication.translate("TalkWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.connectButton.setText(QtGui.QApplication.translate("TalkWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.sendButton.setText(QtGui.QApplication.translate("TalkWindow", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("TalkWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("TalkWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

