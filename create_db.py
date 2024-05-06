# code to construct and deconstruct the database
# fill database with dummy data
# Author: Elaine French
#
# Purpose: Running this file creates the file RecipEASYDB for the recipeasy app database. It pulls in data from CSV files to add initial data to the database for the team to have a db file to all work off of and for the web app to have a common db file with standard tables and values to work off of.
#######################
# To Use: execute this file by running
# python3 create_db.py
# the database file in your directory will now be up to date
# recipe dataset downloaded from https://www.kaggle.com/datasets/pes12017000148/food-ingredients-and-recipe-dataset-with-images?resource=download
##########################

import sqlite3
import os
import datetime

def create(db_filename):
    '''create a database for RecipEASY app
    There are 3 tables: recipesTable, loginTable, communityTable'''
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    # Create recipesTable - 9 fields
    recipesTable = """recipesTable(
                            Recipe_ID INT PRIMARY KEY, 
                            Name VARCHAR, 
                            Ingredients VARCHAR, 
                            Cooking_Time INT, 
                            Directions VARCHAR, 
                            Avg_Ratings decimal(3,2), 
                            Total_Rating_Submission INT, 
                            User_ID VARCHAR, 
                            Submit_Date INT,
        FOREIGN KEY (User_ID) REFERENCES loginTable(User_ID));"""
    
    # login table -- 5 fields
    loginTable = """loginTable(
                        User_ID VARCHAR PRIMARY KEY, 
                        Password VARCHAR, 
                        first_name VARCHAR, 
                        last_name VARCHAR, 
                        Email VARCHAR);"""
    
    # community table -- 5 fields
    communityTable = """communityTable(
                            Post_ID INT PRIMARY KEY, 
                            Post VARCHAR, 
                            Recipe_ID VARCHAR, 
                            User_ID VARCHAR,
                            Rating INT,
                            Post_Date INT,
        FOREIGN KEY (User_ID) REFERENCES loginTable(User_ID),
        FOREIGN KEY (Recipe_ID) REFERENCES recipesTable(Recipe_ID));"""
    
    tables = [recipesTable, loginTable, communityTable]
    for t in tables:
        c.execute("CREATE TABLE " + t)
        
    conn.commit()
    conn.close()
    
def fill_recipes(db_filename, csv_name):
    '''function to fill the recipe table database with dummy data from recipes.csv'''
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    
    with open(csv_name) as recipes_file:
        # put the header row in a separate variable
        first_line = recipes_file.readline()
        # read in the lines from the csv stripping white space characters
        # will read in as a list type
        recipes_list = [line.rstrip() for line in recipes_file]

    # in order for cursor.executemany to function the variabe should be a list of tuples
    recipe_data = []
    for item in recipes_list:
        new_item = item.split(",")
        new_item = tuple(new_item)
        recipe_data.append(new_item)
    #for item in recipe_data:
        #print(recipe_data)
    cursor.executemany("INSERT INTO recipesTable Values(?,?,?,?,?,?,?,?,?)",recipe_data)
    #cursor.execute("SELECT * FROM recipesTable;")
    #print(cursor.fetchall())
    db.commit()
    db.close()
    
def fill_login(db_filename, csv_name):
    '''function to fill the login table database with dummy data from login.csv'''
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    
    with open(csv_name) as file_handle:
        # put the header row in a separate variable
        first_line = file_handle.readline()
        # read in the lines from the csv stripping white space characters
        # will read in as a list type
        logins_list = [line.rstrip() for line in file_handle]

    # in order for cursor.executemany to function the variabe should be a list of tuples
    login_data = []
    for item in logins_list:
        new_item = item.split(",")
        new_item = tuple(new_item)
        login_data.append(new_item)
    
    cursor.executemany("INSERT INTO loginTable Values(?,?,?,?,?)",login_data)
    #cursor.execute("SELECT * FROM loginTable;")
    #print(cursor.fetchall())
    db.commit()
    db.close()

def fill_community(db_filename, csv_name):
    '''function to fill the community table in the database with dummy data from community.csv'''
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    
    with open(csv_name) as file_handle:
        # put the header row in a separate variable
        first_line = file_handle.readline()
        # read in the lines from the csv stripping white space characters
        # will read in as a list type
        community_list = [line.rstrip() for line in file_handle]

    # in order for cursor.executemany to function the variabe should be a list of tuples
    comm_data = []
    for item in community_list:
        new_item = item.split(",")
        new_item = tuple(new_item)
        comm_data.append(new_item)
    
    cursor.executemany("INSERT INTO communityTable Values(?,?,?,?,?,?)",comm_data)
    #cursor.execute("SELECT * FROM communityTable;")
    #print(cursor.fetchall())
    db.commit()
    db.close()

# Test that the database is created correctly
# Code to get the schema information from the database
def print_tables(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print ("\nTables:")
    for t in c.fetchall() :
        print ("\t[%s]"%t[0])

     ##   print ("\tColumns of", t[0])
        c.execute("PRAGMA table_info(%s);"%t[0])
        for attr in c.fetchall() :
            print ("\t\t", attr)
        
        print ("")

def print_tables_rows(dbname):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    print ("\nTable Values:")
    for t in tables :
        print ("\t[%s]"%t)
        
        sql = "SELECT * from %s ;"%t
        print ("\t\t\t<%s>"%sql)
        c.execute(sql)
        for row in c.fetchall() :
            print ("\t\t", row)
       
        print ("") 
    
    
## run the above functions to create and fill the database

db_filename ='RecipEASYDB'
recipe_csv = './csv/recipes.csv'
login_csv = './csv/logins.csv'
community_csv = './csv/community.csv'


# first remove the existing database file if it exists in the directory
try: 
    os.remove(db_filename)
except:
    pass

# now that the file is removed, replace it by running the above defined functions

create(db_filename)
fill_recipes(db_filename, recipe_csv)
fill_login(db_filename, login_csv)
fill_community(db_filename, community_csv)


print('Database updated, file created "RecipEASYDB.db"')

## uncomment the below function if you want to print out the tables created in a user friendly format
#print_tables(db_filename)
#print_tables_rows(db_filename)