import sqlite3

conn = sqlite3.connect('les10/db.sqlite3')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS shows
              (
              title TEXT, director TEXT, year INT
              );
''')

conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER,name VARCHAR(32),
    price DECIMAL(7, 2) NOT NULL DEFAULT(0.0),
    show_title TEXT NOT NULL,
    FOREIGN KEY (show_title) REFERENCES shows(title)
    ON DELETE CASCADE
    );
''')

conn.commit()
