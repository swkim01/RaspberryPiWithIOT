#!/usr/bin/python

import sys
from PySide import QtCore, QtGui

class ListWindow(QtGui.QWidget):
    def __init__(self, model):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("List Window")
        self.setGeometry(300, 200, 200, 200)
        listview = QtGui.QListView(self)
        self.model = model
        listview.setModel(model)

    def setList(self, model):
        for i in range(5):
            model.appendRow(QtGui.QStandardItem("This row number is {}".format(i)))

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    model = QtGui.QStandardItemModel()
    #model.setFilter("name like '%Im%'")

    lw = ListWindow(model)
    lw.setList(model)
    lw.show()
    sys.exit(app.exec_())
