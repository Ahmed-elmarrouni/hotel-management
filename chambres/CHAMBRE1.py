import sys
from PyQt5 import QtWidgets
from chambre import Ui_MainWindow_Chambre
import re
import mysql.connector


class Test(QtWidgets.QMainWindow, Ui_MainWindow_Chambre):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

        self.Add_btn.clicked.connect(self.add_click)
        self.Search_btn.clicked.connect(self.search_click)
        self.Delete_btn.clicked.connect(self.delete_click)
        self.Clear_btn.clicked.connect(self.clear_click)

    # ADD BUTTON
    def add_click(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')

        if self.NUM_CHAMBRE_input.text() == "" and self.ETAGE_input.text() == "" and self.DESCRIPTION_input.text() == "" and self.PRIX_input.text() == "" and self.ETAT_input.text() == "":
            QtWidgets.QMessageBox.warning(
                self, '^_^', 'All input is empty')
        else:

            if self.NUM_CHAMBRE_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter NUM_CHAMBRE.') 
                
            # if int(self.NUM_CHAMBRE_input.text()) < 1 or int(self.NUM_CHAMBRE_input.text()) > 80:
            #     QtWidgets.QMessageBox.warning(self, 'ERROR', 'Please enter a chambre number between 1 and 80.')
 
            elif self.ETAGE_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter ETAGE.')
            elif self.DESCRIPTION_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter DESCRIPTION.')
            elif self.PRIX_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter PRIX.')
            elif self.ETAT_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter ETAT.')

            else:

                m = "INSERT INTO chambre (NUM_CHAMBRE, ETAGE, DESCRIPTION, PRIX, ETAT) VALUES (%s, %s, %s, %s, %s)"
                data = (
                    self.NUM_CHAMBRE_input.text(),
                    self.ETAGE_input.text(),
                    self.DESCRIPTION_input.text(),
                    self.PRIX_input.text(),
                    self.ETAT_input.text(),

                )
                cursor = connection.cursor()
                cursor.execute(m, data)
                connection.commit()
                QtWidgets.QMessageBox.information(
                    self, 'Success', 'Data has been successfully inserted into the database.')

    #  SEARCH BUTTON
    def search_click(self):
        num_chambre = self.NUM_CHAMBRE_input.text()
    
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')
    
        if num_chambre == "":
            QtWidgets.QMessageBox.warning(
                self, 'Input is empty', 'Please enter your  NUM_CHAMBRE.')
            return
    
        query = "SELECT c.NUM_CHAMBRE, c.ETAGE, c.DESCRIPTION, c.PRIX, c.ETAT, r.NUM_VISITEUR, r.DATE_DEB, r.DATE_FIN " \
                "FROM chambre c LEFT JOIN reservation r ON c.NUM_CHAMBRE = r.NUM_CHAMBRE " \
                "WHERE c.NUM_CHAMBRE = %s"
    
        params = (num_chambre,)
    
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
    
        if results:
            self.Chambre_listWidget.clear()
    
            for result in results:
                NUM_CHAMBRE = result[0]
                ETAGE = result[1]
                DESCRIPTION = result[2]
                PRIX = result[3]
                ETAT = result[4]
    
                self.NUM_CHAMBRE_input.setText(str(NUM_CHAMBRE))
                self.ETAGE_input.setText(str(ETAGE))
                self.DESCRIPTION_input.setText(DESCRIPTION)
                self.PRIX_input.setText(str(PRIX))
                self.ETAT_input.setText(ETAT)
    
                if result[5] is not None:
                    self.Chambre_listWidget.addItem(
                        "NUM_VISITEUR: " + str(result[5]))
                    self.Chambre_listWidget.addItem(
                        "NUM_CHAMBRE: " + str(NUM_CHAMBRE))
                    self.Chambre_listWidget.addItem(
                        "DATE_DEB: " + str(result[6]))
                    self.Chambre_listWidget.addItem(
                        "DATE_FIN: " + str(result[7]) + "\n")
    
        else:
            QtWidgets.QMessageBox.warning(
                self, '^__^', 'NOT FOUND !!')
    
        cursor.close()
        connection.close()
    

    # DELETE BUTTON
    def delete_click(self):        
        num_chambre = self.NUM_CHAMBRE_input.text()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')  

        cursor = connection.cursor()
        if num_chambre == "":
            QtWidgets.QMessageBox.warning(   
                self, 'Input is empty', 'Please enter NUM CHAMBRE to delete item.')
        else:
            query = "SELECT * FROM chambre WHERE NUM_CHAMBRE = %s"
            params = (num_chambre,)

            cursor.execute(query, params)
            result = cursor.fetchone()
            if result is not None:
                msg_box = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this chambre?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
                # If user click on the "Yes" button the item is deleted If not the item is not deleted.
                if msg_box == QtWidgets.QMessageBox.Yes:
                    query = "DELETE FROM chambre WHERE NUM_CHAMBRE = %s"
                    cursor.execute(query, params)
                    connection.commit()
                    QtWidgets.QMessageBox.information(self, 'Success', 'chambre deleted successfully.')

            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'visiteur not found in the chambre Table.')

        cursor.close()
        connection.close()
   

    # CLEAR BUTTON
    def clear_click(self):
        self.Chambre_listWidget.clear()
        self.NUM_CHAMBRE_input.clear()
        self.ETAGE_input.clear()
        self.DESCRIPTION_input.clear()
        self.PRIX_input.clear()
        self.ETAT_input.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = Test()
    client.show()
    sys.exit(app.exec_())
