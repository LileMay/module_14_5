import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL)
    """)
    connection.commit()
initiate_db()

def initiate_db():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL)
    """)
    connection.commit()
initiate_db()

cursor.execute("DELETE FROM Products")
for i in range(1, 5):
    cursor.execute('INSERT INTO Products(title, description, price) VALUES(?, ?, ?)',
                           (f"Product: {i}", f"Описание: {i}", f"Цена: {i * 100}"))

    def get_all_products():
        cursor.execute('SELECT * FROM Products')
        return cursor.fetchall()

    connection.commit()

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?,?,?, 1000)',
                   (username, email, age))
    connection.commit()

def is_included(username):
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for user in users:
        if user [1] == username:
            return True
    return False


connection.commit()