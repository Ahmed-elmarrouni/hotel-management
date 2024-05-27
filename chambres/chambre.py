# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chambre.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Chambre(object):
    def setupUi(self, MainWindow_Chambre):
        MainWindow_Chambre.setObjectName("MainWindow_Chambre")
        MainWindow_Chambre.resize(837, 604)
        MainWindow_Chambre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow_Chambre)
        self.centralwidget.setObjectName("centralwidget")
        self.ETAT_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ETAT_input.setGeometry(QtCore.QRect(270, 360, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ETAT_input.setFont(font)
        self.ETAT_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.ETAT_input.setObjectName("ETAT_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 0, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(9, 28, 149);")
        self.label.setObjectName("label")
        self.NUM_CHAMBRE_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NUM_CHAMBRE_input.setGeometry(QtCore.QRect(30, 110, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NUM_CHAMBRE_input.setFont(font)
        self.NUM_CHAMBRE_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.NUM_CHAMBRE_input.setText("")
        self.NUM_CHAMBRE_input.setObjectName("NUM_CHAMBRE_input")
        self.DESCRIPTION_input = QtWidgets.QLineEdit(self.centralwidget)
        self.DESCRIPTION_input.setGeometry(QtCore.QRect(30, 210, 441, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.DESCRIPTION_input.setFont(font)
        self.DESCRIPTION_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.DESCRIPTION_input.setObjectName("DESCRIPTION_input")
        self.Delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Delete_btn.setGeometry(QtCore.QRect(30, 480, 121, 71))
        self.Delete_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Delete_btn.setFont(font)
        self.Delete_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Delete_btn.setStyleSheet("#Delete_btn{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: rgb(255, 2, 14);\n"
"border: 3px Solid rgb(175, 34, 15);\n"
"}\n"
"#Delete_btn:hover:pressed{\n"
"background-color: rgb(255, 167, 43);\n"
"}\n"
"")
        self.Delete_btn.setObjectName("Delete_btn")
        self.Add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Add_btn.setGeometry(QtCore.QRect(350, 480, 121, 71))
        self.Add_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Add_btn.setFont(font)
        self.Add_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Add_btn.setStyleSheet("#Add_btn{\n"
"background-color: rgb(112, 162, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"border: 3px Solid rgb(17, 21, 255);\n"
"}\n"
"#Add_btn:hover:pressed{\n"
"background-color: rgb(190, 164, 255);\n"
"}")
        self.Add_btn.setObjectName("Add_btn")
        self.ETAGE_input = QtWidgets.QLineEdit(self.centralwidget)
        self.ETAGE_input.setGeometry(QtCore.QRect(270, 110, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ETAGE_input.setFont(font)
        self.ETAGE_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.ETAGE_input.setObjectName("ETAGE_input")
        self.Search_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Search_btn.setGeometry(QtCore.QRect(190, 480, 121, 71))
        self.Search_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Search_btn.setFont(font)
        self.Search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Search_btn.setStyleSheet("#Search_btn{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(60, 255, 39);\n"
"border-radius: 18px;\n"
"border: 3px Solid rgb(3, 168, 17);\n"
"}\n"
"#Search_btn:hover:pressed{\n"
"background-color: rgb(126, 255, 103);\n"
"}")
        self.Search_btn.setObjectName("Search_btn")
        self.PRIX_input = QtWidgets.QLineEdit(self.centralwidget)
        self.PRIX_input.setGeometry(QtCore.QRect(30, 360, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.PRIX_input.setFont(font)
        self.PRIX_input.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.PRIX_input.setObjectName("PRIX_input")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 90, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(9, 28, 149);")
        self.label_3.setObjectName("label_3")
        self.Chambre_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.Chambre_listWidget.setGeometry(QtCore.QRect(500, 140, 321, 301))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Chambre_listWidget.setFont(font)
        self.Chambre_listWidget.setStyleSheet("border: 2px solid rgba(0,0,0,0);\n"
"border-color: rgb(17, 40, 255);\n"
"padding-bottom:7px;\n"
"background-color: rgb(194, 254, 255);")
        self.Chambre_listWidget.setObjectName("Chambre_listWidget")
        self.Clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_btn.setGeometry(QtCore.QRect(500, 480, 321, 71))
        self.Clear_btn.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Clear_btn.setFont(font)
        self.Clear_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Clear_btn.setStyleSheet("#Clear_btn{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 18px;\n"
"background-color: rgb(255, 112, 10);\n"
"border: 3px Solid rgb(175, 34, 15);\n"
"}\n"
"#Clear_btn:hover:pressed{\n"
"background-color: rgb(158, 182, 186);\n"
"}\n"
"")
        self.Clear_btn.setObjectName("Clear_btn")
        MainWindow_Chambre.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_Chambre)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 837, 29))
        self.menubar.setObjectName("menubar")
        MainWindow_Chambre.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Chambre)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Chambre.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_Chambre)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Chambre)

    def retranslateUi(self, MainWindow_Chambre):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Chambre.setWindowTitle(_translate("MainWindow_Chambre", "Chambre_Window"))
        self.ETAT_input.setPlaceholderText(_translate("MainWindow_Chambre", "ETAT"))
        self.label.setText(_translate("MainWindow_Chambre", "Chambre"))
        self.NUM_CHAMBRE_input.setPlaceholderText(_translate("MainWindow_Chambre", "NUM_CHAMBRE"))
        self.DESCRIPTION_input.setPlaceholderText(_translate("MainWindow_Chambre", "DESCRIPTION...."))
        self.Delete_btn.setText(_translate("MainWindow_Chambre", "Delete "))
        self.Add_btn.setText(_translate("MainWindow_Chambre", "Add "))
        self.ETAGE_input.setPlaceholderText(_translate("MainWindow_Chambre", "ETAGE"))
        self.Search_btn.setText(_translate("MainWindow_Chambre", "Search "))
        self.PRIX_input.setPlaceholderText(_translate("MainWindow_Chambre", "PRIX"))
        self.label_3.setText(_translate("MainWindow_Chambre", "Chambres list  :"))
        self.Clear_btn.setText(_translate("MainWindow_Chambre", "Clear "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Chambre = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Chambre()
    ui.setupUi(MainWindow_Chambre)
    MainWindow_Chambre.show()
    sys.exit(app.exec_())
