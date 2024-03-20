# SQL file for RecipEASY database API set up

import sqlite3

def create(db_filename): 
    conn = None
    try:
        conn = sqlite3.connect(db_filename)
        print(f"Connected to SQLite database {db_filename}")

        # Create tables
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS Recipe_Title (
                RecipeID INT PRIMARY KEY,
                Servings INT,
                Name VARCHAR
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS Meta_Data (
                idRecipe INT PRIMARY KEY,
                Author VARCHAR,
                CategoryID INT,
                Description VARCHAR
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS Ingredients_Instructions (
                idCategory INT PRIMARY KEY,
                Item VARCHAR,
                Amount DECIMAL,
                Directions VARCHAR
            )
        """)
        conn.commit()
        prCyan("Tables have been successfully created.")

    except Error as e:
        print(f"Error create function: {e}")
    finally:
        if conn:
            conn.close()
            prGreen("Connection closed.")
            print()