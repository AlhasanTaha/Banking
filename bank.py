bank.db

import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chicken-4431",
    database="bank_db"
)
cursor = db.cursor()

def authenticate_account(account_number, pin):
    query = "SELECT * FROM accounts WHERE account_number = %s AND pin = %s"
    cursor.execute(query, (account_number, pin))
    account = cursor.fetchone()
    if account:
        return account
    else:
        return None

def check_balance(account_number):
    query = "SELECT balance FROM accounts WHERE account_number = %s"
    cursor.execute(query, (account_number,))
    balance = cursor.fetchone()
    if balance:
        return balance[0]
    else:
        return None

def deposit_funds(account_number, amount):
    current_balance = check_balance(account_number)
    if current_balance is not None:
        new_balance = current_balance + amount
        query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
        cursor.execute(query, (new_balance, account_number))
        db.commit()
        return new_balance
    else:
        return None

def withdraw_funds(account_number, amount):
    current_balance = check_balance(account_number)
    if current_balance is not None and current_balance >= amount:
        new_balance = current_balance - amount
        query = "UPDATE accounts SET balance = %s WHERE account_number = %s"
        cursor.execute(query, (new_balance, account_number))
        db.commit()
        return new_balance
    else:
        return None

def create_account(account_number, pin, name):
    query = "INSERT INTO accounts (account_number, pin, name, balance) VALUES (%s, %s, %s, 0)"
    cursor.execute(query, (account_number, pin, name))
    db.commit()

def close_account(account_number):
    query = "DELETE FROM accounts WHERE account_number = %s"
    cursor.execute(query, (account_number,))
    db.commit()

def modify_account(account_number, new_name, new_pin):
    query = "UPDATE accounts SET name = %s, pin = %s WHERE account_number = %s"
    cursor.execute(query, (new_name, new_pin, account_number))
    db.commit()

def main():
    print("Welcome to the Online Banking System")
    while True:
        print("\n1. Login\n2. Create New Account\n3. Exit
