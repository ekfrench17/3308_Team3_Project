###############################################################################
## This is the community page for RecipEASY
##
## Instructions:
## this is the SQLite to hold and edit community posts
## there are functions to create, fill, edit, and display posts in the community page
###############################################################################


###############################################################################


# import necessary libraries
import sqlite3
from sqlite3 import Error
from datetime import date
# set the date
today = date.today()

# # Set up the table
# def create_community_post(db_filename): 
#     conn = None
#     try:
#         conn = sqlite3.connect(db_filename)
#         print(f"Connected to SQLite database {db_filename}")

#         # Create tables
#         c = conn.cursor()
#         c.execute("""
#             CREATE TABLE IF NOT EXISTS CommunityPosts (
#                 Post_ID INT PRIMARY KEY,
#                 Post VARCHAR,
#                 Recipe VARCHAR,
#                 User_ID VARCHAR,
#                 Rating INT,
#                 Post_Date INT
#             )
#         """)

#         conn.commit()
#         #print("Tables have been successfully created.")

#     except Error as e:
#         print(f"Error create function: {e}")
#     finally:
#         if conn:
#             conn.close()
#             #print("Connection closed.")
#             #print()
            
            
###############################################################
###############################################################
# Create a routine to fill the table with data
# This is based on assuming that there is a table called RecipeTable and within it is a field called Recipe that can be accessed with RecipeID

# test data to set up initial table ######
# post_id_counter = 0
# user_post_input = "What a great pizza!"
# desired_recipe_id = 0
# user_id_num = 111
# rating = 9
# date_nums = today.strftime('%m/%d/%Y')
##########################################

def fill_community_post(db_filename, post_id_counter, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()

        # Insert data
        c.execute("INSERT INTO CommunityPosts (Post_ID, Post, Recipe, User_ID, Rating, Post_Date) VALUES (?, ?, (SELECT Name FROM recipesTable WHERE Recipe ID=?), ?, ?, ?)", 
                  
                  # these are vaiables to be added later
                  # post_id_counter = number of post like a counter (INT)
                  # user_post_input = input string from user (VARCHAR)
                  # desired_recipe_id = RecipeID number from Recipe table (INT)
                  # user_id_num = unique user id number (INT)
                  # rating = user input number 0 - 10 (INT)
                  # date_nums = date of post in number form 04102024 (INT)
                  
                  (post_id_counter, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums))

        
        # Commit the changes to the database
        conn.commit()
        #print("Table successfully filled.")

    except Error as e:
        print(f"Error inserting data: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.close()
            #print("Connection closed.")
            #print()

#################################################################
#################################################################

# This will take in input to create a post and save it in the table

# test data to add a post ################
# post_id_counter = post_id_counter + 1
# user_post_input = input("Type something here!")
# desired_recipe_id = input("Enter the recipe id.")
# user_id_num = input("Enter your user id number.")
# rating = input("Enter a rating (0-10).")
# date_nums = today.strftime('%m/%d/%Y')
###########################################

def create_post(db_filename, post_id_counter, user_post_input, desired_recipe_id, user_id_num, rating_input):
    message = ''
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()

#         # Insert data
        c.execute("INSERT INTO communityTable (Post_ID, Post, Recipe_id, User_ID, Post_Date) VALUES (?, ?, ?, ?, ?, ?)", 
                  
#                   # these are vaiables to be added later
#                   # post_id_counter = number of post like a counter (INT)
#                   # user_post_input = input string from user (VARCHAR)
#                   # desired_recipe_id = RecipeID number from Recipe table (INT)
#                   # user_id_num = unique user id number (INT)
#                   # rating = user input number 0 - 10 (INT)
#                   # date_nums = date of post in number form 04102024 (INT)
                  
                   (post_id_counter, user_post_input, desired_recipe_id, user_id_num, today))

        
        # Commit the changes to the database
        conn.commit()
        #print("Table successfully filled.")

    except Error as e:
        message = f"Error inserting data: {e}"
    finally:
        # Close the database connection
        if conn:
            conn.close()
            #print("Connection closed.")
            message = "success"
    return message


###################################################################
###################################################################

# This will Edit a post that is already in the table

# test data to add a post ################
# post_id_counter = input("Enter post ID to edit post.")
# user_post_input = input(print(SELECT Post FROM CommunityPosts WHERE PostID=post_id_input), "...Edit post...")
# desired_recipe_id = input("Enter the recipe id.")
# user_id_num = input("Enter your user id number.")
# rating = input("Enter a rating (0-10).")
# date_nums = today.strftime('%m/%d/%Y')
###########################################

def edit_post(db_filename, post_id_input, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()

#         # Insert data
        c.execute("INSERT INTO CommunityPosts (Post_ID, Post, Recipe, User_ID, Rating, Post_Date) VALUES (?, ?, (SELECT Recipe FROM RecipeTitle WHERE RecipeID=?), ?, ?, ?)", 
                  
#                   # these are vaiables to be added later
#                   # post_id_counter = number of post like a counter (INT)
#                   # user_post_input = input string from user (VARCHAR)
#                   # desired_recipe_id = RecipeID number from Recipe table (INT)
#                   # user_id_num = unique user id number (INT)
#                   # rating = user input number 0 - 10 (INT)
#                   # date_nums = date of post in number form 04102024 (INT)
                  
                   (post_id_input, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums))

        
        # Commit the changes to the database
        conn.commit()
        #print("Table successfully filled.")

    except Error as e:
        print(f"Error inserting data: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.close()
            #print("Connection closed.")
            print()
            

############################################################################
############################################################################

# This will display all posts in order of newest to oldest

def display_posts_by_time(db_filename, post_id_counter, user_post_input, desired_recipe_id, user_id_num, rating_input, date_nums):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_filename)
        c = conn.cursor()
                  
        # Execute a SELECT query to retrieve posts ordered by date_nums
        c.execute("SELECT * FROM CommunityPosts ORDER BY Post_Date DESC")  # DESC for descending order, ASC for ascending order

        # Fetch all the rows from the result set
        rows = c.fetchall()

        # Display the posts
        for row in rows:
            print(row)

    except Error as e:
        print(f"Error inserting data: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.close()
            #print("Connection closed.")
            print()