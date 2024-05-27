from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(434, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Price_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Price_input.setGeometry(QtCore.QRect(40, 50, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.Price_input.setFont(font)
        self.Price_input.setText("")
        self.Price_input.setObjectName("Price_input")
        self.price_label = QtWidgets.QLabel(self.centralwidget)
        self.price_label.setGeometry(QtCore.QRect(70, 250, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.price_label.setFont(font)
        self.price_label.setStyleSheet("color: rgb(255, 2, 57);")
        self.price_label.setObjectName("price_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 434, 29))
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
        self.price_label.setText(_translate("MainWindow", "00000  $"))

    
    def changeText(self):
        self.label.setText(self.edit.text())

    def setupConnections(self):
      self.edit = self.centralwidget.findChild(QLineEdit, "Price_input")
      self.label = self.centralwidget.findChild(QLabel, "price_label")

      self.edit.textChanged.connect(self.changeText)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupConnections()
    MainWindow.show()
    sys.exit(app.exec_())

