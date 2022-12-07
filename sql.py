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

cur.executemany('''
    INSERT INTO categories(name, is_published)
    VALUES(?, ?);
''', (('prod1', True), ('prod2', True)))
conn.commit()

# cur.executemany('''
#     INSERT INTO products(name, price, category_id)
#     VALUES(?, ?, ?);
# ''', (('food1', 1000.20), ('food2', 2000.10)))
# conn.commit()
