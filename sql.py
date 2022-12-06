import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) NOT NULL UNIQUE,
        is_published BOOLEAN DEFAULT(false)
    );
''')
conn.commit()

cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(24) NOT NULL,
        descr VARCHAR(1024),
        price DECIMAL(7, 2) NOT NULL DEFAULT(0.0),
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES categories(id)
        ON DELETE CASCADE
    );
''')
conn.commit()

cur.execute('''
    INSERT INTO 
''')