#!/usr/bin/python3

import sys
from PySide2 import QtCore, QtWidgets, QtSql

def connectDB():
    db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test.db')

    if not db.open():
        return False

    return True

def initModel(model):
    model.setTable("student")
    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.select()

    model.setHeaderData(0, QtCore.Qt.Horizontal, "id")
    model.setHeaderData(1, QtCore.Qt.Horizontal, "name")
    model.setHeaderData(2, QtCore.Qt.Horizontal, "birth")
    model.setHeaderData(3, QtCore.Qt.Horizontal, "gender")

class SqliteWindow(QtWidgets.QWidget):
    def __init__(self, model):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Sqlite Window")
        self.setGeometry(300, 200, 480, 200)
        vbox = QtWidgets.QVBoxLayout(self)
        hbox = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel("Query Filter", self)
        self.queryedit = QtWidgets.QLineEdit(self)
        table = QtWidgets.QTableView(self)
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
    app = QtWidgets.QApplication(sys.argv)
    if not connectDB():
        print("Error opening to db")
        sys.exit(1)

    model = QtSql.QSqlTableModel()
    initModel(model)
    #for i in range(model.rowCount()):
    #    print(model.record(i))
    #model.setFilter("name like '%Im%'")

    sw = SqliteWindow(model)
    sw.show()
    sys.exit(app.exec_())
