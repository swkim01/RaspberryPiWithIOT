#!/usr/bin/python

import sys
from PySide import QtCore, QtGui, QtSql

def initModel(model):
    model.setTable("student")
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.select()

    model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "birth")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "gender")

    for i in range(model.rowCount()):
        print(model.record(i))

def connectDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test.db')

    if not db.open():
        return False

    return True

class SqliteWindow(QtGui.QWidget):
    def __init__(self, model):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Sqlite Window")
        self.setGeometry(300, 200, 480, 200)
        vbox = QtGui.QVBoxLayout(self)
        hbox = QtGui.QHBoxLayout()
        label = QtGui.QLabel("Query Filter", self)
        self.queryedit = QtGui.QLineEdit(self)
        table = QtGui.QTableView(self)
        self.model = model
        table.setModel(model)
        #table.resize(450, 200)
        hbox.addWidget(label)
        hbox.addWidget(self.queryedit)
        vbox.addLayout(hbox)
        vbox.addWidget(table)
        self.queryedit.returnPressed.connect(self.sendQuery)

    def sendQuery(self):
        text = self.queryedit.text()
        self.model.setFilter(text)
        self.model.select()

if __name__ == "__main__" :
    app = QtGui.QApplication(sys.argv)
    if not connectDB():
        print "Error opening to db"
        sys.exit(1)

    model = QtSql.QSqlTableModel()
    initModel(model)
    #model.setFilter("name like '%Im%'")

    sw = SqliteWindow(model)
    sw.show()
    sys.exit(app.exec_())
