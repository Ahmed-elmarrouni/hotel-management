import sys
from time import strftime
from PyQt5 import QtWidgets , QtCore 
from reservation import Ui_RESERVATIONMainWindow
from datetime import datetime 
from PyQt5.QtCore import QDate 
import mysql.connector



# TABLE WIDGET
# from PyQt5.QtWidgets import QTableWidgetItem
# from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem


# CALL TO CHAMBRE LIST SCREEN
from chambresList import Ui_MainWindowChambreList

# CALL TO ALL RESERVATION_SCREEN
from allReservation import Ui_allReservationMainWindow


class Test(QtWidgets.QMainWindow, Ui_RESERVATIONMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        
        
        # QDateEdit = "" 
        # QDate = ""
        # datetime = ""
     
       
    #    "allReservation_tableWidget" whith this table now user can see all reservation in hotel
    
        # connection = mysql.connector.connect(
        #      host='localhost',
        #      user='root',
        #      password='',
        #      database='hotel'
        #  )
        # cursor = connection.cursor()
        # reservationQuery = """
        # SELECT * 
        # FROM reservation 
        # JOIN visiteur ON reservation.NUM_VISITEUR = visiteur.NUM_VISITEUR 
        # JOIN chambre ON reservation.NUM_CHAMBRE = chambre.NUM_CHAMBRE
        # """

        # # cursor = self.connection.cursor(dictionary = True)
        
        # cursor.execute(reservationQuery)
        # allReservations = cursor.fetchall()
 
        # self.allReservation_tableWidget.setRowCount(len(allReservations))
        # self.allReservation_tableWidget.setColumnCount(14)
 
        # # With this code, normal users can't change the reservation information
        # self.allReservation_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # for row, reservation in enumerate(allReservations):
        #     # RESERVATION TABLE
        #     NUM_RESERVATION = reservation[1]
        #     NUM_VISITEUR = reservation[2]
        #     NUM_CHAMBRE = reservation[3]
        #     DATE_DEB = QDate.fromString(reservation[4].strftime("%Y-%m-%d"), "yyyy-MM-dd").toString("yyyy-MM-dd")
        #     DATE_FIN = QDate.fromString(reservation[5].strftime("%Y-%m-%d"), "yyyy-MM-dd").toString("yyyy-MM-dd")

        #     # VISITEUR TABLE
        #     CIN = reservation[8]
        #     NOM = reservation[9]
        #     PRENOM = reservation[10]
        #     ADRESSE = reservation[11]
        #     TEL = reservation[12]
        #     EMAIL = reservation[13]
            
        #     # CHAMBRE TABLE
        #     ETAGE = reservation[16]
        #     DESCRIPTION = reservation[17]
        #     PRICE = reservation[18]
            
        #     # Calculate The Price for every chambre in reservations list
        #     date_deb = datetime.strptime(DATE_DEB, '%Y-%m-%d')
        #     date_fin = datetime.strptime(DATE_FIN, '%Y-%m-%d')
            
        #     duration = (date_fin - date_deb).days

        #     chambre_price_query = "SELECT PRIX FROM chambre WHERE NUM_CHAMBRE = %s"
        #     cursor.execute(chambre_price_query, (NUM_CHAMBRE,))
        #     result = cursor.fetchone()
            
        #     PRIX = float(result[0])
        #     PRICE = duration * PRIX
            
        #     # Set Item Set information for every reservation in table Widget
        #     self.allReservation_tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(NUM_RESERVATION)))
        #     self.allReservation_tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(NUM_VISITEUR)))
        #     self.allReservation_tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(NUM_CHAMBRE)))
        #     self.allReservation_tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(DATE_DEB))
        #     self.allReservation_tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(DATE_FIN))
        #     self.allReservation_tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(CIN)))
        #     self.allReservation_tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(NOM))
        #     self.allReservation_tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(PRENOM))
        #     self.allReservation_tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(ADRESSE))
        #     self.allReservation_tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(TEL)))
        #     self.allReservation_tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(EMAIL))
        #     self.allReservation_tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(ETAGE)))
        #     self.allReservation_tableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(DESCRIPTION))
        #     self.allReservation_tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(PRICE)))

        # # Sort the tableWidget  column "DATE_DEB" 
        # self.allReservation_tableWidget.setSortingEnabled(True)
        # column_index = 1
        # self.allReservation_tableWidget.sortItems(column_index, QtCore.Qt.AscendingOrder)
        
        
        # connection.close()
        
        
            #    "allReservation_tableWidget" whith this table now user ( 'worker in hotel' ) can see all reservation in hotel

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel'
        )
        cursor = connection.cursor()

        # Execute the stored procedure to retrieve all reservations
        cursor.callproc("tableAllReservation")
        rows = cursor.fetchall()

        # Set the number of rows and columns in the tableWidget
        self.allReservation_tableWidget.setRowCount(len(rows))
        self.allReservation_tableWidget.setColumnCount(14)

        # Disable editing of the tableWidget by users
        self.allReservation_tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        # Iterate over the retrieved reservations and populate the tableWidget
        for res, reservation in enumerate(rows):
            # Extract reservation information
            NUM_RESERVATION = reservation[1]
            NUM_VISITEUR = reservation[2]
            NUM_CHAMBRE = reservation[3]
            DATE_DEB = QDate.fromString(reservation[4].strftime("%Y-%m-%d"), "yyyy-MM-dd").toString("yyyy-MM-dd")
            DATE_FIN = QDate.fromString(reservation[5].strftime("%Y-%m-%d"), "yyyy-MM-dd").toString("yyyy-MM-dd")

            # Retrieve visitor information from the VISITEUR table
            CIN = reservation[8]
            NOM = reservation[9]
            PRENOM = reservation[10]
            ADRESSE = reservation[11]
            TEL = reservation[12]
            EMAIL = reservation[13]

            # Retrieve room information from the CHAMBRE table
            ETAGE = reservation[16]
            DESCRIPTION = reservation[17]
            PRICE = reservation[18]

            # Calculate the price for the reservation
            date_deb = datetime.strptime(DATE_DEB, '%Y-%m-%d')
            date_fin = datetime.strptime(DATE_FIN, '%Y-%m-%d')
            duration = (date_fin - date_deb).days

            chambre_price_query = "SELECT PRIX FROM chambre WHERE NUM_CHAMBRE = %s"
            cursor.execute(chambre_price_query, (NUM_CHAMBRE,))
            result = cursor.fetchone()
            PRIX = float(result[0])
            PRICE = duration * PRIX

            # Set item information for the current reservation in the tableWidget
            self.allReservation_tableWidget.setItem(res, 0, QtWidgets.QTableWidgetItem(str(NUM_RESERVATION)))
            self.allReservation_tableWidget.setItem(res, 1, QtWidgets.QTableWidgetItem(str(NUM_VISITEUR)))
            self.allReservation_tableWidget.setItem(res, 2, QtWidgets.QTableWidgetItem(str(NUM_CHAMBRE)))
            self.allReservation_tableWidget.setItem(res, 3, QtWidgets.QTableWidgetItem(DATE_DEB))
            self.allReservation_tableWidget.setItem(res, 4, QtWidgets.QTableWidgetItem(DATE_FIN))
            self.allReservation_tableWidget.setItem(res, 5, QtWidgets.QTableWidgetItem(str(CIN)))
            self.allReservation_tableWidget.setItem(res, 6, QtWidgets.QTableWidgetItem(NOM))
            self.allReservation_tableWidget.setItem(res, 7, QtWidgets.QTableWidgetItem(PRENOM))
            self.allReservation_tableWidget.setItem(res, 8, QtWidgets.QTableWidgetItem(ADRESSE))
            self.allReservation_tableWidget.setItem(res, 9, QtWidgets.QTableWidgetItem(str(TEL)))
            self.allReservation_tableWidget.setItem(res, 10, QtWidgets.QTableWidgetItem(EMAIL))
            self.allReservation_tableWidget.setItem(res, 11, QtWidgets.QTableWidgetItem(str(ETAGE)))
            self.allReservation_tableWidget.setItem(res, 12, QtWidgets.QTableWidgetItem(DESCRIPTION))
            self.allReservation_tableWidget.setItem(res, 13, QtWidgets.QTableWidgetItem(str(PRICE)))

        # Enable sorting of the "DATE_DEB" column in the tableWidget
        self.allReservation_tableWidget.setSortingEnabled(True)
        column_index = 3
        self.allReservation_tableWidget.sortItems(column_index, QtCore.Qt.AscendingOrder)

        # Close the database connection
        connection.close()


# ####################################################################################################################
        #  BUTTONS "add/ search/ delete/ clear";
        self.Search_btn.clicked.connect(self.search_click)
        self.Delete_btn.clicked.connect(self.delete_click)
        self.Add_btn.clicked.connect(self.add_click) 
        self.Clear_btn.clicked.connect(self.clear_click)

       # Show Chambre Button
        self.showChambre_Btn.clicked.connect(self.showChambre_click)
        self.chambre_window = None
        
        # All Reservation Button
        self.allReservation_btn.clicked.connect(self.allReservation_click)
        self.allReservation_window = None

    
    #  when user click to "all reservation button" the computer directly open the new screen and show all the reservation 
    
    def allReservation_click(self):
        if self.allReservation_window is None:
            self.allReservation_window = QtWidgets.QMainWindow()
            self.ui = Ui_allReservationMainWindow()
            self.ui.setupUi(self.allReservation_window)
            self.allReservation_window.show()
        
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
        cursor.execute(reservationQuery)
        allReservations = cursor.fetchall()
        if not allReservations:
            self.ui.allReservation_listWidget.addItem("No reservations found")
        else:
            self.ui.allReservation_listWidget.clear()
            for row in allReservations:
               # RESERVATION TABLE
                NUM_RESERVATION = row[1]
                NUM_VISITEUR = row[2]
                NUM_CHAMBRE = row[3]
                DATE_DEB = QDate.fromString(row[4].strftime("%Y-%m-%d"), "yyyy-MM-dd")
                DATE_FIN = QDate.fromString(row[5].strftime("%Y-%m-%d"), "yyyy-MM-dd")
               
               # VISITEUR TABLE
                CIN = row[8]
                NOM = row[9]
                PRENOM = row[10]
                ADRESSE = row[11]
                TEL = row[12]
                EMAIL = row[13]
                
               # CHAMBRE TABLE
                ETAGE = row[16]
                DESCRIPTION = row[17]
                PRIX = row[18]
                ETAT = row[19]
                
                allReservation_text = f"==>🏩 Reservation N°: {NUM_RESERVATION}/ Visitor N°: {NUM_VISITEUR}/ Room N°: {NUM_CHAMBRE}\n📅 Start Date: {DATE_DEB.toString('yyyy-MM-dd')}/ End Date: {DATE_FIN.toString('yyyy-MM-dd')}\n🪪 CIN N°: {CIN}/ Name: {NOM}/ Surname: {PRENOM}\nAddress: {ADRESSE}/📱 Phone N°: {TEL}/ Email 📧: {EMAIL}\nEtage N°: {ETAGE}/ Description: {DESCRIPTION}/ Price: {PRIX} 💸/ Etat: {ETAT} .\n\n"
                self.ui.allReservation_listWidget.addItem(allReservation_text)
        connection.close()

    ## when user click to "show chambre button" the copmputer show the list of every available chambre    

    def showChambre_click(self):
        if self.chambre_window is None:
            self.chambre_window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindowChambreList()
            self.ui.setupUi(self.chambre_window)
            self.chambre_window.show()
            
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
            self.ui.chambres_listWidget.addItem("No available chambre")
        else:
            self.ui.chambres_listWidget.clear()
            for chambre in chambres:
                NUM_CHAMBRE = chambre[1]
                ETAGE = chambre[2]  
                PRIX = chambre[4]  
                item_text = f"N° de chambre: {NUM_CHAMBRE}/ Etage: {ETAGE}/ PRIX: {PRIX}💸"
                self.ui.chambres_listWidget.addItem(item_text)
                
            self.ui.chambres_listWidget.itemClicked.connect(self.selectedChambreClick)
        connection.close()
        
    # W rite the selected chambre
    def selectedChambreClick(self, item):
        selected_text = item.text()
        chambre_number = selected_text.split(':')[1].split('/')[0].strip()  
        self.NUM_CHAMBRE_input.setText(chambre_number)
        
        
        
 
# "When a user adds a new reservation, the application should calculate the duration of the visitor's stay in the room
#  and the corresponding amount the visitor must pay for his residence. without user click for any button"
# (DAT_FIN - DAT_DEB) * ChambrePrice =" totalPrice " ===> Show in '"PRICE" Label'
    
# how to change label text if user write something in LineEdit without using  buttons with python in QtDesigner 
# Clear BUTTOND
    
    # my_function = self.NUM_RESERVATION_input.clear() and self.NUM_VISITEUR_input.clear() and self.NUM_CHAMBRE_input.clear() and self.Reservation_listWidget.clear()4

            
        self.DATE_DEB.dateChanged.connect(self.calculate_price)
        self.DATE_FIN.dateChanged.connect(self.calculate_price)
        self.NUM_CHAMBRE_input.textChanged.connect(self.calculate_price)
    
    def calculate_price(self):
        if not (self.DATE_DEB.date() and self.DATE_FIN.date() and self.NUM_CHAMBRE_input.text()):
            return
    
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel'
        )
        cursor = connection.cursor()
    
        date_deb_obj = datetime.strptime(self.DATE_DEB.text(), '%m/%d/%Y')
        date_fin_obj = datetime.strptime(self.DATE_FIN.text(), '%m/%d/%Y')
        duration = (date_fin_obj - date_deb_obj).days
    
        chambre_price_query = "SELECT PRIX FROM chambre WHERE NUM_CHAMBRE = %s"
        cursor.execute(chambre_price_query, (int(self.NUM_CHAMBRE_input.text()),))
        result = cursor.fetchone()
        if result is None:
            self.Price.setText("Invalid room")
            return
    
        chambre_price = float(result[0])
    
        total_price = duration * chambre_price
        self.Price.setText(f"{total_price} DH.")
    
        connection.commit()
        cursor.close()
        connection.close()  
    





    
    # CLEAR BUTTON "claear all inputs and lists"
    def clear_click(self):
        self.NUM_RESERVATION_input.clear()
        self.NUM_VISITEUR_input.clear()
        self.NUM_CHAMBRE_input.clear()
        self.Reservation_listWidget.clear()
        
        
        
##################################################################################################################
# "add button " Add new reservataion
    def add_click(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel'
        )

        if self.NUM_RESERVATION_input.text() == "" and self.NUM_VISITEUR_input.text() == "" and self.NUM_CHAMBRE_input.text() == "":
            # Show message box if all input empty
            QtWidgets.QMessageBox.warning(
                self, '^_^', 'All input is empty \n Please enter Visiteur information')
        else:
            if self.NUM_RESERVATION_input.text() == "":
                QtWidgets.QMessageBox.warning(self, 'Input is empty', 'Please enter NUM_RESERVATION.')
            else:
                # Check if reservation already exists or not
                reservationTable = "SELECT * FROM reservation WHERE NUM_RESERVATION = %s"
                cursor = connection.cursor()
                cursor.execute(reservationTable, (self.NUM_RESERVATION_input.text(),))
                reservation = cursor.fetchone()
                if reservation is not None:
                    QtWidgets.QMessageBox.warning(self, 'ERROR', 'This reservation already exists.')

                # NUM VISITEUR INPUT
                elif self.NUM_VISITEUR_input.text() == "":
                    QtWidgets.QMessageBox.warning(
                        self, 'Input is empty', 'Please enter NUM_VISITEUR.')
                else:
                    visiteurTable = "SELECT * FROM visiteur WHERE NUM_VISITEUR = %s"
                    cursor.execute(visiteurTable, (self.NUM_VISITEUR_input.text(),))
                    visiteur = cursor.fetchone()
                    if visiteur is None:
                        QtWidgets.QMessageBox.warning(
                            self, 'ERROR', 'This Visiteur does not exist.')
                    # NUM_CHAMBRE_input
                    elif self.NUM_CHAMBRE_input.text() == "":
                        QtWidgets.QMessageBox.warning(
                            self, 'Input is empty', 'Please enter NUM_CHAMBRE.')
                    else:
                        chambreTable = "SELECT * FROM chambre WHERE NUM_CHAMBRE = %s"
                        cursor.execute(chambreTable, (self.NUM_CHAMBRE_input.text(),))
                        chambre = cursor.fetchone()
                        if chambre is None:
                            QtWidgets.QMessageBox.warning(
                                self, 'ERROR', 'This chambre does not exist.')

                        elif chambre[5] != "available":
                                QtWidgets.QMessageBox.warning(
                                self, 'ERROR', 'Chambre is unavailable.')


                        # If all inputs are valid and chambre is available, insert the reservation into the database
                        else:
                            m = "INSERT INTO reservation (NUM_RESERVATION, NUM_VISITEUR, NUM_CHAMBRE, DATE_DEB, DATE_FIN) VALUES (%s, %s, %s, %s, %s)"
                            #set to current date 
                            date_deb_str.setDate(QDate.currentDate()) 

                            date_deb_str = self.DATE_DEB.text()
                            date_fin_str = self.DATE_FIN.text()
                            date_deb_obj = datetime.strptime(date_deb_str, '%m/%d/%Y')
                            date_fin_obj = datetime.strptime(date_fin_str, '%m/%d/%Y')
                            date_deb = date_deb_obj.strftime('%Y-%m-%d')
                            date_fin = date_fin_obj.strftime('%Y-%m-%d')
                            data = (
                                self.NUM_RESERVATION_input.text(),
                                self.NUM_VISITEUR_input.text(),
                                self.NUM_CHAMBRE_input.text(),
                                date_deb,
                                date_fin
                            )
                            cursor.execute(m, data)
                            connection.commit()

                            # Calculate the duration of the visitor's stay and the corresponding amount the visitor must pay
                            duration = (date_fin_obj - date_deb_obj).days

                            chambre_price_query = "SELECT PRIX FROM chambre WHERE NUM_CHAMBRE = %s"
                            cursor.execute(chambre_price_query, (self.NUM_CHAMBRE_input.text(),))
                            chambre_price = cursor.fetchone()[0]
                            
                            total_price = duration * chambre_price
                            
                            # if user is sure that he wants to reserve this chambre "Confirmation buttons in QMessage Box"
                            msg_box = QtWidgets.QMessageBox.question(self, 'Confirmation',f'Total price for {duration} day(s) of stay: {total_price:} Dirham.\n\n  Are you sure you want to reserve  this chambre?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                                     QtWidgets.QMessageBox.No)
                            
                            if msg_box == QtWidgets.QMessageBox.Yes:
                                QtWidgets.QMessageBox.information(self, 'Reservation confirmed', 'Reservation has been confirmed.')
                                self.clear_click()
                            else:
                                connection.rollback()
                                QtWidgets.QMessageBox.warning(self, 'Reservation cancelled', 'Reservation has been cancelled.')
                                
        cursor.close()
        connection.close()



##############################################################################################################################################################################
    #  SEARCH BUTTON


    # def search_click(self):
    #     self.Reservation_listWidget.clear()

    #     num_reservation = self.NUM_RESERVATION_input.text()
    #     dat_deb = self.DATE_DEB.text()
    #     dat_fin = self.DATE_FIN.text()

    #     num_visiteur = self.NUM_VISITEUR_input.text()
    #     num_chambre = self.NUM_CHAMBRE_input.text()

    #     connection = mysql.connector.connect(
    #         host='localhost',
    #         user='root',
    #         password='',
    #         database='hotel'
    #     )

    #     cursor = connection.cursor()

    #     if num_reservation != "" and num_visiteur == "" and num_chambre == "":
    #         reservationQuery = "SELECT * FROM reservation WHERE NUM_RESERVATION = %s"
    #         inputs = (num_reservation,)

    #     elif num_visiteur != "" and num_chambre == "" and num_reservation == "":
    #         reservationQuery = "SELECT * FROM reservation WHERE NUM_VISITEUR = %s"
    #         inputs = (num_visiteur,)
    #     elif num_visiteur != "" and num_chambre != "" and num_reservation == "":
    #         reservationQuery = "SELECT * FROM reservation WHERE NUM_VISITEUR = %s AND NUM_CHAMBRE = %s"
    #         inputs = (num_visiteur, num_chambre)
            
    #     elif num_visiteur == "" and num_chambre != "" and num_reservation == "":
    #         reservationQuery = "SELECT * FROM reservation WHERE NUM_CHAMBRE = %s"
    #         inputs = (num_chambre,)

    #     else:
    #         reservationQuery = "SELECT * FROM reservation WHERE DATE_DEB AND DATE_FIN BETWEEN %s AND %s"
    #         dat_deb = datetime.strptime(dat_deb, '%m/%d/%Y').date()
    #         dat_fin = datetime.strptime(dat_fin, '%m/%d/%Y').date()
    #         inputs = (dat_deb, dat_fin)
            

    #     cursor.execute(reservationQuery, inputs)
    #     results = cursor.fetchall()

    #     found_results = False
    #     for result in results:
    #         NUM_RESERVATION = result[1]
    #         NUM_VISITEUR = result[2]
    #         NUM_CHAMBRE = result[3]
    #         DATE_DEB = QDate.fromString(str(result[4]), "yyyy-MM-dd")
    #         DATE_FIN = QDate.fromString(str(result[5]), "yyyy-MM-dd")
    #         found_results = True

    #         self.Reservation_listWidget.addItem("NUM_RESERVATION: " + str(NUM_RESERVATION))
    #         self.Reservation_listWidget.addItem("NUM_VISITEUR: " + str(NUM_VISITEUR))
    #         self.Reservation_listWidget.addItem("NUM_CHAMBRE: " + str(NUM_CHAMBRE))
    #         self.Reservation_listWidget.addItem("DATE_DEB: " + DATE_DEB.toString("yyyy-MM-dd"))
    #         self.Reservation_listWidget.addItem("DATE_FIN: " + DATE_FIN.toString("yyyy-MM-dd") + "\n")

    #     if not found_results:
    #         self.Reservation_listWidget.clear()
    #         QtWidgets.QMessageBox.warning(self, '^_^', 'NOT FOUND !!')

    #     cursor.close()
    #     connection.close()

# /////////////////////////////////////////
    def search_click(self):
        self.Reservation_listWidget.clear()

        num_reservation = self.NUM_RESERVATION_input.text()
        dat_deb = self.DATE_DEB.text()
        dat_fin = self.DATE_FIN.text()
        num_visiteur = self.NUM_VISITEUR_input.text()
        num_chambre = self.NUM_CHAMBRE_input.text()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel'
        )
        cursor = connection.cursor()

        reservationQuery = ""
        inputs = ()

        


        # If num_reservation or num_chambre or num_visiteur is full and others inputs empty
        if num_reservation != "" or num_chambre != "" or num_visiteur != "":
            reservationQuery = """
                SELECT * FROM reservation
                WHERE NUM_RESERVATION = %s
                OR NUM_CHAMBRE = %s
                OR NUM_VISITEUR = %s
            """
            inputs = (num_reservation, num_chambre, num_visiteur,)
            
        # if num_chambre and  num_visiteur are full and athors empty
        elif num_chambre != "" and num_visiteur != "" and dat_deb == "1/1/2000" and dat_fin == "1/1/2000":
            reservationQuery = """
                SELECT * FROM reservation
                WHERE NUM_VISITEUR = %s AND NUM_CHAMBRE = %s
            """
            inputs = (num_chambre, num_visiteur,)
            
        # if dat deb and dat fin are full
        elif dat_deb != "1/1/2000" or dat_fin != "1/1/2000" :
            reservationQuery = "SELECT * FROM reservation WHERE DATE_DEB AND DATE_FIN BETWEEN %s AND %s"
            dat_deb = datetime.strptime(dat_deb, '%m/%d/%Y').date()
            dat_fin = datetime.strptime(dat_fin, '%m/%d/%Y').date()
            inputs = (dat_deb, dat_fin)
            
            
            
        # If all inputs are full but num_reservation empty
        # elif num_visiteur != "" and num_chambre != "" and dat_deb != "1/1/2000" and dat_fin != "1/1/2000" and num_reservation == "":
        #     reservationQuery = """
        #         SELECT * FROM reservation
        #         WHERE NUM_VISITEUR = %s
        #         AND NUM_CHAMBRE = %s
        #         AND DATE_DEB BETWEEN %s AND %s
        #         AND DATE_FIN BETWEEN %s AND %s
        #     """
        #     dat_deb = datetime.strptime(dat_deb, '%m/%d/%Y').date()
        #     dat_fin = datetime.strptime(dat_fin, '%m/%d/%Y').date()
        #     inputs = (num_visiteur, num_chambre, dat_deb, dat_fin, dat_deb, dat_fin)



        cursor.execute(reservationQuery, inputs)
        results = cursor.fetchall()

        found_results = False
        for result in results:
            NUM_RESERVATION = result[1]
            NUM_VISITEUR = result[2]  
            NUM_CHAMBRE = result[3]   
            DATE_DEB = QDate.fromString(str(result[4]), "yyyy-MM-dd")  
            DATE_FIN = QDate.fromString(str(result[5]), "yyyy-MM-dd")  
            found_results = True

            self.Reservation_listWidget.addItem("NUM_RESERVATION: " + str(NUM_RESERVATION))
            self.Reservation_listWidget.addItem("NUM_VISITEUR: " + str(NUM_VISITEUR))
            self.Reservation_listWidget.addItem("NUM_CHAMBRE: " + str(NUM_CHAMBRE))
            self.Reservation_listWidget.addItem("DATE_DEB: " + DATE_DEB.toString("yyyy-MM-dd"))
            self.Reservation_listWidget.addItem("DATE_FIN: " + DATE_FIN.toString("yyyy-MM-dd") + "\n")

        if not found_results:
            self.Reservation_listWidget.clear()
            QtWidgets.QMessageBox.warning(self, '^_^', 'NOT FOUND !!')

        connection.commit()
        cursor.close()
        connection.close()



##############################################################################################################################################################################
    # DELETE BUTTON
    def delete_click(self):
        
        num_reservation = self.NUM_RESERVATION_input.text()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='hotel')  

        cursor = connection.cursor()
        if num_reservation == "":
            QtWidgets.QMessageBox.warning(   
                self, 'Input is empty', 'Please enter NUM VISITEUR to delete item.')
        else:
            query = "SELECT * FROM reservation WHERE NUM_RESERVATION = %s"
            params = (num_reservation,)

            cursor.execute(query, params)
            result = cursor.fetchone()
            if result is not None:
               msg_box = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this Reservation?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
               # If user click on the "Yes" button the item is deleted If not the item is not deleted.
               if msg_box == QtWidgets.QMessageBox.Yes:
                   query = "DELETE FROM reservation WHERE NUM_RESERVATION = %s"
                   cursor.execute(query, params)
                   connection.commit()
                   QtWidgets.QMessageBox.information(self, 'Success', 'reservation deleted successfully.')
            
               else:
                QtWidgets.QMessageBox.warning(
                    self, 'Error', 'reservation not found in the visiteur Table.')

        cursor.close()
        connection.close()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RESERVATIONMainWindow = Test()
    RESERVATIONMainWindow.show()
    sys.exit(app.exec_())