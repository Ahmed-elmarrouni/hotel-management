# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'allReservation.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_allReservationMainWindow(object):
    def setupUi(self, allReservationMainWindow):
        allReservationMainWindow.setObjectName("allReservationMainWindow")
        allReservationMainWindow.resize(950, 676)
        allReservationMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(allReservationMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.allReservation_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.allReservation_listWidget.setGeometry(QtCore.QRect(10, 150, 931, 471))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.allReservation_listWidget.setFont(font)
        self.allReservation_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.allReservation_listWidget.setStyleSheet("#allReservation_listWidget{\n"
"color: rgb(9, 9, 9);\n"
"background-color: rgb(255, 160, 248);\n"
"border-radius: 18px;\n"
"border: 3px Solid rgb(170, 8, 108);\n"
"}\n"
"")
        self.allReservation_listWidget.setObjectName("allReservation_listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 461, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color:  rgb(170, 8, 108);\n"
"font: 75 italic  \"Open Sans\";\n"
"")
        self.label.setObjectName("label")
        allReservationMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(allReservationMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 950, 29))
        self.menubar.setObjectName("menubar")
        allReservationMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(allReservationMainWindow)
        self.statusbar.setObjectName("statusbar")
        allReservationMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(allReservationMainWindow)
        QtCore.QMetaObject.connectSlotsByName(allReservationMainWindow)

    def retranslateUi(self, allReservationMainWindow):
        _translate = QtCore.QCoreApplication.translate
        allReservationMainWindow.setWindowTitle(_translate("allReservationMainWindow", "MainWindow"))
        self.label.setText(_translate("allReservationMainWindow", "All Reservation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    allReservationMainWindow = QtWidgets.QMainWindow()
    ui = Ui_allReservationMainWindow()
    ui.setupUi(allReservationMainWindow)
    allReservationMainWindow.show()
    sys.exit(app.exec_())