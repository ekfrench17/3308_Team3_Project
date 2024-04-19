############################################################################
## Unit tests for CommunityPosts functionality
## This file contains unit tests for the functions in community_posts_db.py
############################################################################


import unittest
import sqlite3
from community_posts_db import create_community_post, fill_community_post, edit_post, display_posts_by_time

class TestCommunityPosts(unittest.TestCase):
    def setUp(self):
        # Set up a temporary SQLite database for testing
        self.db_filename = 'test_database.db'
        self.conn = sqlite3.connect(self.db_filename)
        self.c = self.conn.cursor()
        
        # Create the CommunityPosts table
        create_community_post(self.db_filename)
        
    def tearDown(self):
        # Drop the CommunityPosts table and close the database connection
        self.c.execute("DROP TABLE IF EXISTS CommunityPosts")
        self.conn.commit()
        self.conn.close()
        
    def test_fill_community_post(self):
        # Test filling a community post
        post_id_counter = 1
        user_post_input = "Test post"
        desired_recipe_id = 1
        user_id_num = "test_user"
        rating_input = 5
        date_nums = 20220301
        
        fill_community_post(self.db_filename, post_id_counter, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums)
        
        # Check if the post exists in the database
        self.c.execute("SELECT * FROM CommunityPosts WHERE Post_ID=?", (post_id_counter,))
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
        fill_community_post(self.db_filename, post_id_input, "Original post", desired_recipe_id, user_id_num, 5, 20220301)
        
        # Edit the post
        edit_post(self.db_filename, post_id_input, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums)
        
        # Check if the post was edited
        self.c.execute("SELECT * FROM CommunityPosts WHERE Post_ID=?", (post_id_input,))
        result = self.c.fetchone()
        self.assertEqual(result[1], user_post_input)
        
    def test_display_posts_by_time(self):
        # Test displaying posts by time
        # Insert some test posts with different dates
        fill_community_post(self.db_filename, 1, "Post 1", 1, "user1", 5, 20220301)
        fill_community_post(self.db_filename, 2, "Post 2", 1, "user2", 6, 20220302)
        fill_community_post(self.db_filename, 3, "Post 3", 1, "user3", 7, 20220303)
        
        # Display posts by time and check the order
        expected_order = [(3, "Post 3"), (2, "Post 2"), (1, "Post 1")]
        self.assertListEqual(display_posts_by_time(self.db_filename), expected_order)

# if __name__ == '__main__':
#     unittest.main()