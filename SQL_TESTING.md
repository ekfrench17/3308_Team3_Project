<div style="text-align: center;">
  <h1>SQL DESIGN</h1>
</div>
<h1> Recipes Table </h1>
<hr>
<b>Table Description:</b> This table will contain all the needed information for ranking a recipe, storing recipe's ingredients, as well as accociating a recipe sumbitted to the creator of it.

<b>Table Values (Columns):</b>
<ul>
  <li>Recipe ID (int)
    <ul>
      <li>This will be the Recipe Identifier</li>
    </ul>
  </li>
  <li>Name (varchar)
    <ul>
      <li>This will be name of the Recipe</li>
    </ul>
  </li>
  <li>Recipe (varchar)
    <ul>
      <li>This will be the Recipe</li>
    </ul>
  </li>
  <li>Avg Ratings Decimal(3,2) **Can be null at a records/recipe's creation**
    <ul>
      <li>This will be rating of the recipe that will be in a 3 digit format with digits being decimals to the 100th's value.</li>
    </ul>
  </li>
  <li>User ID (varchar)
    <ul>
      <li>This will be identifier of the user who submitted the recipe</li>
    </ul>
  </li>
</ul>
<b>List of Tests for Recipes Table</b>
<ul>
    <li>Verify that the Recipe ID is a primary key and auto-increments with each new recipe entry.</li>
    <li>Confirm that each Name entered into the table is unique.</li>
    <li>Ensure that the Avg Ratings field can be set to null upon record creation and restricts the rating to a decimal(3,2) format.</li>
    <li>Verify that the User ID correctly references the identifier of the user who submitted the recipe.</li>
    <li>Attempt to insert a record with missing required fields to ensure that the table enforces data integrity.</li>
    <li>Test the calculation and updating of the Avg Ratings field when new ratings are added.</li>
    <li>Retrieve a recipe by Recipe ID to confirm that all associated information is returned correctly.</li>
    <li>Attempt to delete a recipe to check for cascading effects or restrictions and try updating a recipe's User ID to test for immutability.</li>
    <li>Perform searches on the Name field to ensure that recipes can be found based on their title.</li>
    <li>Update the Avg Ratings for a recipe and confirm that the new average is accurately reflected.</li>
</ul>

</hr>

<h2>Access Methods for Recipe Table</h2>
<hr>
<ul>
<li>Add a Recipie</li>
    <ul><li>By passing the recipe, its name, user id as parameters you will be add a record/recipe to the table. The AVG Rating will be initalized to null no values will be returned.</li></ul>
    <ul><li>Tests:</li></ul> 
<li>Search Recipies</li>
    <ul><li>By passing the recipe name as a parameter you will be able to have the recipe requested returned to the page. The AVG Rating will be initalized to null no values will be returned.</li></ul>
    <ul><li>Tests:</li></ul> 
<li>Pull Recently Added Recipe</li>
<li>Suggested Recipes. (I don't know if possible given time frame). If needed we can pull maybe just top rated Recipes</li>
<li>Pull and Display all Recipes uploaded by a user</li>
<li>Pull and Display all Recipes by Name given user Input</li>
<li>Pull and Display all Recipes by Ingredient given user Input</li>
<li>Pull and Display all Recipes by Author (User who uploaded) given user Input</li>
<li>Pull and Display all Random Recipes by Name given user Input (likely just pressing a button)</li>
</ul>

</hr>

<h1> Login Credentials Table </h1>

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

<b>List of Tests for User_Table</b>
<ul>
    <li>Verify that each User name is unique.</li>
    <li>Confirm that User_ID is auto-incremented and unique for each user.</li>
    <li>Check that passwords are encrypted before storage.</li>
</ul>
 
</hr>

<h2>Access Methods for Login Credentials Table</h2>
<hr>
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



<h1>Community Posts Table</h1>

<b>Table Description:</b> This table will contain all the community posts posted on the community page as well as other data associated with those posts.

<b>Table Values (Columns):</b>
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
<b>List of Tests for Community_Table</b>
<ul>
    <li>Confirm that Post_ID is auto-incremented and unique.</li>
    <li>Check that User_ID refers to a valid user in User_Table.</li>
    <li>Ensure Recipe_ID corresponds to an existing recipe entry.</li>
    <li>Check that Post Date is automatically set to the current date and time in UTC upon creation.</li>
</ul>
</hr>


<h2>Access Methods for Community_Table</h2>
<hr>
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
