import sqlite3
import Constants

conn = sqlite3.connect(Constants.databasePath)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS apod(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT,
               title TEXT,
               explanation TEXT,
               filename TEXT,
               image_path TEXT
               )
""" )
conn.commit()

def store_metadata(data):
    conn = sqlite3.connect(Constants.databasePath)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO apod (date, title, explanation, filename, image_path)
    VALUES (?, ?, ?, ?, ?)
    """, (data['date'], data['title'], data['explanation'], data['filename'], data['image_path']))
    
    conn.commit()
    conn.close()