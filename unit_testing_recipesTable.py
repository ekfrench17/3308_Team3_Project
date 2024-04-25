############################################################################
## Unit tests for recipesTable functionality
## This file contains unit tests for the functions in community_posts_db.py
############################################################################

import os
import unittest
import sqlite3
import random
from recipeAPI import add_recipe, get_recipe_data, my_recently_added, get_recipes_by_user
from user_login_db import create_user
import subprocess
from unit_test_helper_functions import establish_db_connection, close_db_connection


class Test_recipesTable (unittest.TestCase):
    def setUp(self):
        
        database_path = os.path.join(os.getcwd(),'RecipEASYDB')
        if not os.path.exists(database_path):
            create_db_file_path = "./create_db.py"
            subprocess.run(["python3", create_db_file_path])
    def test_add_recipe(self):
        
        ##set up test data of a recipe that should already exist in the DB
        recipe_name = "Warm Comfort"
        ingredients = "2 chamomile tea bags.1 oz reposado tequila.1/2 oz fresh lemon juice.1 Tbsp agave nectar"
        cook_time = 5
        directions = "Place 2 chamomile tea bags in a heatsafe vessel such as a large liquid measuring cup. Pour in 1 1/2 cups boiling water and let steep 5 minutes  then remove tea bags. Add 1 oz reposado tequila 1/2 oz fresh lemon juice and 1 Tbsp agave nectar and stir until incorporated. Pour into a 16-ounce insulated mug (or two smaller 8-ounce mugs) and drink hot."
        user_id = "garci446"

        ## check to see if the recipe was unable to be added to db as it already exists
        self.assertNotEqual(add_recipe(recipe_name, ingredients, cook_time, directions, 0, 0, user_id), (True, 'Recipe successfully added!'), "Test to avoid adding duplicate recipe names has not passed")

        ## setting a new recipe unique recipe to be passed to the table
        recipe_name = "Test: Unique Recipe"
        db, cursor = establish_db_connection()
        cursor.execute("Delete from recipesTable where Name='Test: Unique Recipe';")
        db.commit()
        close_db_connection(db)
        
        ## check to see of the recipe was able to be added to db as it is unique
        self.assertEqual(add_recipe(recipe_name, ingredients, cook_time, directions, 0, 0, user_id), (True, 'Recipe successfully added!'), "Test to add unique named recipe names has not passed")

    def test_get_recipe_data(self):
        
        #set test data
        ingredients = "2 chamomile tea bags.1 oz reposado tequila.1/2 oz fresh lemon juice.1 Tbsp agave nectar"
        cook_time = 5
        directions = "Place 2 chamomile tea bags in a heatsafe vessel such as a large liquid measuring cup. Pour in 1 1/2 cups boiling water and let steep 5 minutes  then remove tea bags. Add 1 oz reposado tequila 1/2 oz fresh lemon juice and 1 Tbsp agave nectar and stir until incorporated. Pour into a 16-ounce insulated mug (or two smaller 8-ounce mugs) and drink hot."
        user_id = "garci446"

        db, cursor = establish_db_connection()
        ##Clear any reference to the recipe "Recipe should not exist" from the table
        cursor.execute("Delete from recipesTable where Name='Recipe should not exist';")
        db.commit()
        close_db_connection(db)

       ##Test to see if we get a type error (or a None Object) respone when searching for a recipe that shouldn't exist
        with self.assertRaises(TypeError):
            recipe_name = "Recipe should not exist"
            get_recipe_data(recipe_name)[1]
        
        ##Add a recipe to the db and test search function to see if the recipe will be returned
        recipe_name = "Test: Search Recipe"
        add_recipe(recipe_name, ingredients, cook_time, directions, 0, 0, user_id)
        self.assertEqual(get_recipe_data(recipe_name)[1],recipe_name,"Test to search for recipe '{}' did not pass".format(recipe_name))

    def test_my_recently_added(self):
        ##Create test data

        user_id = "test user"
        user_email = user_id + "@gmail.com"
        result = create_user(user_id, user_id, user_id, user_id, user_email)
        print("User created == {}".format(result))

        test_recipe_names_list= []
        incrament = 1

        while incrament < 6:
            test_recipe_names_list.append(str(incrament))
            add_recipe(str(incrament), str(incrament), incrament, str(incrament), 0, 0, user_id)
            incrament += 1
        test_recipe_names_list.reverse()
        self.assertEqual(my_recently_added(user_id),test_recipe_names_list, "This test to confirm 5 most recent recipes submitted by a user did not pass")
        
        db, cursor = establish_db_connection()
        ##Clear any reference to the recipe "Recipe should not exist" from the table
        cursor.execute("Delete from recipesTable where User_ID=(?);", (user_id,))
        cursor.execute("Delete from loginTable where User_ID=(?);", (user_id,))
        db.commit()
        close_db_connection(db)

    def test_recipes_by_user(self):
        ##Create test data

        user_id = "test user"
        user_email = user_id + "@gmail.com"
        result = create_user(user_id, user_id, user_id, user_id, user_email)
        print("User created == {}".format(result))

        test_recipe_names_list= []
        incrament = 1

        while incrament < 17:
            test_recipe_names_list.append(str(incrament))
            add_recipe(str(incrament), str(incrament), incrament, str(incrament), 0, 0, user_id)
            incrament += 1
            
        self.assertEqual(get_recipes_by_user(user_id),test_recipe_names_list, "This test to confirm user recipes submitted by are retreived")
        
        db, cursor = establish_db_connection()
        ##Clear any reference to the recipe "Recipe should not exist" from the table
        cursor.execute("Delete from recipesTable where User_ID=(?);", (user_id,))
        cursor.execute("Delete from loginTable where User_ID=(?);", (user_id,))
        db.commit()
        close_db_connection(db)





if __name__ == '__main__':
        unittest.main()