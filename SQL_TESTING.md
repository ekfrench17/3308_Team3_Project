#  SQL DESIGN

---

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

<hr>

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
     
<hr>

## Access Methods for Recipe Table

<hr>

Pages that will access this table:
- Home page
- Explore page
- My Recipes page
- Add New Recipe page (get and post)

<ul>
<li>Add a Recipe</li>
    <ul>
        <li>By passing the recipe name, ingredients, quantity, cooking time, directions, and user ID as parameters, you can add a new recipe record to the table. The AVG Rating will be initialized to null, and the submit date will be automatically set to the current date. No values will be returned.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Attempt to add a recipe with a unique name and all necessary details to see if the recipe record is created.</li>
            <li>Attempt to add a recipe with a name that already exists to ensure the system prevents duplicate identical recipe names.</li>
        </ul>
    </ul>
<li>Give Rating on Recipe</li>
    <ul>
        <li>By passing a recipe ID and a rating that follows the 3 digit 2 decimal format, a new rating will be calculated using the weighted average of the new rating submitted and the current average rating, factoring in the updated total ratings submission. No values will be returned.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Test the weighted average calculation and updating of the Avg Ratings field when a new rating is added.</li>
            <li>Verify that the Total Ratings submission auto-increments with each new recipe rating submission.</li>
        </ul>
    </ul>
<li>Search Recipes</li>
    <ul>
        <li>By passing the recipe name as a parameter, you will be able to retrieve the recipe details including ingredients, cooking time, and directions, alongside the recipe, author, and rating.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Verify the correct recipe is pulled when given a name.</li>
            <li>Verify nothing is returned when a recipe name that doesn't exist is being searched.</li>
        </ul>
    </ul>
<li>Pull Recently Added Recipe</li>
    <ul>
        <li>By passing the user ID, you will be able to retrieve up to 5 of the most recently submitted recipes by that user.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Verify the order of the 5 recipes returned is correctly listed from the most recent to the 5th most recent submission date.</li>
            <li>Verify only 5 recipes are returned when more than 5 recipes exist in the table.</li>
            <li>Verify all recipes are returned when fewer than 5 recipes exist in the table.</li>
        </ul>
    </ul>
<li>Suggested Recipes</li>
    <ul>
        <li>By calling this method, you will be able to return up to 5 of the top-rated recipes.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Verify the top 5 rated recipes are returned in order from the highest to the 5th highest average rating for the entire recipe table.</li>
            <li>Verify only 5 recipes are returned when more than 5 recipes exist in the table.</li>
            <li>Verify all recipes are returned when fewer than 5 recipes exist in the table.</li>
        </ul>
    </ul>
<li>Pull and Display all Recipes uploaded by a user</li>
    <ul>
        <li>By passing the User ID as a parameter, this method will return all recipes uploaded by a user, including their ingredients, quantities, cooking times, and directions.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Verify nothing is returned when a User ID that doesn't exist is being searched.</li>
            <li>Verify every recipe associated with a User ID is being returned, complete with all new fields.</li>
        </ul>
    </ul>
</ul>
<hr>


## List of Tests for Recipes Table

<hr>
<ul>
  <li>Verify that the Recipe ID is a primary key and auto-increments with each new recipe entry.</li>
  <li>Confirm that each Name entered into the table is unique.</li>
  <li>Ensure that the Ingredients field can store a list of ingredients in the expected varchar format.</li>
  <li>Verify that the Quantity field can store quantities for each ingredient in the expected varchar format.</li>
  <li>Check that the Cooking Time field accepts only integer values and represents the time in minutes.</li>
  <li>Ensure that the Directions field can store a text value large enough for step-by-step instructions.</li>
  <li>Ensure that the Avg Ratings field can be set to null upon record creation and restricts the rating to a decimal(3,2) format.</li>
  <li>Verify that the Total Rating Submissions field auto-increments with each new rating entry.</li>
  <li>Verify that the User ID correctly references the identifier of the user who submitted the recipe.</li>
  <li>Confirm that the Submit Date field is automatically set to the current date and time upon recipe creation.</li>
  <li>Attempt to insert a record with missing required fields to ensure that the table enforces data integrity.</li>
  <li>Retrieve a recipe by Recipe ID to confirm that all associated information is returned correctly.</li>
  <li>Attempt to delete a recipe to check for cascading effects or restrictions and try updating a recipe's User ID to test for immutability.</li>
  <li>Perform searches on the Name field to ensure that recipes can be found based on their title.</li>
</ul>
<hr>


# **Login Credentials Table**

<b>Table Description:</b> This table stores essential information about the users registered in the application, including their credentials.

<b>Table Values (Columns):</b>
<ul>
  <li>User_ID (Int)
    <ul>
      <li>This will be identifier of the user who submitted the recipe</li>
    </ul>
  </li>
  <li>Password (varchar)
    <ul>
      <li>This will be the password associated with the User ID</li>
    </ul>
  </li>
  <li>First Name (varchar)
    <ul>
      <li>This will be the first name of the user</li>
    </ul>
  </li>
  <li>Last Name (char)
    <ul>
      <li>This will be the last name of the user</li>
    </ul>
  </li>
  <li>Email (varchar)
    <ul>
      <li>This will be the email address of the user</li>
    </ul>
  </li>
</ul>

</hr>

## List of Tests for User_Table

<ul>
    <li>Verify that each User name is unique.</li>
    <li>Confirm that User_ID is auto-incremented and unique for each user.</li>
    <li>Check that passwords are encrypted before storage.</li>
</ul>
 
</hr>

## Access Methods for Login Credentials Table

<hr>

Pages that will access this table:
- Home page: login page pop up as part of home page from User perspective

<ul>
    <li>Add User</li>
    <ul>
        <li>By passing the user's name and password as parameters, you can add a new user record to the table. No values will be returned.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Attempt to add a user with unique credentials and verify that the record is created.</li>
            <li>Attempt to add a user with an existing username to ensure the system prevents duplicate usernames.</li>
        </ul>
    </ul>
    <li>Validate User Login</li>
    <ul>
        <li>By passing a username and password, you can validate a user's credentials. Returns <code>true</code> if credentials match, otherwise <code>false</code>.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Verify that correct username and password return <code>true</code>.</li>
            <li>Verify that incorrect credentials return <code>false</code>.</li>
        </ul>
    </ul>
</ul>



# **Community Posts Table**

**Table Description:** This table will contain all the community posts posted on the community page as well as other data associated with those posts.

**Table Values (Columns):**
<ul>
  <li>Post_ID (int)
    <ul>
      <li>This will be the identifier for the post</li>
    </ul>
  </li>
  <li>Post (varchar)
    <ul>
      <li>This will be the post itself</li>
    </ul>
  </li>
  <li>Recipe (varchar)
    <ul>
      <li>This will be the Recipe in which post is related to</li>
    </ul>
  <li>User_ID (varchar)
    <ul>
      <li>This will be identifier of the user who submitted the post</li>
    </ul>
  </li>
  <li>Post Date (int)
    <ul>
      <li>This will be the date of the post</li>
    </ul>
  </li>
</ul>
</hr>

## List of Tests for Community_Table

<hr>
<ul>
    <li>Confirm that Post_ID is auto-incremented and unique.</li>
    <li>Check that User_ID refers to a valid user in User_Table.</li>
    <li>Ensure Recipe_ID corresponds to an existing recipe entry.</li>
    <li>Check that Post Date is automatically set to the current date and time in UTC upon creation.</li>
</ul>
</hr>

## Access Methods for Community_Table

<hr>

Pages that will access this table:
- Community page

<ul>
    <li>Create Post</li>
    <ul>
        <li>By providing the user ID, recipe ID, post title, user rating, and user comments, a new post will be created in the table. The post date is set to the current UTC time. No values will be returned.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Ensure that a post with all required fields can be created and receives a proper timestamp.</li>
            <li>Confirm rejection of post creation when mandatory fields are missing or invalid.</li>
        </ul>
    </ul>
    <li>Edit Post</li>
    <ul>
        <li>By passing the post ID along with any new values for post title, user rating, and user comments, an existing post can be updated. The method verifies the post belongs to the user before editing.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Check that valid edits update the post correctly.</li>
            <li>Confirm that editing a non-existent post ID fails gracefully.</li>
        </ul>
    </ul>
    <li>Delete Post</li>
    <ul>
        <li>By providing the post ID and user ID, a post can be deleted from the table. The method verifies the post belongs to the user before deletion.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Ensure a post can be deleted when valid IDs are provided.</li>
            <li>Attempt to delete a post with incorrect user ID to ensure it cannot be deleted by another user.</li>
        </ul>
    </ul>
    <li>Display Posts by Time</li>
    <ul>
        <li>Posts can be retrieved and sorted by their post date. Returns a list of posts in descending order from the most recent to the oldest.</li>
    </ul>
    <ul>
        <li>Tests:</li>
        <ul>
            <li>Verify that the posts are returned in the correct order based on the post date.</li>
            <li>Confirm that the posts retrieved are within the specified timeframe if one is set.</li>
        </ul>
    </ul>
</ul>
<hr>

