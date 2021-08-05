# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmailFile(1).ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
import pandas as pd
import datetime

class Ui_MainWindow(object):
    file = ""
    companyFile = ""
    removedEmails = 0
    todays_date = datetime.datetime.now().date()
    index = pd.date_range(todays_date-datetime.timedelta(10), periods=10, freq='D')

    columns = ['A','B', 'C']
    data = pd.DataFrame(index=index, columns=columns)
    companyData = pd.DataFrame(index=index, columns=columns)
    data = data.fillna(0)
    companyData.fillna(0)
    companyNamesArray = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1156, 750)
        MainWindow.setMinimumSize(QtCore.QSize(0, 750))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 750))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 750))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(350, 40, 771, 591))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_24 = QtWidgets.QLabel(self.page)
        self.label_24.setGeometry(QtCore.QRect(10, 390, 201, 51))
        self.label_24.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_24.setObjectName("label_24")
        self.label_21 = QtWidgets.QLabel(self.page)
        self.label_21.setGeometry(QtCore.QRect(10, 120, 201, 51))
        self.label_21.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_21.setObjectName("label_21")
        self.label_25 = QtWidgets.QLabel(self.page)
        self.label_25.setGeometry(QtCore.QRect(320, 390, 201, 51))
        self.label_25.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_25.setObjectName("label_25")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(290, 340, 171, 41))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    font-size: 15px;\n"
"    border-radius: 15px;\n"
"    border: solid 2px #ce7910;\n"
"    color: white;\n"
"    padding: 5px 5px;\n"
"    background-color: rgb(18, 21, 52);\n"
"    box-shadow: 0px 10px 14px -7px #616174;\n"
"    font-family: Arial;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(15, 25, 40);\n"
"}\n"
"QPushButton:active {\n"
"    position: relative;\n"
"    top: 1px;\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.removeEmail)
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(270, 120, 450, 51))
        self.label_18.setStyleSheet("color: #7a7c7f; font-size: 15px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_18.setObjectName("label_18")
        self.label_22 = QtWidgets.QLabel(self.page)
        self.label_22.setGeometry(QtCore.QRect(10, 250, 201, 51))
        self.label_22.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.page)
        self.label_23.setGeometry(QtCore.QRect(300, 250, 201, 51))
        self.label_23.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_23.setObjectName("label_23")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 130, 41, 41))
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/face/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.setLocation)
        self.label_27 = QtWidgets.QLabel(self.page)
        self.label_27.setGeometry(QtCore.QRect(10, 190, 201, 51))
        self.label_27.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.page)
        self.label_28.setGeometry(QtCore.QRect(300, 190, 201, 51))
        self.label_28.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.page)
        self.label_29.setGeometry(QtCore.QRect(10, 460, 201, 51))
        self.label_29.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.page)
        self.label_30.setGeometry(QtCore.QRect(320, 460, 201, 51))
        self.label_30.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_30.setObjectName("label_30")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_26 = QtWidgets.QLabel(self.page_2)
        self.label_26.setGeometry(QtCore.QRect(10, 130, 201, 51))
        self.label_26.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_26.setObjectName("label_26")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_10.setGeometry(QtCore.QRect(530, 390, 171, 41))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
"    font-size: 12px;\n"
"    border-radius: 15px;\n"
"    border: solid 2px #ce7910;\n"
"    color: white;\n"
"    padding: 5px 5px;\n"
"    background-color: rgb(18, 21, 52);\n"
"    box-shadow: 0px 10px 14px -7px #616174;\n"
"    font-family: Arial;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(15, 25, 40);\n"
"}\n"
"QPushButton:active {\n"
"    position: relative;\n"
"    top: 1px;\n"
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.cleanCompanyName)
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(270, 130, 450, 51))
        self.label_19.setStyleSheet("color: #7a7c7f; font-size: 15px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_19.setObjectName("label_19")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_12.setGeometry(QtCore.QRect(570, 140, 41, 41))
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setIconSize(QtCore.QSize(22, 22))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.setCompanyLocation)
        self.label_31 = QtWidgets.QLabel(self.page_2)
        self.label_31.setGeometry(QtCore.QRect(10, 220, 201, 51))
        self.label_31.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_31.setObjectName("label_31")
        self.textEdit = QtWidgets.QTextEdit(self.page_2)
        self.textEdit.setGeometry(QtCore.QRect(240, 220, 271, 51))
        self.textEdit.setStyleSheet("font: 14pt \"Arial\";")
        self.textEdit.setObjectName("textEdit")
        self.AddButton = QtWidgets.QPushButton(self.page_2)
        self.AddButton.setGeometry(QtCore.QRect(530, 230, 101, 41))
        self.AddButton.setStyleSheet("QPushButton{\n"
"    font-size: 12px;\n"
"    border-radius: 15px;\n"
"    border: solid 2px #ce7910;\n"
"    color: white;\n"
"    padding: 5px 5px;\n"
"    background-color: rgb(18, 21, 52);\n"
"    box-shadow: 0px 10px 14px -7px #616174;\n"
"    font-family: Arial;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(15, 25, 40);\n"
"}\n"
"QPushButton:active {\n"
"    position: relative;\n"
"    top: 1px;\n"
"}")
        self.AddButton.setObjectName("AddButton")
        self.AddButton.clicked.connect(self.addToList)
        self.label_32 = QtWidgets.QLabel(self.page_2)
        self.label_32.setGeometry(QtCore.QRect(10, 70, 201, 51))
        self.label_32.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.label_32.setObjectName("label_32")
        self.TotalRemoved = QtWidgets.QLabel(self.page_2)
        self.TotalRemoved.setGeometry(QtCore.QRect(210, 70, 201, 51))
        self.TotalRemoved.setStyleSheet("color: #7a7c7f; font-size: 20px; font-family: \"Libre Baskerville\", serif; line-height: 45px; text-align: center; text-shadow: 0 1px 1px #fff; padding-top: 20px; ")
        self.TotalRemoved.setObjectName("TotalRemoved")
        self.tableWidget = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget.setGeometry(QtCore.QRect(190, 290, 321, 281))
        self.tableWidget.setRowCount(1)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.RemoveButton = QtWidgets.QPushButton(self.page_2)
        self.RemoveButton.setGeometry(QtCore.QRect(530, 290, 101, 41))
        self.RemoveButton.setStyleSheet("QPushButton{\n"
"    font-size: 12px;\n"
"    border-radius: 15px;\n"
"    border: solid 2px #ce7910;\n"
"    color: white;\n"
"    padding: 5px 5px;\n"
"    background-color: rgb(18, 21, 52);\n"
"    box-shadow: 0px 10px 14px -7px #616174;\n"
"    font-family: Arial;\n"
"    cursor: pointer;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(15, 25, 40);\n"
"}\n"
"QPushButton:active {\n"
"    position: relative;\n"
"    top: 1px;\n"
"}")
        self.RemoveButton.setObjectName("RemoveButton")
        self.RemoveButton.clicked.connect(self.removeFromList)
        self.stackedWidget.addWidget(self.page_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 301, 778))
        self.widget.setMinimumSize(QtCore.QSize(0, 755))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 778))
        self.widget.setStyleSheet("background-color: rgb(18, 21, 52)")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(0, 240, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("     QPushButton {\n"
"               color: white;\n"
"               font: 17pt;\n"
"               border: 0px solid orange;\n"
"               padding: 5px;\n"
"                  border-radius: 3px;\n"
"               opacity: 200;\n"
"            text-align:left;\n"
"            \n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: white;\n"
"            color: black;\n"
"                border-style: inset;\n"
"\n"
"            }\n"
"            QPushButton:pressed {\n"
"            qproperty-icon: url(:/face/stamp.png);\n"
"                background-color: white;\n"
"                border-style: inset;\n"
"            }\n"
"\n"
"            ")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/face/contract.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(0, 300, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("     QPushButton {\n"
"               color: white;\n"
"               font: 17pt;\n"
"               border: 0px solid orange;\n"
"               padding: 5px;\n"
"                  border-radius: 3px;\n"
"               opacity: 200;\n"
"            text-align:left;\n"
"            \n"
"\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: white;\n"
"            color: black;\n"
"                border-style: inset;\n"
"\n"
"            }\n"
"            QPushButton:pressed {\n"
"            qproperty-icon: url(:/face/stamp.png);\n"
"                background-color: white;\n"
"                border-style: inset;\n"
"            }\n"
"\n"
"            ")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.widget.raise_()
        self.stackedWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        with open("file.txt","r") as f:
            l=[x[:-1] for x in f.readlines()]
        for i in l:
            print(i)
            rowPosition = self.tableWidget.rowCount()
            print("Position: ",rowPosition)
            
            self.tableWidget.insertRow(rowPosition)
            #self.tableWidget.insertColumn(0)
            self.tableWidget.setItem(rowPosition-1 , 0, QTableWidgetItem(i))
            self.tableWidget.setItem(rowPosition-1 , 1, QTableWidgetItem(str(0)))
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_24.setText(_translate("MainWindow", "Removed Emails"))
        self.label_21.setText(_translate("MainWindow", "File Location"))
        self.label_25.setText(_translate("MainWindow", "0"))
        self.pushButton_7.setText(_translate("MainWindow", "Remove Emails"))
        self.label_18.setText(_translate("MainWindow", "File Location"))
        self.label_22.setText(_translate("MainWindow", "Total Emails"))
        self.label_23.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "Total Leads"))
        self.label_28.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "Remaining Emails"))
        self.label_30.setText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "File Location"))
        self.pushButton_10.setText(_translate("MainWindow", "Clean Names"))
        self.label_19.setText(_translate("MainWindow", "File Location"))
        self.label_31.setText(_translate("MainWindow", "Remove Names"))
        self.AddButton.setText(_translate("MainWindow", "Add"))
        self.label_32.setText(_translate("MainWindow", "Total Removed"))
        self.TotalRemoved.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Item"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Removed"))
        self.RemoveButton.setText(_translate("MainWindow", "Remove"))
        self.pushButton.setText(_translate("MainWindow", "   Remove Emails"))
        self.pushButton_6.setText(_translate("MainWindow", "   Clean Company Name"))

    def setLocation(self, MainWindow):
        self.file = QFileDialog.getOpenFileName(QtWidgets.QMainWindow(), "Select Directory")[0]
        self.label_18.setText(self.file)
        self.data = pd.read_csv(self.file)
        self.label_28.setText(str(self.data.shape[0]))
        tempLengths = 0
        for i in range(0, self.data.shape[0]):
            print(i)
            if isinstance(self.data.iloc[i][3], str):
                chunks = self.data.iloc[i][3].split(',')
                tempLengths = tempLengths + len(chunks)
        self.label_23.setText(str(tempLengths))
    
    def setCompanyLocation(self, MainWindow):
        self.companyFile = QFileDialog.getOpenFileName(QtWidgets.QMainWindow(), "Select Directory")[0]
        self.label_19.setText(self.companyFile)
        self.companyData = pd.read_csv(self.companyFile)

        

    def removeEmail(self, MainWindow):
        tempLengths = 0
        for i in range(0, self.data.shape[0]):
            print(i)
            tempLengths = 0
            if isinstance(self.data.iloc[i][3], str):
                chunks = self.data.iloc[i][3].split(',')
                chunks = list(dict.fromkeys(chunks))
                print(chunks)
                print("Commas : ", chunks)
                email = ""
                tempLengths = len(chunks)
                self.label_25.setText(str(self.removedEmails))
                for j in range(len(chunks)):
                    if '@' + self.data.iloc[i][0] in chunks[j] and chunks[j][len(chunks[j])-1] == self.data.iloc[i][0][len(self.data.iloc[i][0])-1]:
                        tempLengths = tempLengths - 1
                        print("Found: ", chunks[j])
                        email = email + chunks[j] + ','
                self.data.iloc[i,self.data.columns.get_loc('Emails')] = email[:-1]
                        
                print()
                self.removedEmails = self.removedEmails + tempLengths
                
        self.data.to_csv('out.csv', index=False)
            #if(data.iloc[i][0] )
        print(self.data)
        msgBox = QMessageBox()
        msgBox.setText("Emails Removed")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        ret = msgBox.exec_()
        self.label_25.setText(str(self.removedEmails))
        self.label_30.setText(str(int(self.label_23.text()) - int(self.label_25.text())))
        

    def cleanCompanyName(self, MainWindow):
        self.companyNamesArray = []
        column = 0
        for row in range(self.tableWidget.rowCount()): 
            # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
            _item = self.tableWidget.item(row, column) 
            self.tableWidget.setItem(row , 1, QTableWidgetItem(str(0)))
            if _item:            
                item = self.tableWidget.item(row, column).text()
                self.companyNamesArray.append(item)
                print(f'row: {row}, column: {column}, item={item}')
        
        print(self.companyNamesArray)

        with open("file.txt","w") as f:
            for sub in self.companyNamesArray:
                f.write(sub)
                f.write('\n')
        #chunks = self.textEdit.toPlainText().split(',')
        chunks = self.companyNamesArray
        print("Length: ", len(chunks))
        for i in range (len(chunks)):
            if chunks[i][0] != ' ':
                chunks[i] = ' ' + chunks[i]
            if chunks[i][len(chunks[i])-1] != ' ':
                chunks[i] = chunks[i] + ' '
                
        print(chunks)
        
        for i in range(0, self.companyData.shape[0]):
            
        #     tempLengths = 0
            if isinstance(self.companyData.iloc[i][0], str):
                iterator = 0
                for j in chunks:
                    tempp = self.companyData.iloc[i][0]
                    self.companyData.iloc[i][0] = self.companyData.iloc[i][0].replace(j, '')
                    if(tempp != self.companyData.iloc[i][0]):
                        
                        temp = self.tableWidget.item(iterator, 1).text()
                        print("Temp: ", temp)
                        self.tableWidget.setItem(iterator , 1, QTableWidgetItem(str(int(temp)+1)))
                        temp = 0

                    iterator += 1
                    
        self.companyData.to_csv('CleanNames.csv', index=False)
        summ = 0
        for row in range(self.tableWidget.rowCount()): 
            # item(row, 0) Returns the item for the given row and column if one has been set; otherwise returns nullptr.
            _item = self.tableWidget.item(row, column) 

            if _item:            
                item = self.tableWidget.item(row, 1).text()
                summ = summ + int(item)
        self.TotalRemoved.setText(str(summ))
        msgBox = QMessageBox()
        msgBox.setText("Names Cleaned")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        ret = msgBox.exec_()
        
        
    def addToList(self):
        rowPosition = self.tableWidget.rowCount()
        print("Position: ",rowPosition)
        
        self.tableWidget.insertRow(rowPosition)
        #self.tableWidget.insertColumn(0)
        self.tableWidget.setItem(rowPosition-1 , 0, QTableWidgetItem(self.textEdit.toPlainText()))
        self.tableWidget.setItem(rowPosition-1 , 1, QTableWidgetItem(str(0)))
        self.textEdit.setText("")
    
    def removeFromList(self):
        print(self.tableWidget.selectedItems())
        self.tableWidget.removeRow(self.tableWidget.currentRow())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

