# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CarParkQtDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 508)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 10, 661, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(52, 101, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(True)
        self.label1.setObjectName("label1")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 90, 13))
        self.label_6.setObjectName("label_6")
        self.make = QtWidgets.QLineEdit(self.centralwidget)
        self.make.setGeometry(QtCore.QRect(120, 160, 113, 20))
        self.make.setObjectName("make")
        self.firstRecord = QtWidgets.QPushButton(self.centralwidget)
        self.firstRecord.setGeometry(QtCore.QRect(30, 440, 120, 23))
        self.firstRecord.setObjectName("firstRecord")
        self.databaseView = QtWidgets.QTableWidget(self.centralwidget)
        self.databaseView.setGeometry(QtCore.QRect(30, 241, 511, 181))
        self.databaseView.setObjectName("databaseView")
        self.databaseView.setColumnCount(4)
        self.databaseView.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.databaseView.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.databaseView.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.databaseView.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.databaseView.setHorizontalHeaderItem(3, item)
        self.nextRecord = QtWidgets.QPushButton(self.centralwidget)
        self.nextRecord.setGeometry(QtCore.QRect(160, 440, 120, 23))
        self.nextRecord.setObjectName("nextRecord")
        self.previousRecord = QtWidgets.QPushButton(self.centralwidget)
        self.previousRecord.setGeometry(QtCore.QRect(290, 440, 120, 23))
        self.previousRecord.setObjectName("previousRecord")
        self.lastRecord = QtWidgets.QPushButton(self.centralwidget)
        self.lastRecord.setGeometry(QtCore.QRect(420, 440, 120, 23))
        self.lastRecord.setObjectName("lastRecord")
        self.staffCars = QtWidgets.QPushButton(self.centralwidget)
        self.staffCars.setGeometry(QtCore.QRect(550, 280, 111, 23))
        self.staffCars.setObjectName("staffCars")
        self.studentCars = QtWidgets.QPushButton(self.centralwidget)
        self.studentCars.setGeometry(QtCore.QRect(550, 330, 111, 23))
        self.studentCars.setObjectName("studentCars")
        self.visitorCars = QtWidgets.QPushButton(self.centralwidget)
        self.visitorCars.setGeometry(QtCore.QRect(550, 380, 111, 23))
        self.visitorCars.setObjectName("visitorCars")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 90, 13))
        self.label_3.setObjectName("label_3")
        self.model = QtWidgets.QLineEdit(self.centralwidget)
        self.model.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.model.setObjectName("model")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 200, 90, 16))
        self.label_7.setObjectName("label_7")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(120, 80, 113, 20))
        self.name.setObjectName("name")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 120, 90, 16))
        self.label_5.setObjectName("label_5")
        self.registration = QtWidgets.QLineEdit(self.centralwidget)
        self.registration.setGeometry(QtCore.QRect(120, 120, 113, 20))
        self.registration.setObjectName("registration")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(330, 70, 150, 150))
        self.picture.setObjectName("picture")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 684, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Collyers Car Parking"))
        self.label1.setText(_translate("MainWindow", "Collyers Car Park"))
        self.label_6.setText(_translate("MainWindow", "Make"))
        self.firstRecord.setText(_translate("MainWindow", "First Record"))
        item = self.databaseView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date"))
        item = self.databaseView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.databaseView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Registration"))
        item = self.databaseView.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Model"))
        self.nextRecord.setText(_translate("MainWindow", "Next Record"))
        self.previousRecord.setText(_translate("MainWindow", "Previous Record"))
        self.lastRecord.setText(_translate("MainWindow", "Last Record"))
        self.staffCars.setText(_translate("MainWindow", "Staff Cars"))
        self.studentCars.setText(_translate("MainWindow", "Student Cars"))
        self.visitorCars.setText(_translate("MainWindow", "Visitor Cars"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_7.setText(_translate("MainWindow", "Model"))
        self.label_5.setText(_translate("MainWindow", "Registration"))
        self.picture.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Photo</p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())