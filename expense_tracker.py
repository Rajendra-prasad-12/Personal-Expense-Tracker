from db import connect
from datetime import date

def add_expense(amount, category, description):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (%s, %s, %s, %s)",
                   (amount, category, description, date.today()))
    conn.commit()
    conn.close()
    print("✅ Expense added!")

def view_expenses():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# CLI Interface
while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        amt = float(input("Amount: "))
        cat = input("Category: ")
        desc = input("Description: ")
        add_expense(amt, cat, desc)
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        break
