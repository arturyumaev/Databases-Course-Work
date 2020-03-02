import sqlite3

# Create database for catalog of clothing
conn = sqlite3.connect('./database/catalog.db')

c = conn.cursor()

conn.close()