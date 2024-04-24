import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(user_id, password, first_name, last_name, email):
    """Create a new user in the loginTable."""
    result = False
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    hashed_password = generate_password_hash(password)
    try:
        cursor.execute("INSERT INTO loginTable (User_ID, Password, first_name, last_name, Email) VALUES (?, ?, ?, ?, ?)",
                       (user_id, hashed_password, first_name, last_name, email))
        db.commit()
        result = True
    except Exception as e:
        print("An error occurred:", e)
    finally:
        db.close()
    return result

def validate_login(user_id, password):
    """Validate a user's login credentials."""
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    cursor.execute("SELECT Password FROM loginTable WHERE User_ID = ?", (user_id,))
    stored_password = cursor.fetchone()
    db.close()
    if stored_password and check_password_hash(stored_password[0], password):
        return True
    return False

def update_user(user_id, new_password=None, new_email=None):
    """Update user details such as password or email."""
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    if new_password:
        new_password_hash = generate_password_hash(new_password)
        cursor.execute("UPDATE loginTable SET Password = ? WHERE User_ID = ?", (new_password_hash, user_id))
    if new_email:
        cursor.execute("UPDATE loginTable SET Email = ? WHERE User_ID = ?", (new_email, user_id))
    db.commit()
    db.close()
    return "User updated successfully"


def delete_user(user_id):
    """Delete a user from the loginTable."""
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    cursor.execute("DELETE FROM loginTable WHERE User_ID = ?", (user_id,))
    db.commit()
    db.close()
    return "User deleted successfully"
