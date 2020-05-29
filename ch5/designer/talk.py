# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'talk.ui',
# licensing of 'talk.ui' applies.
#
# Created: Wed Aug 28 17:42:07 2019
#      by: pyside2-uic  running on PySide2 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_TalkWindow(object):
    def setupUi(self, TalkWindow):
        TalkWindow.setObjectName("TalkWindow")
        TalkWindow.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(TalkWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setObjectName("connectButton")
        self.verticalLayout.addWidget(self.connectButton)
        self.talkMain = QtWidgets.QTextEdit(self.centralwidget)
        self.talkMain.setObjectName("talkMain")
        self.verticalLayout.addWidget(self.talkMain)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.messageEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.messageEdit.setObjectName("messageEdit")
        self.horizontalLayout.addWidget(self.messageEdit)
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        TalkWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TalkWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 19))
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        TalkWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TalkWindow)
        self.statusbar.setObjectName("statusbar")
        TalkWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(TalkWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(TalkWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), TalkWindow.close)
        QtCore.QMetaObject.connectSlotsByName(TalkWindow)

    def retranslateUi(self, TalkWindow):
        TalkWindow.setWindowTitle(QtWidgets.QApplication.translate("TalkWindow", "MainWindow", None, -1))
        self.connectButton.setText(QtWidgets.QApplication.translate("TalkWindow", "Connect", None, -1))
        self.sendButton.setText(QtWidgets.QApplication.translate("TalkWindow", "Send", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("TalkWindow", "File", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("TalkWindow", "Exit", None, -1))

