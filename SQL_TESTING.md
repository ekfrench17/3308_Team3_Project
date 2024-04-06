#  SQL DESIGN


##  Overview
**Tables:**
- Recipes Table
    * Access methods
    * Tests
- Community Posts Table
    * Access methods
    * Tests
- Login Credentials Table
    * Access methods
    * Tests

---

#  **Recipes Table**

**Table Description:** This table will contain all the needed information for ranking a recipe, storing recipe's ingredients, as well as associating a recipe submitted to the creator of it.

**Table Values (Columns):**
- Recipe ID (int)
    * The unique Recipe Identifier.
    * Reference field for the other two tables
- Name (varchar)
    * The name of the Recipe.
- Ingredients (varchar)
    * A list of ingredients required for the recipe.
- Quantity (varchar)
    * The quantities of each ingredient needed for the recipe.
- Cooking Time (int)
    * The time required to cook the recipe, measured in minutes.
- Directions (text)
    * Step-by-step instructions on how to prepare and cook the recipe.
- Avg Ratings (Decimal(3,2)) **Can be null at a record/recipe's creation**
    * The average rating of the recipe, in a 3-digit format with 2 decimals to the hundredth's value.
- Total Rating Submissions (int)
    * The tally of the number of ratings submitted for a specific recipe.
- User ID (varchar)
    * The identifier of the user who submitted the recipe.
    * Reference from the Login Credentials table
- Submit Date (datetime)
     * The date and time when the recipe was submitted.
     

## Access Methods for Recipe Table

**Pages that will access this table:**
- Home page
- Explore page
- My Recipes page
- Add New Recipe page (get and post)

**Methods**
- Add a Recipe
    * By passing the recipe name, ingredients, quantity, cooking time, directions, and user ID as parameters, you can add a new recipe record to the table. The AVG Rating will be initialized to null, and the submit date will be automatically set to the current date. No values will be returned.
    * Tests:
        + Attempt to add a recipe with a unique name and all necessary details to see if the recipe record is created.
        + Attempt to add a recipe with a name that already exists to ensure the system prevents duplicate identical recipe names.
- Give Rating on Recipe
    * By passing a recipe ID and a rating that follows the 3 digit 2 decimal format, a new rating will be calculated using the weighted average of the new rating submitted and the current average rating, factoring in the updated total ratings submission. No values will be returned.
    * Tests:
        + Test the weighted average calculation and updating of the Avg Ratings field when a new rating is added.
        + Verify that the Total Ratings submission auto-increments with each new recipe rating submission.
- Search Recipes
    * By passing the recipe name as a parameter, you will be able to retrieve the recipe details including ingredients, cooking time, and directions, alongside the recipe, author, and rating.
    * Tests:
        + Verify the correct recipe is pulled when given a name.
        + Verify nothing is returned when a recipe name that doesn't exist is being searched.
- Pull Recently Added Recipe
    * By passing the user ID, you will be able to retrieve up to 5 of the most recently submitted recipes by that user.
    * Tests:
        + Verify the order of the 5 recipes returned is correctly listed from the most recent to the 5th most recent submission date.
        + Verify only 5 recipes are returned when more than 5 recipes exist in the table.
        + Verify all recipes are returned when fewer than 5 recipes exist in the table.
- Suggested Recipes
    * By calling this method, you will be able to return up to 5 of the top-rated recipes.
    * Tests:
        + Verify the top 5 rated recipes are returned in order from the highest to the 5th highest average rating for the entire recipe table.
        + Verify only 5 recipes are returned when more than 5 recipes exist in the table.
        + Verify all recipes are returned when fewer than 5 recipes exist in the table.
- Pull and Display all Recipes uploaded by a user
    * By passing the User ID as a parameter, this method will return all recipes uploaded by a user, including their ingredients, quantities, cooking times, and directions.
    * Tests:
        + Verify nothing is returned when a User ID that doesn't exist is being searched.
        + Verify every recipe associated with a User ID is being returned, complete with all new fields.


## List of Tests for Recipes Table

**Field Type Verification**
- Verify that the Recipe ID is a primary key and auto-increments with each new recipe entry.
- Confirm that each Name entered into the table is unique.
- Ensure that the Ingredients field can store a list of ingredients in the expected varchar format.
- Verify that the Quantity field can store quantities for each ingredient in the expected varchar format.
- Check that the Cooking Time field accepts only integer values and represents the time in minutes.
- Ensure that the Directions field can store a text value large enough for step-by-step instructions.
- Ensure that the Avg Ratings field can be set to null upon record creation and restricts the rating to a decimal(3,2) format.
- Verify that the Total Rating Submissions field auto-increments with each new rating entry.
- Verify that the User ID correctly references the identifier of the user who submitted the recipe.
- Confirm that the Submit Date field is automatically set to the current date and time upon recipe creation.

**Data Access Verification**
- Attempt to insert a record with missing required fields to ensure that the table enforces data integrity.
- Retrieve a recipe by Recipe ID to confirm that all associated information is returned correctly.
- Attempt to delete a recipe to check for cascading effects or restrictions and try updating a recipe's User ID to test for immutability.
- Perform searches on the Name field to ensure that recipes can be found based on their title.

---


# **Login Credentials Table**

**Table Description:** This table stores essential information about the users registered in the application, including their credentials.

**Table Values (Columns):**
- User_ID (Int)
    * This will be identifier of the user who submitted the recipe
    * Referenced by the Recipes Table and Community Table
- Password (varchar)
    * This will be the password associated with the User ID
- First Name (varchar)
    * This will be the first name of the user
- Last Name (char)
    * This will be the last name of the user
- Email (varchar)
    * This will be the email address of the user


## Access Methods for Login Credentials Table

**Pages that will access this table:**
- Home page: login page pop up as part of home page from User perspective

**Methods**
- Add User
    * By passing the user's name and password as parameters, you can add a new user record to the table. No values will be returned.
    * Tests:
        + Attempt to add a user with unique credentials and verify that the record is created.
        + Attempt to add a user with an existing username to ensure the system prevents duplicate usernames.
- Validate User Login
    * By passing a username and password, you can validate a user's credentials. Returns `true` if credentials match, otherwise `false`.
    * Tests:
        + Verify that correct username and password return `true`.
        + Verify that incorrect credentials return `false`.

## List of Tests for Login Credentials Table

- Verify that each User name is unique.
- Confirm that User_ID is auto-incremented and unique for each user.
- Check that passwords are encrypted before storage.

---

# **Community Posts Table**

**Table Description:** This table will contain all the community posts posted on the community page as well as other data associated with those posts.

**Table Values (Columns):**
- Post_ID (int)
    * This will be the identifier for the post
- Post (varchar)
    * This will be the post itself
- Recipe (varchar)
    * This will be the Recipe in which post is related to
- User_ID (varchar)
    * This will be identifier of the user who submitted the post
- Post Date (int)
    * This will be the date of the post

## Access Methods for Community_Table


**Pages that will access this table:**
- Community page

**Methods**
- Create Post
    * By providing the user ID, recipe ID, post title, user rating, and user comments, a new post will be created in the table. The post date is set to the current UTC time. No values will be returned.
    * Tests:
        + Ensure that a post with all required fields can be created and receives a proper timestamp.
        + Confirm rejection of post creation when mandatory fields are missing or invalid.
- Edit Post
    * By passing the post ID along with any new values for post title, user rating, and user comments, an existing post can be updated. The method verifies the post belongs to the user before editing.
    * Tests:
        + Check that valid edits update the post correctly.
        + Confirm that editing a non-existent post ID fails gracefully.
- Delete Post
    * By providing the post ID and user ID, a post can be deleted from the table. The method verifies the post belongs to the user before deletion.
    * Tests:
        + Ensure a post can be deleted when valid IDs are provided.
        + Attempt to delete a post with incorrect user ID to ensure it cannot be deleted by another user.
- Display Posts by Time
    * Posts can be retrieved and sorted by their post date. Returns a list of posts in descending order from the most recent to the oldest.
    * Tests:
        + Verify that the posts are returned in the correct order based on the post date.
        + Confirm that the posts retrieved are within the specified timeframe if one is set.

## List of Tests for Community_Table

- Confirm that Post_ID is auto-incremented and unique.
- Check that User_ID refers to a valid user in User_Table.
- Ensure Recipe_ID corresponds to an existing recipe entry.
- Check that Post Date is automatically set to the current date and time in UTC upon creation.
