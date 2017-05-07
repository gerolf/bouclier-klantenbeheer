import sys, socket, time
from PyQt4 import QtGui,QtCore

from klantenbeheerwindow import KlantenBeheerWindow
from commfunctions import *

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    window = KlantenBeheerWindow()
    window.show()
    app.exec_()


