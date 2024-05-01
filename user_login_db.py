"""
File: user_login_db.py
Author: JonPaul Ferzacca
GitHub: JPFerzacca
Description: This module handles user management operations such as creating, validating,
             updating, and deleting user information in the 'RecipEASYDB' SQLite database.
             It uses the werkzeug.security module for password hashing to ensure security.

References:
    Password Hashing Functions:
    - werkzeug.security - https://werkzeug.palletsprojects.com/en/2.0.x/utils/#module-werkzeug.security
    - Understanding Password Hashing - https://www.youtube.com/watch?v=8ebIEefhBpM

    Code Structure and Best Practices:
    - Effective Python Code Structure - https://youtu.be/v3CSQkPJtAc
"""

import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Inserts a new user into the loginTable with hashed password and user details.
def create_user(user_id, password, first_name, last_name, email):
    result = False
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    hashed_password = generate_password_hash(password)  # Securely hash the password before storage
    try:
        cursor.execute("INSERT INTO loginTable (User_ID, Password, first_name, last_name, Email) VALUES (?, ?, ?, ?, ?)",
                       (user_id, hashed_password, first_name, last_name, email))
        db.commit()
        result = True
    except Exception as e:
        print("An error occurred:", e)  # Consider using logging
    finally:
        db.close()
    return result

# Checks the provided password against the stored hash for the given user_id.
def validate_login(user_id, password):

    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    cursor.execute("SELECT Password FROM loginTable WHERE User_ID = ?", (user_id,))
    stored_password = cursor.fetchone()
    db.close()
    return stored_password and check_password_hash(stored_password[0], password)


# Updates user's password and/or email in the database based on provided data.
def update_user(user_id, new_password=None, new_email=None):

    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    if new_password:
        new_password_hash = generate_password_hash(new_password)  # Update password with a new hashed value
        cursor.execute("UPDATE loginTable SET Password = ? WHERE User_ID = ?", (new_password_hash, user_id))
    if new_email:
        cursor.execute("UPDATE loginTable SET Email = ? WHERE User_ID = ?", (new_email, user_id))
    db.commit()
    db.close()
    return "User updated successfully"


# Removes a user from the database by their user ID.
def delete_user(user_id):

    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    cursor.execute("DELETE FROM loginTable WHERE User_ID = ?", (user_id,))
    db.commit()
    db.close()
    return "User deleted successfully"