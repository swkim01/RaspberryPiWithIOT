#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

class DialogWindow(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setWindowTitle("Dialog Window")
        vbox = QtGui.QVBoxLayout(self)
        hbox1 = QtGui.QHBoxLayout()
        hbox2 = QtGui.QHBoxLayout()
        self.ok = QtGui.QPushButton("OK", self)
        self.cancel = QtGui.QPushButton("Cancel", self)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        hbox1.addWidget(QtGui.QLabel("Enter your name", self))
        self.lineedit = QtGui.QLineEdit(self)
        hbox1.addWidget(self.lineedit)
        hbox2.addWidget(self.ok)
        hbox2.addWidget(self.cancel)

        self.ok.clicked.connect(self.accept)
        self.cancel.clicked.connect(self.reject)

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    dg = DialogWindow()
    result = dg.exec_()
    if result == QtGui.QDialog.Accepted:
        print "your name is", dg.lineedit.text()
        #result = QtGui.QMessageBox.information(dg, "Query", "Are you sure?",
        #            QtGui.QMessageBox.Yes | QtGui.QMessageBox.Default,
        #            QtGui.QMessageBox.No)
        #if result == QtGui.QMessageBox.No:
        #    text = QtGui.QInputDialog.getText(dg, "Question",
        #            "Write your name again.", QtGui.QLineEdit.Normal)
    elif result == QtGui.QDialog.Rejected:
        print "Input canceled"
