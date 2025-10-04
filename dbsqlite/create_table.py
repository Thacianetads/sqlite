import sqlite3


conn = sqlite3.connect('carros.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS carros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelo TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER NOT NULL
)
''')
conn.commit()
conn.close()