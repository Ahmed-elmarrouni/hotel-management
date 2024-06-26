# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1816, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 30, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(51, 24, 255);")
        self.label.setObjectName("label")
        self.allReservation_tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.allReservation_tableWidget.setGeometry(QtCore.QRect(10, 130, 1791, 421))
        self.allReservation_tableWidget.setStyleSheet("")
        self.allReservation_tableWidget.setObjectName("allReservation_tableWidget")
        self.allReservation_tableWidget.setColumnCount(14)
        self.allReservation_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.allReservation_tableWidget.setHorizontalHeaderItem(13, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1816, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Reservation Table"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NUM_RESERVATION"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "NUM_VISITEUR"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "NUM_CHAMBRE"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "DATE_DEB"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "DATE_FIN"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "CIN"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "NOM"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "PRENOM"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "ADRESSE"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "TEL"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "EMAIL"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "ETAGE"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "DESCRIPTION"))
        item = self.allReservation_tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "PRIX"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
