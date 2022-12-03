import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()


cur.execute('''
    CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER NOT NULL PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER    
    );
''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
    title VARCHAR(36),
    description VARCHAR(140),
    category_id INTEGER,
    id INTEGER NOT NULL PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES order_items(id)
    ON DELETE CASCADE
    );
''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
    name VARCHAR(24) UNIQUE,
    id INTEGER NOT NULL PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES products(id)
    ON DELETE CASCADE
    );
''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    user_id INTEGER,
    status_id INTEGER,
    id INTEGER NOT NULL PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES order_items(id)
    ON DELETE CASCADE
    );
''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS statuses(
    name VARCHAR(10) UNIQUE,
    id INTEGER NOT NULL PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES orders(id)
    ON DELETE CASCADE
    );
''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
    name VARCHAR(24),
    email VARCHAR(24) UNIQUE,
    id INTEGER NOT NULL PRIMARY KEY,
    FOREIGN KEY (id) REFERENCES orders(id)
    ON DELETE CASCADE
    );
''')
conn.commit()
