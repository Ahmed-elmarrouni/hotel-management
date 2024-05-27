from hashlib import new
import string
import sys
from PyQt5 import QtWidgets 
from PyQt5.QtCore import QDate
from datetime import datetime
import mysql.connector
from test2 import Ui_MainWindow
# "QtCore" for sort the table
from PyQt5 import QtCore


class Test(QtWidgets.QMainWindow, Ui_MainWindow):
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
        reservationQuery = """
        SELECT * 
        FROM reservation 
        JOIN visiteur ON reservation.NUM_VISITEUR = visiteur.NUM_VISITEUR 
        JOIN chambre ON reservation.NUM_CHAMBRE = chambre.NUM_CHAMBRE
        """

        # cursor = self.connection.cursor(dictionary = True)
        
        cursor.execute(reservationQuery)
        allReservations = cursor.fetchall()
 
        self.allReservation_tableWidget.setRowCount(len(allReservations))
        self.allReservation_tableWidget.setColumnCount(14)
 
        # With this code, normal users can't change the reservation information
        self.allReservation_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        for row, reservation in enumerate(allReservations):
            # RESERVATION TABLE
            NUM_RESERVATION = reservation[1]
            NUM_VISITEUR = reservation[2]
            NUM_CHAMBRE = reservation[3]
            DATE_DEB = QDate.fromString(reservation[4].strftime("%Y-%m-%d"), "yyyy-MM-dd").toString("yyyy-MM-dd")
            DATE_FIN = QDate.fromString(reservation[5].strftime("%Y-%m-%d"), "yyyy-MM-dd").toString("yyyy-MM-dd")

            # VISITEUR TABLE
            CIN = reservation[8]
            NOM = reservation[9]
            PRENOM = reservation[10]
            ADRESSE = reservation[11]
            TEL = reservation[12]
            EMAIL = reservation[13]
            
            # CHAMBRE TABLE
            ETAGE = reservation[16]
            DESCRIPTION = reservation[17]
            PRICE = reservation[18]
            
            # Calculate The Price for every chambre in reservations list
            date_deb = datetime.strptime(DATE_DEB, '%Y-%m-%d')
            date_fin = datetime.strptime(DATE_FIN, '%Y-%m-%d')
            
            duration = (date_fin - date_deb).days

            chambre_price_query = "SELECT PRIX FROM chambre WHERE NUM_CHAMBRE = %s"
            cursor.execute(chambre_price_query, (NUM_CHAMBRE,))
            result = cursor.fetchone()
            
            PRIX = float(result[0])
            PRICE = duration * PRIX
            
            # Set Item Set information for every reservation in table Widget
            self.allReservation_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(NUM_RESERVATION)))
            self.allReservation_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(NUM_VISITEUR)))
            self.allReservation_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(NUM_CHAMBRE)))
            self.allReservation_tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(DATE_DEB))
            self.allReservation_tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(DATE_FIN))
            self.allReservation_tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(CIN)))
            self.allReservation_tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(NOM))
            self.allReservation_tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(PRENOM))
            self.allReservation_tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(ADRESSE))
            self.allReservation_tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(TEL)))
            self.allReservation_tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(EMAIL))
            self.allReservation_tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(ETAGE)))
            self.allReservation_tableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(DESCRIPTION))
            self.allReservation_tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(PRICE))) 
            
            


        # Sort the tableWidget  column "DATE_DEB" 
        self.allReservation_tableWidget.setSortingEnabled(True)
        self.allReservation_tableWidget.sortItems(QtCore.Qt.AscendingOrder)




        connection.close()





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = Test()
    client.show()
    sys.exit(app.exec_())


