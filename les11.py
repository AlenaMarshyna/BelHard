import sqlite3

conn = sqlite3.connect('db11.sqlite3')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(10)
    );
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24),
        email VARCHAR(24) UNIQUE
    );
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    status_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses(id) ON DELETE CASCADE
    );
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) UNIQUE
    );
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(36),
    description VARCHAR(140),
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
    );
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
        FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
    );
''')
conn.commit()

cur.execute('''
    INSERT INTO statuses(name)
    VALUES('buy');
''')
conn.commit()

cur.execute('''
    INSERT INTO users(name, email)
    VALUES(?, ?);
''', ('Andr', 'and@gmail.com'))
conn.commit()

cur.execute('''
    INSERT INTO categories(name)
    VALUES('prod1');
''')
conn.commit()

cur.execute('''
    INSERT INTO products(title, description)
    VALUES(?, ?);
''', ('AA', 'aa'))
conn.commit()

