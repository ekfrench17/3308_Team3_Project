###############################################################################
## These are the access methods for the recipes table for RecipEASY DB
##
## Instructions:
## 
## 
###############################################################################


###############################################################################

import sqlite3
from sqlite3 import Error
import random
import datetime
import SQL_Insert_test


def add_recipe(recipe_name, ingredients, cook_time, directions, avg_ratings, count_submissions, user_id, db_filename='RecipEASYDB'):
    '''add a new recipe to the recipes table
    return True if successful, False otherwise'''
    #db = getattr(g, '_database', None)
    success = False
    
    db = sqlite3.connect(db_filename)
    cursor = db.cursor()
    
    # set up variables for testing conditions before inserting to table
    # check categoryID exists in category table
    cursor.execute("SELECT user_id FROM loginTable")
    Ids = cursor.fetchall() # returns: [(1,), (2,), (3,)]
    check = []
    
    for item in Ids:
        check.append(item[0])
    
    # check the recipe does not already exist    
    all_recipes = get_all_recipes()
    
    # make sure recipe_name is a string and not empty
    if(type(recipe_name) != str):
        message = "recipe name must be text string"
        #raise ValueError
    elif(recipe_name == ''):
        message = "recipe name can not be empty"
        #raise ValueError
        
    # check cooking time is an integer above 0
    elif(type(cook_time) != int):
        message = "cooking time must be an integer"
        #raise ValueError
    elif(cook_time < 0):
        message = "cooking time must be greater than 0"
        #raise ValueError
    # Check the user is in the database
    elif user_id not in check:
        message = "User not found in database, need valid ID to submit recipe"
        #raise ValueError
    # check the recipe name does not exist yet
    elif recipe_name in all_recipes:
        message = "recipe name already exists"
    # if all passes, add to table
    else:
            # get last recipe id and increment by one for next item
            cursor.execute("SELECT recipe_id FROM recipesTable ORDER BY recipe_id DESC")
            last_id = cursor.fetchone()
            new_id = last_id[0] + 1

            # insert into table
            ##Initializing variables that aren't relevant to inserting a recipes table
            avg_ratings = 0
            count_submissions = 0
            cursor.execute("INSERT INTO RecipesTable Values(?,?,?,?,?,?,?,?,?);",(
                                                                new_id,
                                                                recipe_name,
                                                                ingredients,
                                                                cook_time,
                                                                directions,
                                                                avg_ratings,
                                                                count_submissions,
                                                                user_id,
                                                            datetime.datetime.now().timestamp()                                             
                )) 
            #cursor.execute("SELECT * FROM RecipesTable;")
            #test_output = cursor.fetchall()
            #test_output = [str(val) for val in test_output]
            db.commit()
            success = True
    db.close()
    if success == True:
        message = "Recipe successfully added!"
    return(success, message)

def get_recipe_data(recipe_name):
    '''function to pull recipe data from the recipestable based on the recipe_name
    function returns a list where each item is a column from the table'''
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    
    # make sure recipe exists in table
    cursor.execute("SELECT name FROM recipesTable")
    names = cursor.fetchall()
    check = []
    for item in names:
        check.append(item[0])
    if recipe_name not in check:
        recipe = None
    else:
        cursor.execute("""SELECT * FROM RecipesTable WHERE name=?""",(recipe_name,))
        recipe = cursor.fetchall()
        #recipe = [str(val) for val in recipe]
    db.close()
    if recipe == None:
        recipe = None
    else:
        # convert the returned item to a proper list to be parsed
        recipe = list(recipe[0])#.strip(')(').split(',')
        recipe[2] = recipe[2].strip(']["').split(".")
        recipe[4] = recipe[4].split(".")

    return recipe

def my_recently_added(user_id):
    '''function to return the 5 most recent recipes added by a given user
    return type is a list'''
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    #Select up to 5 of the most recent recipes a user has added order by most recent to oldest.
    cursor.execute('SELECT * FROM recipesTable where User_ID=? order by Submit_Date DESC LIMIT 5;',(user_id,))
    my_recipes = cursor.fetchall()
    #Capture a tuple of all 5 recipes
    my_recipes= [str(val[1]) for val in my_recipes]
    #print(str(my_recipes))
    return my_recipes

def get_recipes_by_user(user_id):
    '''function to return the saved recipes of a given user
    return type is a list'''
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    # select the user_id column from the recipes table
    cursor.execute("SELECT name FROM recipesTable WHERE user_id=?",(user_id,))
    # get a list of all recipes from the table
    my_recipes = cursor.fetchall()
    # remove the tuple to return strings using list comprehension
    my_recipes = [str(val[0]) for val in my_recipes]
    return my_recipes

def my_recently_added(user_id):
    '''function to return the 5 most recent recipes added by a given user
    return type is a list'''
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    #Select up to 5 of the most recent recipes a user has added order by most recent to oldest.
    cursor.execute('SELECT * FROM recipesTable where User_ID=? order by Submit_Date DESC LIMIT 5;',(user_id,))
    my_recipes = cursor.fetchall()
    #Capture a tuple of all 5 recipes
    my_recipes= [str(val[1]) for val in my_recipes]
    #print(str(my_recipes))
    return my_recipes
    
def delete_recipe(recipe_name):
    '''function to delete a recipe in the table'''
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    try:
        sql_del = cursor.execute("DELETE FROM recipesTable WHERE name = ?",(recipe_name,))
        result = "Total records affected: ", sql_del.rowcount
        #cursor.execute(sql_del)
        db.commit()
    except Error as e:
        result = f"Oops! Something went wrong. Error: {e}"
        # reverse the change in case of error
        db.rollback()
    return result

def get_all_recipes():
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    # select the name column from the recipes table
    cursor.execute("SELECT name FROM recipesTable")
    # get a list of all recipes from the table
    all_recipes = cursor.fetchall()
    # remove the tuple to return strings using list comprehension
    all_recipes = [str(val[0]) for val in all_recipes]
    return all_recipes

def create_recipesTable(db_filename):
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
    
    c.execute("CREATE TABLE " + recipesTable)
        
    conn.commit()
    conn.close()
    
#recipe = get_recipe_data("Warm Comfort")

#delete_recipe("homemade_pizza")
#test_my_recently_added = my_recently_added("garci446")


