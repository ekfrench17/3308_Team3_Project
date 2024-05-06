############################################################################
## Unit tests for CommunityPosts functionality
## This file contains unit tests for the functions in community_posts_db.py
############################################################################

import os
import unittest
import sqlite3
from community_posts_db import create_post, fill_community_post, edit_post, display_posts_by_time
from datetime import date

class TestCommunityPosts(unittest.TestCase):
    def setUp(self):
        # Set up a temporary SQLite database for testing
        
        self.db_filename = 'test_community.db'
        
        try:
            os.remove(self.db_filename)
        except:
            pass
        
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()

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
            self.c.execute("CREATE TABLE " + t)
        
        self.conn.commit()
        
        recipe_data = [2,'test recipe','ingredients',15,'directions',3.0,4,"test_user",date.today()]
        
        self.c.execute("INSERT INTO recipesTable Values(?,?,?,?,?,?,?,?,?)",recipe_data)
        #cursor.execute("SELECT * FROM recipesTable;")
        #print(cursor.fetchall())
        self.conn.commit()
        
        # Create the CommunityPosts table
        #create_community_post(self.db_filename)
        #database_path = os.path.join(os.getcwd(),self.db_filename)
        #if not os.path.exists(database_path):
            #create_db_file_path = "./create_db.py"
            #subprocess.run(["python3", create_db_file_path])
        #self.conn = sqlite3.connect(self.db_filename)
        #self.c = self.conn.cursor()
        
    def tearDown(self):
        # Drop the CommunityPosts table and close the database connection
        #self.c.execute("DROP TABLE IF EXISTS communityTable")
        
        os.remove(self.db_filename)
        
    def test_fill_community_post(self):
        # Test filling a community post
        post_id_counter = 1
        user_post_input = "Test post"
        desired_recipe_id = 1
        user_id_num = "test_user"
        rating_input = 5
        date_nums = 20220301
        
        fill_community_post(self.db_filename, post_id_counter, user_post_input, desired_recipe_id, user_id_num, rating_input)
        
        # Check if the post exists in the database
        self.c.execute("SELECT * FROM communityTable WHERE Post_ID=?", (post_id_counter,))
        result = self.c.fetchone()
        self.assertIsNotNone(result)
   
    def test_edit_post(self):
        # Test editing a community post
        post_id_input = 1
        user_post_input = "Edited post"
        desired_recipe_id = 1
        user_id_num = "test_user"
        rating_input = 8
        date_nums = 20220302
        
        # Insert a post to edit
        fill_community_post(self.db_filename, post_id_input, "Original post", desired_recipe_id, user_id_num, 5)
        
        # Edit the post
        edit_post(self.db_filename, post_id_input, user_post_input)
        
        # Check if the post was edited
        self.c.execute("SELECT * FROM communityTable WHERE Post_ID=?", (post_id_input,))
        result = self.c.fetchone()
        self.assertEqual(result[1], user_post_input)
       
    def test_display_posts_by_time(self):
        # Test displaying posts by time
        # Insert some test posts with different dates
        fill_community_post(self.db_filename, 1, "Post 1", 2, "user1", 5)
        fill_community_post(self.db_filename, 2, "Post 2", 2, "user2", 6)
        fill_community_post(self.db_filename, 3, "Post 3", 2, "user3", 7)
        
        today = str(date.today())
        #print("today is: ",today)
        
        # Display posts by time and check the order
        expected_order = [(1, "Post 1", '2', "user1", 5, today),(2, "Post 2", '2', "user2", 6, today), (3, "Post 3", '2', "user3", 7, today)]
        # error with this call - display_posts_by_time requires 6 arguments: (db_filename, post_id_counter, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums)
        row_list = display_posts_by_time(self.db_filename)
        #print('test data: ',expected_order)
        #print('output data: ',row_list)
        self.assertListEqual(row_list, expected_order)

if __name__ == '__main__':
     unittest.main()