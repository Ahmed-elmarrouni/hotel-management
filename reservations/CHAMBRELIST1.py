import sys
from PyQt5 import QtWidgets
from chambresList import Ui_MainWindowChambreList
import mysql.connector


class Test(QtWidgets.QMainWindow, Ui_MainWindowChambreList):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        connection = mysql.connector.connect(
            host="localhost", user="root", password="", database="hotel"
        )
        cursor = connection.cursor()

        chambre_query = "SELECT * FROM chambre WHERE ETAT = 'available'"
        cursor.execute(chambre_query)
        chambres = cursor.fetchall()

        if not chambres:
            self.chambres_listWidget.addItem("No available chambre")
        else:
            for chambre in chambres:
                NUM_CHAMBRE = chambre[1]
                ETAGE = chambre[2]
                PRIX = chambre[4]

                item_text = f"NUM_CHAMBRE: {NUM_CHAMBRE}/ ETAGE: {ETAGE}/ PRIX: {PRIX}"
                self.chambres_listWidget.addItem(item_text)

        self.chambres_listWidget.itemClicked.connect(self.handleChambreClick)
        connection.close()

    def handleChambreClick(self, item):
        selected_text = item.text()
        print(selected_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = Test()
    client.show()
    sys.exit(app.exec_())
