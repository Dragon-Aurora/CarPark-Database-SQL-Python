import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from CarParkQtDesigner import Ui_MainWindow
from urllib.request import pathname2url
import sqlite3

# Name of database
db = r'carparkdb.sqlite'

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
    seatBooking = SeatBooking()
    regText = ""
    makeText = ""
    modelText = ""
    nameText = ""
    currentLine = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.connectSignalsSlots()
        self.populateTable()

    def populateTable(self):
        # open database
        dburi = 'file:{}?mode=rw'.format(pathname2url(db))
        conn = sqlite3.connect(dburi, uri=True)

        # query the table for the data in a row
        cursor = conn.execute("SELECT EXPIRE_DATE, name, reg, model, make, permit_type from CARPARK")

        self.updateTable(conn, cursor, "SELECT COUNT() FROM CARPARK")

    def updateTable(self, conn, cursor, countString):
        self.databaseView.clear()

        # SQLLite the rowcount is usually -1. SQL Server the rowcount is the number of selected records
        rowCount = int(cursor.rowcount)
        if rowCount == -1:
            # count the number of records
            rowCount = conn.execute(countString).fetchone()[0]
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
            count += 1

            # self.databaseView.setItem(count, 4, QTableWidgetItem(str(row[4])))
            # self.databaseView.setItem(count, 5, QTableWidgetItem(str(row[5])))

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
        dburi = 'file:{}?mode=rw'.format(pathname2url(db))
        conn = sqlite3.connect(dburi, uri=True)

        # query the table for the data in a row
        # https://www.sqlitetutorial.net/sqlite-where/
        cursor = conn.execute("SELECT EXPIRE_DATE, name, reg, model, make, permit_type from CARPARK WHERE PERMIT_TYPE = 1;")
        self.updateTable(conn, cursor, "SELECT COUNT() FROM CARPARK WHERE PERMIT_TYPE = 1")

    def studentCarsClicked(self):
        # student = 2
        # open database
        dburi = 'file:{}?mode=rw'.format(pathname2url(db))
        conn = sqlite3.connect(dburi, uri=True)

        # query the table for the data in a row
        # https://www.sqlitetutorial.net/sqlite-where/
        cursor = conn.execute("SELECT EXPIRE_DATE, name, reg, model, make, permit_type from CARPARK WHERE PERMIT_TYPE = 2;")
        self.updateTable(conn, cursor, "SELECT COUNT() FROM CARPARK WHERE PERMIT_TYPE = 2")

    def visitorCarsClicked(self):
        print("visitorCars")
        # visitor = 3
        # open database
        dburi = 'file:{}?mode=rw'.format(pathname2url(db))
        conn = sqlite3.connect(dburi, uri=True)

        # query the table for the data in a row
        # https://www.sqlitetutorial.net/sqlite-where/
        cursor = conn.execute("SELECT EXPIRE_DATE, name, reg, model, make, permit_type from CARPARK WHERE PERMIT_TYPE = 3;")
        self.updateTable(conn, cursor, "SELECT COUNT() FROM CARPARK WHERE PERMIT_TYPE = 3")

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
        nameText = self.name.text()
        print(nameText)

    def makeEnter(self):
        makeText = self.make.text()
        print(makeText)

    def modelEnter(self):
        modelText = self.model.text()
        print(modelText)


# Ref: https://www.tutorialspoint.com/sqlite/sqlite_python.htm
#
# Walthrough of simple app that uses a DB and QTableWidget
# YouTube: https://www.youtube.com/playlist?list=PLs3IFJPw3G9KZsqOj8vS_9KGApyxpGN5f
# Source: https://github.com/codefirstio/PyQt5-Daily-Task-Planner-App
#
if __name__ == "__main__":
    try:
        dburi = 'file:{}?mode=rw'.format(pathname2url(db))
        conn = sqlite3.connect(dburi, uri=True)
    except sqlite3.OperationalError:
        # handle missing database case

        # open and create
        conn = sqlite3.connect(db)

        # create table
        conn.execute('''CREATE TABLE CARPARK
                 (REG TEXT PRIMARY KEY     NOT NULL,
                 NAME           TEXT    NOT NULL,
                 MODEL           TEXT     NOT NULL,
                 EXPIRE_DATE        TEXT NOT NULL,
                 MAKE         TEXT NOT NULL,
                 PERMIT_TYPE         INT);''')
        print("Table created successfully");


        # add some stuff (using SQL) to db.
        conn.execute("INSERT INTO CARPARK (REG,NAME,MODEL,EXPIRE_DATE,MAKE,PERMIT_TYPE) \
              VALUES ('GX64KGP', 'Damian Dixon', 'Auris', '12/12/2040', 'Toyota', 1 )")
        conn.execute("INSERT INTO CARPARK (REG,NAME,MODEL,EXPIRE_DATE,MAKE,PERMIT_TYPE) \
              VALUES ('GX64KGB', 'Damian', 'Auris', '12/12/2035', 'Toyota', 3 )")
        conn.execute("INSERT INTO CARPARK (REG,NAME,MODEL,EXPIRE_DATE,MAKE,PERMIT_TYPE) \
              VALUES ('GX77KGP', 'Laura Dixon', 'SUV', '12/12/2045', 'Ford', 2 )")
        conn.execute("INSERT INTO CARPARK (REG,NAME,MODEL,EXPIRE_DATE,MAKE,PERMIT_TYPE) \
              VALUES ('GX36KGB', 'Susie', 'Model 3', '12/12/2035', 'Tesla', 3 )")

        # save it
        conn.commit()

    print("Opened database successfully");
    conn.close()



    app = QApplication(sys.argv)
    win = Window()
    win.show()
    ret = app.exec()
    sys.exit(ret)
