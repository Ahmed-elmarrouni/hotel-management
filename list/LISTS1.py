import sys
from PyQt5 import QtWidgets
from lists import Ui_Lists_MainWindow
import mysql.connector


class Test(QtWidgets.QMainWindow, Ui_Lists_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Clear_btn.clicked.connect(self.clear_click)
        self.Search_btn.clicked.connect(self.search_click)

    def search_click(self):

        self.ClientInformation_listWidget.clear()
        self.ClientReservation_listWidget.clear()

        user_Id = self.User_Id_input.text()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')
        
        if self.User_Id_input.text() == "":
            QtWidgets.QMessageBox.warning(
                self, 'Input is empty', 'Please enter User ID.')

        else:
            query_1 = "SELECT * FROM visiteur WHERE NUM_VISITEUR = %s"
            query_2 = "SELECT * FROM reservation WHERE NUM_VISITEUR = %s"
            params = (user_Id,)

            cursor = connection.cursor()
            cursor.execute(query_1, params)

            results_1 = cursor.fetchall()
            cursor.execute(query_2, params)

            results_2 = cursor.fetchall()

            cursor.close()
            connection.close()

            if results_1 or results_2:

                for result in results_1:
                    # List des "INFORMATION"
                    self.ClientInformation_listWidget.addItem(
                        "NUM_VISITEUR: " + str(result[0]))
                    self.ClientInformation_listWidget.addItem(
                        "CIN: " + str(result[1]))
                    self.ClientInformation_listWidget.addItem(
                        "NOM: " + str(result[2]))
                    self.ClientInformation_listWidget.addItem(
                        "PRENOM: " + str(result[3]))
                    self.ClientInformation_listWidget.addItem(
                        "ADRESSE: " + str(result[4]))
                    self.ClientInformation_listWidget.addItem(
                        "TEL: " + str(result[5]))
                    self.ClientInformation_listWidget.addItem(
                        "EMAIL: " + str(result[6]) + "\n" + "\n")

                for result in results_2:
                    # List des "RESERVATION"
                    self.ClientReservation_listWidget.addItem(
                        "NUM_RESERVATION: " + str(result[1]))
                    self.ClientReservation_listWidget.addItem(
                        "NUM_CHAMBRE: " + str(result[2]))
                    self.ClientReservation_listWidget.addItem(
                        "DATE_DEB: " + str(result[3]))
                    self.ClientReservation_listWidget.addItem(
                        "DATE_FIN: " + str(result[4]) + "\n")

            else:
                QtWidgets.QMessageBox.warning(self, '^_^', 'NOT FOUND !!')

# Clear BUTTOND
    def clear_click(self):
        self.ClientInformation_listWidget.clear()
        self.ClientReservation_listWidget.clear()
        self.User_Id_input.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = Test()
    client.show()
    sys.exit(app.exec_())





