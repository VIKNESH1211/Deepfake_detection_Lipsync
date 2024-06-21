import sqlite3
conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
''')
cursor.execute("INSERT OR REPLACE INTO users (username, password) VALUES (?, ?)", ('user1', 'your_password_here'))
conn.commit()
conn.close()
