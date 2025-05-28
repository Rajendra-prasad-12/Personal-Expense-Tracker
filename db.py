import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="Personal_expense_tracker"
    )  
