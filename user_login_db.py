import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(db_filename, user_id, username, password, first_name, last_name, email):
    """Create a new user in the loginTable."""
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    hashed_password = generate_password_hash(password)
    try:
        cursor.execute("INSERT INTO loginTable (User_ID, Username, Password, first_name, last_name, Email) VALUES (?, ?, ?, ?, ?, ?)",
                       (user_id, username, hashed_password, first_name, last_name, email))
        db.commit()
    except sqlite3.IntegrityError:
        return "Username or Email already exists"
    finally:
        db.close()
    return "User created successfully"

def validate_login(db_filename, username, password):
    """Validate a user's login credentials."""
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    cursor.execute("SELECT Password FROM loginTable WHERE Username = ?", (username,))
    stored_password = cursor.fetchone()
    db.close()
    if stored_password and check_password_hash(stored_password[0], password):
        return True
    return False

def update_user(db_filename, username, new_password=None, new_email=None):
    """Update user details such as password or email."""
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    if new_password:
        new_password_hash = generate_password_hash(new_password)
        cursor.execute("UPDATE loginTable SET Password = ? WHERE Username = ?", (new_password_hash, username))
    if new_email:
        cursor.execute("UPDATE loginTable SET Email = ? WHERE Username = ?", (new_email, username))
    db.commit()
    db.close()
    return "User updated successfully"

def delete_user(db_filename, username):
    """Delete a user from the loginTable."""
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    cursor.execute("DELETE FROM loginTable WHERE Username = ?", (username,))
    db.commit()
    db.close()
    return "User deleted successfully"
