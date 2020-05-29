import sys
from PySide2 import QtCore, QtWidgets, QtUiTools

#def loadUiWidget(uifilename, parent=None):
#    loader = QtUiTools.QUiLoader()
#    uifile = QtCore.QFile(uifilename)
#    uifile.open(QtCore.QFile.ReadOnly)
#    ui = loader.load(uifile, parent)
#    uifile.close()
#    return ui

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #ui = loadUiWidget("hello.ui")
    loader = QtUiTools.QUiLoader()
    ui = loader.load('./hello.ui')
    ui.show()
    sys.exit(app.exec_())
