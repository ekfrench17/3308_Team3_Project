############################################################################
## Unit tests for Login Table functionality
## This file contains unit tests for the functions in user_login_db.py
############################################################################

import os
import unittest
import sqlite3
import random
from werkzeug.security import generate_password_hash, check_password_hash

from user_login_db import create_user, validate_login, update_user, delete_user
import subprocess
from unit_test_helper_functions import establish_db_connection, close_db_connection


class Test_loginTable (unittest.TestCase):
    def setUp(self):
        
        database_path = os.path.join(os.getcwd(),'RecipEASYDB')
        if not os.path.exists(database_path):
            create_db_file_path = "./create_db.py"
            subprocess.run(["python3", create_db_file_path])
       
    def test_table_creation(self):
        pass
    
    def test_create_user(self):
        '''test that the create_user function successfully adds a user to the table'''
        
        ## setting a new unique user to be passed to the table
        user = "test_user"
        password = "password"
        first_name = "test"
        last_name = "user"
        user_email = "test_user@colorado.edu"
        
        ## check to see if the user was able to be added to db
        self.assertEqual(create_user(user, password, first_name, last_name, user_email), True, "Test to add unique user has not passed")
        
        db, cursor = establish_db_connection()
        ##Clear any reference to test user
        cursor.execute("Delete from loginTable where User_ID=?;",(user,))
        db.commit()
        close_db_connection(db)
        
    def test_user_exists(self):
        '''test that creating a new user is unique
        is a user id is added that already exists, inserting into the table should fail'''
        
        ## set up test data that should already exist in the DB
        user = "garci446"
        password = "pbkdf2:sha256:260000$fbqtDfUCqW2ToBn5$44524276f619874f02e7dbe575a99de237634d794eb845d8298d1531fa3b81a8" #hashed password
        first_name = "Carlos"
        last_name = "Garcia"
        user_email = "garci446@colorado.edu"
        
        ## check to see if the user was unable to be added to db as it already exists
        self.assertNotEqual(create_user(user, password, first_name, last_name, user_email), (True, 'User successfully added!'), "Test to avoid adding duplicate user names has not passed")

    def test_validate_login(self):
        '''test given password compared to hashed password'''
        
        #set test data
        user = "Knox"
        password = 'test_password'
        first = "D"
        last = "Knox"
        email = "knox@gmail.com"


        result_msg = create_user(user,password,first,last,email)
        
        db, cursor = establish_db_connection()
        
        cursor.execute("SELECT password FROM loginTable WHERE User_ID=?",(user,))
        test_password = cursor.fetchone()
        test_password = test_password[0]
        
        self.assertEqual(check_password_hash(test_password, password),True,"test to validate password on login failed")

    def test_update_user(self):
        
        ##Create test data
        user = "test_user_2"
        password = "password123"
        first_name = "test_2"
        last_name = "user"
        user_email = "test_user2@colorado.edu"
        
       
        result = create_user(user, password, first_name, last_name, user_email)
        self.assertEqual(result,True,"create user before updating did not pass")
        
        ## test to see if updating the user password is successful
        new_password = "new_password"
        result_msg = update_user(user, new_password, None)
        
        db, cursor = establish_db_connection()
        cursor.execute("SELECT password FROM loginTable WHERE User_ID=?",(user,))
        test_output = cursor.fetchone()
        test_output = test_output[0]
        
        self.assertEqual(check_password_hash(test_output, new_password), True, "Test to confirm password change did not pass")
        
        ## test to see if updating the user email is successful
        new_email = "test_user2@gmail.com"
        result_msg = update_user(user, None, new_email)
        cursor.execute("SELECT email FROM loginTable WHERE User_ID=?",(user,))
        test_output = cursor.fetchone()
        test_output = test_output[0]
        self.assertEqual(test_output, new_email, "Test to confirm email change did not pass")
        
        ##Clear any reference to recipes under the user "test user for future testing"
        cursor.execute("Delete from loginTable where User_ID=?;",(user,))
        db.commit()
        close_db_connection(db)

    def test_delete_user(self):
        ##Create test data
        
        user = "test_user"
        password = "password"
        first_name = "test"
        last_name = "user"
        user_email = "test_user@colorado.edu"

        result = create_user(user, password, first_name, last_name, user_email)
        self.assertEqual(result,True,"create user before deleting did not pass")
        
        ## set up to compare if user is deleted
        result_msg = delete_user(user)
        
        db, cursor = establish_db_connection()
        cursor.execute("SELECT User_ID FROM loginTable WHERE User_ID=?",(user,))
        result = cursor.fetchone()
        close_db_connection(db)
        
        # test to see if user is successfully deleted 
        self.assertEqual(result,None,"Delete user test failed")
        

    def test_field_type_verification(self):
        ##Pull the loginTable schema/columns
        db, cursor = establish_db_connection()
        cursor.execute("select sql from sqlite_master where type='table' and name='loginTable';")
        login_table_info = cursor.fetchall()
        close_db_connection(db)

        ##parse through the loginTable schema/columns to pull column that contains the primary key
        login_table_columns = login_table_info[0][0]
        login_table_columns = login_table_columns.split("\n")
        primary_key_column_info = ""
        for line in login_table_columns:
            if "PRIMARY KEY" in line:
                primary_key_column_info = line.strip()

        ##Asses that 'User_ID' is contained in the same column value that the Primary Key was found. Pretty much make sure the primary key is User_ID
        self.assertTrue("User_ID" in primary_key_column_info, "User_ID is not the primary key in the loginTable")


if __name__ == '__main__':
    unittest.main()