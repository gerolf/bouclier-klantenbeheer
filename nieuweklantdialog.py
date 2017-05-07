from PyQt4 import QtGui,QtCore,Qt
from ui_nieuweklant import Ui_Dialog
import sys


class NieuweklantDialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, mainwindow):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.parent=mainwindow
    
    def setId(self, nr):
        strnr = repr(str(nr))
        strnr=eval(strnr)
        nr=(strnr.lstrip('0'))
        nr=eval(nr)
        nr=nr+1
        self.lineEdit.setText(str(nr))
        self.lineEdit_2.setFocus()

    def accept(self):
        # checks
        try:
            eval(str(self.lineEdit.text()))
        except:
            QtGui.QMessageBox.critical(self,"Error","The ID needs to be a number")
            return 
        data=[]
        data.append(self.lineEdit.text())
        data.append(self.lineEdit_2.text())
        data.append(self.lineEdit_3.text())
        data.append(self.lineEdit_4.text())
        data.append(self.lineEdit_5.text())
        data.append(self.lineEdit_6.text())
        data.append(self.lineEdit_7.text())
        data.append(self.lineEdit_8.text())
        data.append(self.lineEdit_9.text())
        data.append(self.lineEdit_10.text())
        data.append(self.lineEdit_11.text())
        self.parent.addCLientWithData(data)
        QtGui.QDialog.accept(self)
