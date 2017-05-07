from PyQt4 import QtGui,QtCore,Qt
from ui_klantenbeheer import Ui_MainWindow
from nieuweklantdialog import NieuweklantDialog
import sys
from commfunctions import *


class KlantenBeheerWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.connect(self.actionVernieuwen, QtCore.SIGNAL("triggered()"), self.showKlanten)
        self.connect(self.actionWijzigingen_doorvoeren, QtCore.SIGNAL("triggered()"), self.updateDB)
        self.connect(self.tableWidget, QtCore.SIGNAL("cellChanged(int,int)"),self.userUpdatesCell)    
        self.changedrecords=[]
        self.listoaded=0
        self.showKlanten()

    
    def addClient(self,):
        d=NieuweklantDialog(self)
        d.setId(self.getIdProposal())
        d.exec_()
     
    def getIdProposal(self): 
        if self.listoaded==1:
            return self.tableWidget.item(self.tableWidget.rowCount()-1, 0).text()
        else:
            return 0
        
    def updateDB(self):
        toremove=[]
        if(len(self.changedrecords)==0):
            return
        #QtGui.QApplication.setOverrideCursor(QtGui.QCursor(Qt.waitCursor));
        for rownr in self.changedrecords:
            # get the contents
            current=Klant()
            current.nr=self.checkId(self.tableWidget.item(rownr,0).text())
            current.klant=self.paddText(self.tableWidget.item(rownr,1).text(),40)
            current.adres=self.paddText(self.tableWidget.item(rownr,2).text(),40)
            current.gemeente=self.paddText(self.tableWidget.item(rownr,3).text(),40)
            current.u1=self.paddText(self.tableWidget.item(rownr,4).text(),40)
            current.telefoon=self.paddText(self.tableWidget.item(rownr,5).text(),15)
            current.gsm=self.paddText(self.tableWidget.item(rownr,6).text(),15)
            current.rekeningnr=self.paddText(self.tableWidget.item(rownr,7).text(),15)
            current.u2=self.paddText(self.tableWidget.item(rownr,8).text(),6)
            current.u3=self.paddText(self.tableWidget.item(rownr,9).text(),6)
            current.u4=self.paddText(self.tableWidget.item(rownr,10).text(),4)
            # send to server
            try:
                result=upload(current)
            except:
                QtGui.QMessageBox.critical(self,"Error","The server was not found. Is it running?")
                return
            if result>0: # an error occured
                QtGui.QMessageBox.warning(self,"Warning","The last client could not be updated. His id was not found in the database")
                #QtGui.QApplication.restoreOverrideCursor();
                return
            # remove from list
            toremove.append(rownr)
            # uncolor the row
            for i in range(0,10):
                self.tableWidget.item(rownr,i).setBackground(QtGui.QBrush(QtGui.QColor(QtCore.Qt.white)))
        # remove from list
        for rownr in toremove:
            self.changedrecords.remove(rownr)
        #QtGui.QApplication.restoreOverrideCursor();
        return
    
    def checkId(self,id):
        while(len(id)<5):
            id='0'+id
        return id
            
    def paddText(self,text,length):
        text=text[0:length]
        while(len(text) < length):
             text=text+' '
        print(len(text))
        print(repr(text))
        return text
                
    def keyPressEvent(self, event):
     if event.key() == QtCore.Qt.Key_Escape:
         self.close()
         
    def addCLientWithData(self, d):
         # get the contents
            current=Klant()
            current.nr=self.checkId(d[0])
            current.klant=self.paddText(d[1], 40)
            current.adres=self.paddText(d[2],40)
            current.gemeente=self.paddText(d[3],40)
            current.u1=self.paddText(d[4], 40)
            current.telefoon=self.paddText(d[5], 15)
            current.gsm=self.paddText(d[6],15)
            current.rekeningnr=self.paddText(d[7],15)
            current.u2=self.paddText(d[8],6)
            current.u3=self.paddText(d[9],6)
            current.u4=self.paddText(d[10],4)
            # send to server
            try:
                result=insert(current)
                # update the list
                self.showKlanten()
            except:
                QtGui.QMessageBox.critical(self,"Error","The server was not found. Is it running?")
        
    def userUpdatesCell(self, *args):
        if(self.loading!=1):
            row=args[0]
            if(self.changedrecords.count(row)>0):
                return
            column=args[1]
            self.changedrecords.append(row)
            # color the row
            for i in range(0,10):
                self.tableWidget.item(row,i).setBackground(QtGui.QBrush(QtGui.QColor(QtCore.Qt.yellow)))
       
    def showKlanten(self):
        self.loading=1
        klanten=self.getData()
        if klanten is not None:
            self.setKlantenList(klanten)
            self.tableWidget.resizeColumnsToContents()
            self.listoaded=1
        self.loading=0
        
    def getData(self):
        try:
            klanten=getKlantenList()
        except:
            QtGui.QMessageBox.critical(self,"Error","The server was not found. Is it running?")
            return
        return klanten
    
    def setKlantenList(self,klantenlist):
        # first, clear the table
        self.tableWidget.clearContents()
        for i in range(0,self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        # fill in the data
        row=0
        for klant in klantenlist:
            # create row
            self.tableWidget.setRowCount(row+1)
            # populate
            self.tableWidget.setItem(row,0,QtGui.QTableWidgetItem(klant.nr.rstrip()))
            self.tableWidget.setItem(row,1,QtGui.QTableWidgetItem(klant.klant.rstrip()))
            self.tableWidget.setItem(row,2,QtGui.QTableWidgetItem(klant.adres.rstrip()))
            self.tableWidget.setItem(row,3,QtGui.QTableWidgetItem(klant.gemeente.rstrip()))
            self.tableWidget.setItem(row,4,QtGui.QTableWidgetItem(klant.u1.rstrip()))
            self.tableWidget.setItem(row,5,QtGui.QTableWidgetItem(klant.telefoon.rstrip()))
            self.tableWidget.setItem(row,6,QtGui.QTableWidgetItem(klant.gsm.rstrip()))
            self.tableWidget.setItem(row,7,QtGui.QTableWidgetItem(klant.rekeningnr.rstrip()))
            self.tableWidget.setItem(row,8,QtGui.QTableWidgetItem(klant.u2.rstrip()))
            self.tableWidget.setItem(row,9,QtGui.QTableWidgetItem(klant.u3.rstrip()))
            self.tableWidget.setItem(row,10,QtGui.QTableWidgetItem(klant.u4.rstrip()))
            row=row+1

