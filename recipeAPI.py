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



def add_recipe(recipe_name, ingredients, cook_time, directions, avg_ratings, count_submissions, user_id):
    '''add a new recipe to the recipes table'''
    #db = getattr(g, '_database', None)
     
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    
    # make sure recipe_name is a string and not empty
    if(type(recipe_name) != str):
        raise ValueError
    elif(recipe_name == ''):
        raise ValueError
        
    # check cooking time is an integer above 0
    if(type(cook_time) != int):
        raise ValueError
    elif(cook_time < 0):
        raise ValueError
    
    # increment next recipe_id
    # check categoryID exists in category table
    cursor.execute("SELECT user_id FROM loginTable")
    Ids = cursor.fetchall() # returns: [(1,), (2,), (3,)]
    check = []
    for item in Ids:
        check.append(item[0])
    if user_id not in check:
        raise ValueError
    
    # check the recipe does not already exist
    all_recipes = get_all_recipes()
    if recipe_name in all_recipes:
        result = "try again, recipe name already exists"
    else:
        # get last recipe id and increment by one for next item
        cursor.execute("SELECT recipe_id FROM recipesTable ORDER BY recipe_id DESC")
        last_id = cursor.fetchone()
        new_id = last_id[0] + 1

        # insert into table
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
        cursor.execute("SELECT * FROM RecipesTable;")
        test_output = cursor.fetchall()
        test_output = [str(val) for val in test_output]
        db.commit()
    db.close()
    return(test_output)

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

def my_recipes(user_id):
    '''function to return the saved recipes of a given user
    return type is a list'''
    
def delete_recipe(recipe_name):
    '''function to delete a recipe in the table'''
    db = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    try:
        sql_del = cursor.execute("DELETE FROM recipesTable WHERE name = ?",(recipe_name,))
        print("Total records affected: ", sql_del.rowcount)
        #cursor.execute(sql_del)
        db.commit()
    except Error as e:
        print(f"Oops! Something went wrong. Error: {e}")
        # reverse the change in case of error
        db.rollback()

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


    
#recipe = get_recipe_data("Warm Comfort")

#delete_recipe("homemade_pizza")


