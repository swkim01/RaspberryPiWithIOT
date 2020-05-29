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
    if len(sys.argv) < 2:
        print("please input the following command:")
        print("$ python uiload.py xxx.ui")
        sys.exit(0)
    loader = QtUiTools.QUiLoader()
    ui = loader.load(sys.argv[1])
    child = ui.findChild(QtWidgets.QWidget, "connectButton")
    child.clicked.connect(ui.close)
    ui.show()
    sys.exit(app.exec_())
