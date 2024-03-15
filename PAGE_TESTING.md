# Web Page Design Milestone 4
## A list of descriptions for each page that will be implemented for the project

### Summary of Pages:
* Home Page
* Login Page
* My Recipes Page
* Explore - Search Page
* Community - Social Page
* Add New Recipe Page

### Home Page
Page Title: RecipEASY</br>
Page Description: [Home Page Mockup](web_page_designs/RecipEASY_Home.pdf) The home page will be a default landing page for the site where you can access the other pages, see a preview of your recently added/saved recipes, see notifications and/or preview the ‘community’ page, or add a new recipe</br>
Parameters needed for the page:‘/’</br>
Data needed to render the page: 
* an html sheet for the frontend (and copy)
* links for the other pages
* data pulled in for the preview sections (if possible)</br>
Link destinations for the page: links for the other 4 pages will be on the home page as a navigation bar for easy navigation</br>

List of tests for verifying the rendering of the page:</br>
* navigation bar is working
* response design testing - the screen size doesn't change how the page works or is navigated, everything is still responsive
* each preview of the other pages is appearing correctly and the links work
* everything is loaded properly (images and text etc)

### User/Profile Page
Page Title: User Profile</br>
[Profile Page Mockup](web_page_designs/Profile_Page_Mockup.png)
Page Description:</br>
- The User Profile page displays the personal details of the user</br>
- Editable Information (Name, Username, Password)</br>
- Their activity history saved recipes </br>
- It should have a clean, user-friendly layout with distinct sections for different information types. </br>

Parameters Needed for the Page:</br>
- userID: Unique identifier for the user to fetch the correct profile data.</br>
- sessionToken: To ensure that the user is authenticated and to maintain session security.</br>

Data Needed to Render the Page:</br>
- User personal details (name, email, etc.)</br>
- List of recent user activities (e.g., personal recipes/saved recipes)</br>
- Account settings (name, email, password, account management options)</br>

Link Destinations for the Page:</br>
- Home/Feed: Redirects to the main content feed.</br>
- Edit Profile: Allows the user to modify their profile details.</br>
- Recipes: Allows user to see their recipes (Personal/Saved)</br>
- Logout: A link for the user to log out of their account.</br>

List of Tests for Verifying the Rendering of the Page:</br>
- User Data Display Test: Verify that all user data (profile picture, name, email, etc.) is correctly fetched and displayed.
- Responsive Design Test: Ensure that the page is responsive and renders well on different devices and screen sizes.
- Link Functionality Test: Test all links on the page (Edit Profile, Settings, Logout, etc.) to ensure they redirect correctly.
- Loading Performance Test: Check that the page loads within an acceptable time frame, with all elements rendering correctly.
- Security Test: Ensure that the page does not render without a valid sessionToken, preventing unauthorized access.
- User Interaction Test: Confirm that interactive elements (like edit buttons, settings options) respond correctly to user input.
- Error Handling Test: Verify that the page handles errors gracefully (e.g., displays user-friendly error messages if data fails to load).


### My Recipes Page
Page Title</br>
Page Description (include a mockup or hand drawn image of the page)</br>
Parameters needed for the page</br>
Data needed to render the page</br>
Link destinations for the page</br>
List of tests for verifying the rendering of the page</br>

### Explore
Page Title: Search</br>

Page Description [mockup](web_page_designs/search.jpg) This is the page that will give options for searching the recipes in the database. There will be options to search by ingredient, title, and a button to generate a random recipe. [mockup](web_page_design/search_results.JPG) This is the page that will display the results of the search (except the "Surprise me" button- it will jump straight to recipe display. [mockup](web_page_designs/recipe_display.JPG) This is the page where the recipe will be displayed for the user.</br> 

Parameters needed for the page: '/search' '/search_results' and '/recipe_display'</br>

Data needed to render the page: 
* html pages for each of the three outlined above: search, search_results, and recipe_display
* a css style sheet to format and add colors
* links to each other and the home page
* data from the recipe and user database</br>

Link destinations for the page: the link destination for the search page will be on the home page, the recipe display will be on the user profile page and attached to the search results page. The search results page will be a link from the search page, and the recipe display page will be linked to the results page and well as the surprise me button in the search.</br>

List of tests for verifying the rendering of the page:
* valid search paramters
* working links to recipe display, search, and results
* image display working correctly
* database access is correct for recipe
* button links correctly correspond
* error friendly message printed if parameters for search are not met
</br>


### Community
Page Title: Community Page</br>
Page Description: A community page where users can post about recipies.[mockup](web_page_designs/Community_Page.png)</br>
Parameters needed for the page @app.route('/community_page')</br>
Data needed to render the page:
* HTML, CSS, and Javascript programs for the UI of commmunity page.
* previous post data from users 
* links for a menu/toggle scetion to direct me to the other pages </br>
Link destinations for the page:</br>
* Links for the 4 other pages on the site including the home page</br>
List of tests for verifying the rendering of the page:</br>
* Validate previous posts are seen from other users in decending order (oldest to newest)
* Valitdate you can make your own post
* Validate you can see your previous post
* Validate you can scroll up to first post.
* Validate you can scroll down to most recent post
</br>

### Add New Recipe Page
Page Title: Add New Recipe</br>
Page Description: [mockup](web_page_designs/RecipEASY_addNew.pdf) Page to input a new recipe to the my recipes archive</br>
Parameters needed for the page: @app.route('/my_recipes/add_new')</br>
Data needed to render the page: an input form for recipe data</br>
Link destinations for the page:
* navigation bar on the page
* cancel - return to my recipes page
* save - save recipe to DB and return to my recipes page</br>

List of tests for verifying the rendering of the page:
* verify the form is ready for input / connected to database
* verify submit working correctly
* verify cancel returns to the previous page
* verify data was input to database</br>
