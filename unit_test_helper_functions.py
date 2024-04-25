import sqlite3

def establish_db_connection():
        db = sqlite3.connect('RecipEASYDB')
        cursor = db.cursor()
        return db, cursor

def close_db_connection(db):
        db.close()
        print("DB connection closed")