import sys
from PyQt5 import QtWidgets
from visiteur import Ui_MainWindow_visiteur
import mysql.connector
import re


class Test(QtWidgets.QMainWindow, Ui_MainWindow_visiteur):
    def __init__(self):
        
        super().__init__()
        self.setupUi(self)

        self.Search_btn.clicked.connect(self.search_click)
        self.Add_btn.clicked.connect(self.add_click)
        self.Delete_btn.clicked.connect(self.delete_click)

    
# ADD BUTTON :

    def add_click(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')

        if self.NUM_VISITEUR_input.text() == "" and self.CIN_input.text() == "" and self.NOM_input.text() == "" and self.PRENOM_input.text() == "" and self.ADRESSE_input.text() == "" and self.EMAIL_input.text() == "" and self.TEL_input.text() == "":
            
            # Show message box
            QtWidgets.QMessageBox.warning(
                self, '^_^', 'All input is empty \n Please enter your information')
            
                                    
        else:
            # NUM VISITEUR INPUT
            if self.NUM_VISITEUR_input.text() == "":
                QtWidgets.QMessageBox.warning(self, 'Input is empty', 'Please enter your NUM_VISITEUR.')
            # CIN INPUT
            if self.CIN_input.text() == "":   
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter your CIN.')
            # NOM INPUT
            elif self.NOM_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter your NOM.')
            # PRENOM INPUT
            elif self.PRENOM_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter your PRENOM.')
            # ADRESSE INPUT
            elif self.ADRESSE_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter your ADRESSE.')
            # TEL INPUT
            elif self.TEL_input.text() == "":
                QtWidgets.QMessageBox.warning(
                    self, 'Input is empty', 'Please enter your TEL.')

            else:
                tel_pattern = r"\d{10}"
                if not re.match(tel_pattern, self.TEL_input.text()):
                    QtWidgets.QMessageBox.warning(
                        self, 'Invalid Phone Number', 'Please enter a valid phone number.')
                # EMAIL INPUT
                elif self.EMAIL_input.text() == "":
                    QtWidgets.QMessageBox.warning(
                        self, 'Input is empty', 'Please enter your EMAIL.')

                else:
                    email_pattern = r"[^@]+@[^@]+\.[^@]+"
                    if not re.match(email_pattern, self.EMAIL_input.text()):
                        self.EMAIL_input.setStyleSheet(
                            "border: 2px solid red;")
                        QtWidgets.QMessageBox.warning(
                            self, 'Invalid Email', 'Please enter a valid email address.')
                    else:
                        m = "INSERT INTO visiteur (NUM_VISITEUR, CIN, NOM, PRENOM, ADRESSE, TEL, EMAIL) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                        data = (
                            self.NUM_VISITEUR_input.text(),
                            self.CIN_input.text(),
                            self.NOM_input.text(),
                            self.PRENOM_input.text(),
                            self.ADRESSE_input.text(),
                            self.TEL_input.text(),
                            self.EMAIL_input.text()
                        )
                        cursor = connection.cursor()
                        cursor.execute(m, data)
                        connection.commit()
                        QtWidgets.QMessageBox.information(
                            self, 'Success', 'Data has been successfully inserted into the database.')

    # # SEARCH BUTTON
    def search_click(self):
        num_visiteur = self.NUM_VISITEUR_input.text()
    
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')
    
        if num_visiteur == "":
            QtWidgets.QMessageBox.warning(
                self, 'Input is empty', 'Please enter  NUM_VISITEUR.')
            return
    
        query = "SELECT * FROM visiteur WHERE NUM_VISITEUR = %s"
        params = (num_visiteur,)
    
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
    
        if results:
            self.NUM_VISITEUR_input.setText(str(results[0][1]))
            self.CIN_input.setText(str(results[0][2]))
            self.NOM_input.setText(results[0][3])
            self.PRENOM_input.setText(results[0][4])
            self.ADRESSE_input.setText(results[0][5])
            self.TEL_input.setText(str(results[0][6]))
            self.EMAIL_input.setText(str(results[0][7]))
        else:
            QtWidgets.QMessageBox.warning(
                self, '^_^', 'VISITEUR NOT FOUND !!')
            
            self.NUM_VISITEUR_input.clear()
            self.CIN_input.clear()
            self.NOM_input.clear()
            self.PRENOM_input.clear()
            self.ADRESSE_input.clear()
            self.TEL_input.clear()
            self.EMAIL_input.clear()
    
        cursor.close()
        connection.close()
    
    
        # DELETE BUTTOn
    def delete_click(self):
        
        num_visiteur = self.NUM_VISITEUR_input.text()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')  

        cursor = connection.cursor()
        if num_visiteur == "":
            QtWidgets.QMessageBox.warning(   
                self, 'Input is empty', 'Please enter NUM VISITEUR to delete item.')
        else:
            query = "SELECT * FROM visiteur WHERE NUM_VISITEUR = %s"
            params = (num_visiteur,)

            cursor.execute(query, params)
            result = cursor.fetchone()
            if result is not None:
                msg_box = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this visiteur?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
                # If user click on the "Yes" button the item is deleted If not the item is not deleted.
                if msg_box == QtWidgets.QMessageBox.Yes:
                    query = "DELETE FROM visiteur WHERE NUM_VISITEUR = %s"
                    cursor.execute(query, params)
                    connection.commit()
                    QtWidgets.QMessageBox.information(self, 'Success', 'Visiteur deleted successfully.')

            else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'visiteur not found in the visiteur Table.')

        cursor.close()
        connection.close()
        





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = Test()
    client.show()
    sys.exit(app.exec_())
