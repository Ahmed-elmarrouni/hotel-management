````markdown
# Hotel Management Application

## Overview

This Python-based **Hotel Management Application** is developed using **PyQt5** and **Qt Designer**. The application aims to streamline hotel operations by providing an efficient and user-friendly interface for managing reservations, guests, rooms, and other essential hotel functions.

### Features

- **Guest Management**: Add, edit, and manage guest information.
- **Room Management**: Track room availability, assign rooms to guests, and manage room details.
- **Reservation System**: Handle reservations, check-ins, and check-outs.
- **Billing and Invoicing**: Generate bills and invoices for guests.

---

## Key Features

### 1. **Input Validation**

- **Phone Number**: Ensures the phone number is exactly 10 digits using regex.
- **Email**: Checks for a valid email format using regex.
- Displays error messages if required fields are left empty.

### 2. **CRUD Operations**

- **Add**: Inserts new records into the database, ensuring all fields are validated before submission.
- **Search**: Fetches and displays details based on unique identifiers (`NUM_RESERVATION` or `NUM_VISITEUR`).
- **Delete**: Provides a confirmation dialog before deletion and checks if the record exists before proceeding.

### 3. **User Experience**

- Uses `QtWidgets.QMessageBox` for user feedback, error messages, and confirmations.
- Clears input fields after operations like deletion or when the search yields no results.

---

## Screenshots

### Chambre Screen

![Chambre Screen](./Readme-imgs/image.png)

### Client List

![Client List](./Readme-imgs/image-1.png)

### Display All Reservations

![Display All Reservations](./Readme-imgs/image-2.png)

### Display All Available Rooms

![Display All Available Rooms](./Readme-imgs/image-3.png)

### Visiteurs

![Visiteurs](./Readme-imgs/image-4.png)

---

## Technologies Used

- **PyQt5**: For the graphical user interface.
- **MySQL**: For data storage.
- **Python**: For application logic and database interaction.

---

## Strengths

- **Code Organization**: Logical separation of features into functions (`add_click`, `search_click`, `delete_click`).
- **Validation**: Comprehensive input validation minimizes errors during database operations.
- **User Feedback**: Confirmation dialogs and message boxes improve user interaction and clarity.
- **Modular SQL Queries**: Parameters (`%s`) in queries enhance security by preventing SQL injection.

---

## Suggestions for Improvement

### 1. **Connection Management**

Currently, database connections are opened and closed within each function. This approach works but can be inefficient in larger applications. Consider using a **database connection pool** or a centralized connection handler.

### 2. **Error Handling**

There is minimal handling for database-related errors. Implement error handling for cases like:

- Database connection failure.
- SQL execution errors (e.g., duplicate entries, constraint violations).

Example:

```python
try:
    connection = mysql.connector.connect(...)
    # Execute SQL queries
except mysql.connector.Error as e:
    QtWidgets.QMessageBox.critical(self, 'Database Error', f"An error occurred: {e}")
finally:
    connection.close()
```
````

### 3. **Code Duplication**

Some code segments, such as repeated `QMessageBox` calls and query executions, can be refactored into helper functions. For example:

```python
def show_message(self, title, message, icon=QtWidgets.QMessageBox.Information):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.exec_()
```

### 4. **Database Schema**

Ensure the schema for `reservation` and `visiteur` tables includes appropriate constraints like:

- Primary keys (`NUM_RESERVATION`, `NUM_VISITEUR`).
- Unique constraints (e.g., `CIN` for `visiteur`).
- Data types that match expected input.

---

## School Project Context

Since this is a school project, it demonstrates your understanding of:

- GUI design principles.
- Basic SQL operations (CRUD).
- Validation and error handling in software.

To enhance your project further:

- Add more advanced SQL features (e.g., joins, stored procedures).
- Implement data export functionality (e.g., export search results to CSV).

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

```
