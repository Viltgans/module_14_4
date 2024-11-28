import sqlite3

def initiate_db():
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products(id, title, description, price) VALUES(?, ?, ?, ?)",
                       (i, f'Продукт{i}', f'Описание{i}', f'{i * 100}'))
    connect.commit()
    connect.close()

def get_all_products():
    connect = sqlite3.connect('products.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connect.commit()
    connect.close()
    return products
