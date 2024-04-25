############################################################################
## Unit tests for recipesTable functionality
## This file contains unit tests for the functions in community_posts_db.py
############################################################################

import os
import unittest
import sqlite3
import random
from recipeAPI import add_recipe, create_recipesTable
from create_db import fill_recipes


class Test_recipesTable (unittest.TestCase):
    def setUp(self):

        # Set up a temporary SQLite database for testing if doesn't already exist
        self.db_filename = 'recipesTableDB.db'
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()
        
        database_path = os.path.join(os.getcwd(), 'recipesTableDB.db')
        if os.path.exists(database_path):
            os.remove(database_path)
            print("The database {} was removed from the current directory ({}) for accurate testing".format(self.db_filename, os.getcwd()))
            
        create_recipesTable(self.db_filename)
        fill_recipes(self.db_filename, "./csv/recipes.csv")


    def test_add_recipe(self):
        ##self.mymessage = "Filled"
        number_of_unique_recipes = 1 
        db = self.db_filename

        recipe_name = "Warm Comfort"
        ingredients = "2 chamomile tea bags.1 oz reposado tequila.1/2 oz fresh lemon juice.1 Tbsp agave nectar"
        cook_time = 5
        directions = "Place 2 chamomile tea bags in a heatsafe vessel such as a large liquid measuring cup. Pour in 1 1/2 cups boiling water and let steep 5 minutes  then remove tea bags. Add 1 oz reposado tequila 1/2 oz fresh lemon juice and 1 Tbsp agave nectar and stir until incorporated. Pour into a 16-ounce insulated mug (or two smaller 8-ounce mugs) and drink hot."
        user_id = "garci446"

        self.assertNotEqual(add_recipe(recipe_name, ingredients, cook_time, directions, 0, 0, user_id), (True, 'Recipe successfully added!'), "Test to avoid adding duplicate recipe names has not passed");

        recipe_name = "Completely new recipe"
        
        self.assertEqual(add_recipe(recipe_name, ingredients, cook_time, directions, 0, 0, user_id), (True, 'Recipe successfully added!'), "Test to add unique named recipe names has not passed");


if __name__ == '__main__':
    unittest.main()