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
  <li>Total Rating Submissions (int)
    <ul>
      <li>This will tally the number of ratings submitted for a specific recipe</li>
    </ul>
  </li>
  <li>User ID (varchar)
    <ul>
      <li>This will be identifier of the user who submitted the recipe</li>
    </ul>
  </li>
  <li>Submit Date (int)
    <ul>
      <li>This will be the date of the post</li>
    </ul>
  </li>
</ul>

</hr>

<h2>Access Methods for Recipe Table</h2>
<hr>
<ul>
<li>Add a Recipie</li>
    <ul><li>By passing the recipe, its name, user id as parameters you will be add a record/recipe to the table. The AVG Rating will be initalized to null no values will be returned.</li></ul>
    <ul><li>Tests:</li></ul> 
<li>Give Rating on Recipe</li>
    <ul><li>By passing a parameter that follows the 3 digit 2 decimal format, a new rating will be returned. The new rating will be calulated by using the weighted average of the new rating submitted and the current rating weighted off the Total Ratings Submission .</li></ul>
    <ul><li>Tests:</li></ul> 
<li>Search Recipies</li>
    <ul><li>By passing the recipe name as a parameter you will be able to have the recipe, author, and rating returned to the page.</li></ul>
    <ul><li>Tests:</li></ul> 
<li>Pull Recently Added Recipe</li>
<ul><li>By passing the user ID you will be able to up to 5 of the most recent recipes.</li></ul>
<ul><li>Tests:</li></ul> 
<li>Suggested Recipes</li>
<ul><li>By calling this method you will be able to return up to 5 of the top rated recipes .</li></ul>
<ul><li>Tests:</li></ul> 
<li>Pull and Display all Recipes uploaded by a user</li>
<ul><li>By passing the User ID as a parameter this method will return all Recipes uploaded by a user</li></ul>
<ul><li>Tests:</li></ul> 
</ul>

</hr>

<h1> Login Credentials Table </h1>

<b>Table Description:</b> This table will contain all the needed information for login credentials

<b>Table Values (Columns):</b>
<ul>
  <li>User ID (varchar)
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
<h2>Access Methods for Login Credentials Table</h2>
<hr>
<ul>
  <li>Add User Record
    <ul>
      <li>By passing a user id, password, first name, last name, and email, a record of login credentials will be created </li>
      <li>Tests:</li>
    </ul>
  </li>
  <li>Verify User exists
    <ul>
      <li>By passing a user id and password as parameters a search will be conducted for the user id and password access to the site will be granted.</li>
      <li>Tests:</li>
    </ul>
  </li>
</ul>
</hr>


<h1>Community Posts Table</h1>

<b>Table Description:</b> This table will contain all the community posts posted on the community page as well as other data associated with those posts.

<b>Table Values (Columns):</b>
<ul>
  <li>Post ID (int)
    <ul>
      <li>This will be the identifier for the post</li>
    </ul>
  </li>
  <li>Post (varchar)
    <ul>
      <li>This will be the post itself</li>
    </ul>
  </li>
  <li>User ID (varchar)
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
<h2>Access Methods for Community Posts Table</h2>
<hr>
<ul>
  <li>Add Posts
    <ul>
      <li>By using the post (string) as a parameter to this method, we will be able to store this post, record the date and time, and record the user of the post to the DB. Nothing will be returned from this method.</li>
      <li>Test:</li>
    </ul>
  </li>
  <li>Pull all posts (maybe have a cap for total that should be posted?)
    <ul>
      <li>There will be no needed parameters but by using this method we should be able to return all posts and their correspond user ids. These posts will be returned in the order of most recent to oldest</li>
      <li>Tests:</li>
    </ul>
  </li>
</ul>
</hr>
</hr>