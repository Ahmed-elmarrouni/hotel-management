import sys
from PyQt5 import QtWidgets
from allReservation import Ui_allReservationMainWindow
import mysql.connector


class Test(QtWidgets.QMainWindow, Ui_allReservationMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel'
        )
        cursor = connection.cursor()

        chambre_query = "SELECT * FROM chambre WHERE ETAT = 'available'"
        cursor.execute(chambre_query)
        chambres = cursor.fetchall()

        if not chambres:
            self.allReservation_listWidget.addItem("No available chambre")
        else:
            for chambre in chambres:
                NUM_CHAMBRE = chambre[1]
                ETAGE = chambre[2]
                PRIX = chambre[4]

                item_text = f"N° de chambre: {NUM_CHAMBRE}/ Etage: {ETAGE}/ PRIX: {PRIX}💸"
                self.allReservation_listWidget.addItem(item_text)

        connection.close()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = Test()
    client.show()
    sys.exit(app.exec_())
