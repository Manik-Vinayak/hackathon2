import sqlite3

# Connect to database (it will create items.db if it doesn't exist)
conn = sqlite3.connect('items.db')
c = conn.cursor()

# Create items table
c.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    image TEXT NOT NULL,
    location TEXT NOT NULL,
    status TEXT DEFAULT 'lost',
    date TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("✅ Database and table 'items' created successfully.")
