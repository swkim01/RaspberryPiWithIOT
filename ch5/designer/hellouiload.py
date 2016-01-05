import sys
from PySide import QtCore, QtGui, QtUiTools

#def loadUiWidget(uifilename, parent=None):
#    loader = QtUiTools.QUiLoader()
#    uifile = QtCore.QFile(uifilename)
#    uifile.open(QtCore.QFile.ReadOnly)
#    ui = loader.load(uifile, parent)
#    uifile.close()
#    return ui

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #ui = loadUiWidget("hello.ui")
    loader = QtUiTools.QUiLoader()
    ui = loader.load('./hello.ui')
    ui.show()
    sys.exit(app.exec_())
