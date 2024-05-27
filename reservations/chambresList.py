# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chambresList.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowChambreList(object):
    def setupUi(self, MainWindowChambreList):
        MainWindowChambreList.setObjectName("MainWindowChambreList")
        MainWindowChambreList.resize(617, 507)
        MainWindowChambreList.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.centralwidget = QtWidgets.QWidget(MainWindowChambreList)
        self.centralwidget.setObjectName("centralwidget")
        self.chambres_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.chambres_listWidget.setGeometry(QtCore.QRect(10, 140, 591, 311))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.chambres_listWidget.setFont(font)
        self.chambres_listWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.chambres_listWidget.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(170, 247, 255);\n"
"color:rgb(0, 0, 0)")
        self.chambres_listWidget.setObjectName("chambres_listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 0, 371, 61))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(35)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(9, 28, 149);\n"
"font: 75 italic  \"Open Sans\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(9, 28, 149);")
        self.label_2.setObjectName("label_2")
        MainWindowChambreList.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowChambreList)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 29))
        self.menubar.setObjectName("menubar")
        MainWindowChambreList.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowChambreList)
        self.statusbar.setObjectName("statusbar")
        MainWindowChambreList.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowChambreList)
        QtCore.QMetaObject.connectSlotsByName(MainWindowChambreList)

    def retranslateUi(self, MainWindowChambreList):
        _translate = QtCore.QCoreApplication.translate
        MainWindowChambreList.setWindowTitle(_translate("MainWindowChambreList", "MainWindow"))
        self.label.setText(_translate("MainWindowChambreList", "Chambres-List"))
        self.label_2.setText(_translate("MainWindowChambreList", "Choose chambre :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowChambreList = QtWidgets.QMainWindow()
    ui = Ui_MainWindowChambreList()
    ui.setupUi(MainWindowChambreList)
    MainWindowChambreList.show()
    sys.exit(app.exec_())