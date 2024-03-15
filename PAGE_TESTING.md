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
Page Description: [mockup](web_page_designs/RecipEASY_Home.pdf) The home page will be a default landing page for the site where you can access the other pages, see a preview of your recently added/saved recipes, see notifications and/or preview the ‘community’ page, or add a new recipe</br>
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

### Login Page
Page Title</br>
Page Description (include a mockup or hand drawn image of the page)</br>
Parameters needed for the page</br>
Data needed to render the page</br>
Link destinations for the page</br>
List of tests for verifying the rendering of the page</br>

### My Recipes Page
Page Title</br>
Page Description (include a mockup or hand drawn image of the page)</br>
Parameters needed for the page</br>
Data needed to render the page</br>
Link destinations for the page</br>
List of tests for verifying the rendering of the page</br>

### Explore
Page Title</br>
Page Description (include a mockup or hand drawn image of the page)</br>
Parameters needed for the page</br>
Data needed to render the page</br>
Link destinations for the page</br>
List of tests for verifying the rendering of the page</br>

### Community
Page Title: Community Page</br>
Page Description: A community page where users can post about recipies.</br>
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
