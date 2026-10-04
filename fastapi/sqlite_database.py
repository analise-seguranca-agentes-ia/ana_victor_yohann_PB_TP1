import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

connection.commit()
cursor.close()
connection.close()
