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

</hr>