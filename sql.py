# import sqlite3
#
# conn = sqlite3.connect('db.sqlite3')
# cur = conn.cursor()
# # рекурсивная ссылка
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS categories(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(24) NOT NULL UNIQUE,
#         is_published BOOLEAN DEFAULT(false),
#         reference_id INTEGER,
#         FOREIGN KEY (reference_id) REFERENCES categories(id) ON DELETE CASCADE
#     );
# ''')
# conn.commit()
#
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS products(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(24) NOT NULL,
#         descr VARCHAR(1024),
#         price DECIMAL(7, 2) NOT NULL DEFAULT(0.0),
#         category_id INTEGER NOT NULL,
#         FOREIGN KEY (category_id) REFERENCES categories(id)
#         ON DELETE CASCADE
#     );
# ''')
# conn.commit()
#
# cur.executemany('''
#     INSERT INTO categories(name, is_published)
#     VALUES(?, ?);
# ''', (('prod1', True), ('prod2', True)))
# conn.commit()
#
# # cur.executemany('''
# #     INSERT INTO products(name, price)
# #     VALUES(?, ?, ?);
# # ''', (('food1', 1000.20), ('food2', 2000.10)))
# # conn.commit()


import sqlite3


conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS categories(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32) NOT NULL UNIQUE,
        is_published BOOLEAN DEFAULT(false)
    );
''')
conn.commit()
cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(32) NOT NULL,
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
''', (('Food', True), ('Drinks', True)))
conn.commit()
cur.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(64) NOT NULL,
        email VARCHAR(64) NOT NULL UNIQUE,
        referrer_id INTEGER,
        FOREIGN KEY (referrer_id) REFERENCES users(id) ON DELETE NO ACTION
    );
''')
conn.commit()
cur.execute('''
    UPDATE categories
    SET name = ?,
    is_published = ?
    WHERE id = 2;
''', ('Meat', False))
conn.commit()
cur.execute('''
    ALTER TABLE users ADD surname VARCHAR(32);
''')
conn.commit()
cur.execute('''
    DELETE FROM users WHERE name LIKE 'v%';
''')
conn.commit()

cur.execute('''
    SELECT * FROM categories ORDER BY name ASC, id DESC;
''')
print(cur.fetchall())


cur.execute('''
    SELECT categories.name, products.name, products.descr, products.price FROM categories
    JOIN products ON products.category_id = categories.id
    WHERE categories.is_published = true AND products.price > 100;
''')
print(cur.fetchall())