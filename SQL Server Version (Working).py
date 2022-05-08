import pyodbc
import sys

from PyQt5.QtWidgets import *
from CarParkQtDesigner import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

"""
 Create the Database on the server using Microsoft SQL Server Management Studio.

 Create the table:
   CREATE TABLE tCarPark (
    REG varchar(7) PRIMARY KEY NOT NULL,
    NAMES varchar(255) NOT NULL,
    MODEL varchar(255) NOT NULL,
	MAKE varchar(255) NOT NULL,
	EXPIRE_DATE varchar(10) NOT NULL,
	PERMIT_TYPE int NOT NULL,
   );

Add records:
INSERT INTO tCarPark(REG,NAMES,MODEL,MAKE,EXPIRE_DATE,PERMIT_TYPE)
VALUES(...)
"""

College = False
cs = ""
# https://github.com/mkleehammer/pyodbc/wiki/Connecting-to-SQL-Server-from-Windows
# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver15
# Try commenting out Trusted_Connection
if College:
    cs = (
       "Driver={SQL Server};" # deprecated
        "Server=svr-cmp-01;"
        "Database=21DixonSE86;"
        "Trusted_Connection=yes;" # try removing as you specify UID and pwd
        "UID=COLLYERS\21DixonSE86;"
        "pwd=galaxy"
        )
else:
    cs = (
        "Driver={ODBC Driver 17 for SQL Server};" # SQL server 2008 to 2019
        "Server=MSI-SUSIE;"
        "Database=21DixonSE86;"
        "Trusted_Connection=yes;"
        #"UID=COLLYERS\21DixonSE86;"
        #"pwd=galaxy"
        )

# columns in qtableview
dateCol = 0
nameCol = 1
regCol = 2
modelCol = 3
makeCol = 4
permitCol = 5

# permit_type
student = 1
visitor = 2
staff = 3


class Window(QMainWindow, Ui_MainWindow):
    regText = ""
    makeText = ""
    modelText = ""
    nameText = ""
    currentLine = 0
    cnxn = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.connectSignalsSlots()
        self.populateTable()

    def populateTable(self):
        # open database
        statementSQL = "SELECT * from tCarPark"
        try:
            self.cnxn = pyodbc.connect(cs)
            print("Connected")

            if self.cnxn is not None:
                cursor = self.cnxn.cursor()
                cursor.execute(statementSQL)
                row = cursor.fetchone()
                print(row)
                self.make.setText(str(row[0]))
                self.model.setText(str(row[1]))
                self.name.setText(str(row[2]))
                self.registration.setText(str(row[3]))

        except pyodbc.DatabaseError as err:
            print("Error: ")
            print(err)
            self.databaseView.clearContents()
            exit(1)
            #print(e)

        self.cnxn.close()
        self.cnxn = pyodbc.connect(cs)

        # query the table for the data in a row
        cursor = self.cnxn.execute("SELECT EXPIRE_DATE, names, reg, model, make, permit_type from tCarPark").fetchall()
    
        self.updateTable(self.cnxn, cursor, "SELECT COUNT() FROM tCarPark")

        self.cnxn.close()

    def updateTable(self, conn, cursor, countString):
        self.databaseView.clear()

        # SQLLite the rowcount is usually -1. SQL Server the rowcount is the number of selected records
        rowCount = len(cursor)
        numRecords = "SELECT COUNT() FROM tCarPark"
        if rowCount == -1:
            # count the number of records
            rowCount = conn.execute(numRecords).fetchone()[0]
        self.databaseView.setRowCount(rowCount)
        print("rowcount = " + str(rowCount))

        # iterate over the contents of the database and stuff into the databaseView.
        count = 0
        for row in cursor:
            # each number matches the order in the execute abovw
            item = QTableWidgetItem(str(row[0]))
            self.databaseView.setItem(count, 0, item)
            self.databaseView.setItem(count, 1, QTableWidgetItem(str(row[1])))
            self.databaseView.setItem(count, 2, QTableWidgetItem(str(row[2])))
            self.databaseView.setItem(count, 3, QTableWidgetItem(str(row[3])))
            self.databaseView.setItem(count, 4, QTableWidgetItem(str(row[4])))
            self.databaseView.setItem(count, 5, QTableWidgetItem(str(row[5])))
            count += 1

        # Table will fit the screen horizontally
        self.databaseView.resizeColumnsToContents()
        self.databaseView.resizeRowsToContents()
        self.databaseView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.currentLine = 0
        self.loadDisplay()

    def connectSignalsSlots(self):
        self.staffCars.clicked.connect(self.staffCarsClicked)
        self.studentCars.clicked.connect(self.studentCarsClicked)
        self.visitorCars.clicked.connect(self.visitorCarsClicked)
        self.firstRecord.clicked.connect(self.firstRecordClicked)
        self.nextRecord.clicked.connect(self.nextRecordClicked)
        self.previousRecord.clicked.connect(self.previousRecordClicked)
        self.lastRecord.clicked.connect(self.lastRecordClicked)
        self.registration.returnPressed.connect(self.registrationEnter)
        self.model.returnPressed.connect(self.modelEnter)
        self.make.returnPressed.connect(self.makeEnter)
        self.name.returnPressed.connect(self.nameEnter)

    def staffCarsClicked(self):
        # staff = 1
        # open database
        self.cnxn = pyodbc.connect(cs)
        # query the table for the data in a row
        cursor = self.cnxn.execute("SELECT EXPIRE_DATE, names, reg, model, make, permit_type from tCarPark WHERE PERMIT_TYPE = 1;").fetchall()
        self.updateTable(self.cnxn, cursor, "SELECT COUNT() FROM tCarPark WHERE PERMIT_TYPE = 1")
        self.cnxn.close()


    def studentCarsClicked(self):
        # student = 2
        # query the table for the data in a row
        self.cnxn = pyodbc.connect(cs)
        cursor = self.cnxn.execute("SELECT EXPIRE_DATE, names, reg, model, make, permit_type from tCarPark WHERE PERMIT_TYPE = 2;").fetchall()
        self.updateTable(self.cnxn, cursor, "SELECT COUNT() FROM tCarPark WHERE PERMIT_TYPE = 2")
        self.cnxn.close()

    def visitorCarsClicked(self):
        print("visitorCars")
        # visitor = 3
        # query the table for the data in a row
        self.cnxn = pyodbc.connect(cs)
        cursor = self.cnxn.execute("SELECT EXPIRE_DATE, names, reg, model, make, permit_type from tCarPark WHERE PERMIT_TYPE = 3;").fetchall()
        self.updateTable(self.cnxn, cursor, "SELECT COUNT() FROM tCarPark WHERE PERMIT_TYPE = 3")
        self.cnxn.close()


    def firstRecordClicked(self):
        self.currentLine = 0
        self.loadDisplay()

    def loadDisplay(self):
        # dateCol, nameCol, regCol, modelCol, makeCol, permitCol
        nameFromTable = self.databaseView.item(self.currentLine, nameCol)
        self.name.setText(nameFromTable.text())
        regFromTable = self.databaseView.item(self.currentLine, regCol)
        self.registration.setText(regFromTable.text())
        modelFromTable = self.databaseView.item(self.currentLine, modelCol)
        self.model.setText(modelFromTable.text())


    def nextRecordClicked(self):
        self.currentLine += 1
        if self.currentLine >= self.databaseView.rowCount():
            self.currentLine = 0
        self.loadDisplay()

    def previousRecordClicked(self):
        self.currentLine -= 1
        if self.currentLine < 0:
            self.currentLine = 0
        self.loadDisplay()

    def lastRecordClicked(self):
        self.currentLine = self.databaseView.rowCount() - 1
        self.loadDisplay()

    def registrationEnter(self):
        regText = self.registration.text()
        print(regText)

    def nameEnter(self):
        nameText = self.names.text()
        print(nameText)

    def makeEnter(self):
        makeText = self.make.text()
        print(makeText)

    def modelEnter(self):
        modelText = self.model.text()
        print(modelText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    ret = app.exec()
    sys.exit(ret)