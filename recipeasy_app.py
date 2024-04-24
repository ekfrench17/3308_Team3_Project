###############################################################################
## This is starter code for RecipEASY Flask App
##
## Instructions:
## start vitual environment with . venv/bin/activate
## then run flask --app recipeasy_app run
###############################################################################


###############################################################################
# Resources used to build
# Cory Schafer - Flask Tutorials
# - https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
#
# Code Structure and Best Practices:
# - Effective Python Code Structure - https://youtu.be/v3CSQkPJtAc
###############################################################################


import sqlite3
import random
import datetime
from flask import Flask, url_for, make_response, render_template, session, request, g, redirect, flash

#added flash to pop up a message

from recipeAPI import add_recipe, get_recipe_data, get_all_recipes, get_recipes_by_user, delete_recipe
from community_posts_db import create_post

## 
from user_login_db import create_user, validate_login, update_user, delete_user  # Corrected import statement


# create app to use in this Flask application
app = Flask(__name__) 
# secret key is used to encrypt cookies
app.secret_key = "31xsyBa<VIt8]hD(q;<P18NYYaZyFh6qLeofB[ct"

###############################################################################
## Routes for RecipEASY app include:
##
##     1. static text page, "home"   @app.route('/')
##     2. static text page, "explore"   @app.route('/explore')
##     3. static text page, "community"    @app.route('/community')
##     4. static text page, "my recipes"   @app.route('/recipe')
##

@app.route('/')
def home():
    return render_template("home_page.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['username']
        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        result = create_user(user_id, password, first_name, last_name, email)
        if result:
            flash('Registration successful! Please login to continue.', 'success')  # Message flashing
            return redirect(url_for('login'))  # Redirect to the login page
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['username']
        password = request.form['password']
        if validate_login(user_id, password):  # Correctly pass user_id instead of 'session["userid"]'
            session['user_id'] = user_id  # Store user_id in session
            flash('You are now logged in!', 'success')
            return redirect(url_for('home'))  # Redirect to home after login
        else:
            flash('Invalid username or password', 'error')  # Flash an error message
    return render_template('login.html')

@app.route('/logout')
def logout():
    # Remove user_id from session if it's there
    session.pop('user_id', None)  # Adjust 'user_id' if you use a different key for storing user login information
    flash('You have been logged out.', 'info')  # Optional: Flash a message confirming logout
    return redirect(url_for('home'))  # Redirect to the home page or another appropriate page


@app.route('/recipe/<recipe_name>')
def recipe(recipe_name=None):
    # function returns a list where each item is from a different column
    recipe_data = get_recipe_data(recipe_name)
    if recipe_data == None:
        recipe_data = "No recipe found"
        result = recipe_data
    else:
        result = render_template("recipe_display.html",recipe_data=recipe_data)
    return result

@app.route('/explore')
def explore():
    session["all_recipes"] = get_all_recipes()
    # recipe fields: [ recipeID INT, name string, ingredients list of strings, cook_time INT, directions list of strings]
    return render_template("explore.html", all_recipes=session["all_recipes"])

@app.route('/my_recipes/<user_id>')
def my_recipes(user_id):
    '''function to get and display all the recipes submitted by the given user_id'''
    # good_id = check_user_id(user_id)
    session['user_id'] = user_id
    good_id = True
    if good_id == True:
        session['my_recipes'] = get_recipes_by_user(session['user_id'])
    return render_template("my_recipes.html", my_recipes=session['my_recipes'])

@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/add_new')
def add(message = ""):
    return render_template("add_new.html", message=message)

@app.route('/submitted_recipe', methods=["POST"])
def submitted_recipe():
    recipe_name = ''
    success = False
    message = ''
    
    if request.method == "POST":
        # result is a dictionary; example;
        # {"cook_time":"5","directions":"heat over stove","ingredients":"broth, seasoning","recipeName":"soup"}
        result = request.form
        user_id = "garci446" 
        avg_ratings = 0
        count_submissions = 1
        try:
            cook_time = int(result['cook_time'])
            success, message = add_recipe(result['recipeName'],result['ingredients'],cook_time,result['directions'],avg_ratings,count_submissions,user_id)
            recipe_name = result['recipeName']
        except:
            message = 'cooking time must be an integer greater than 0'
        #add_recipe(recipe_name, ingredients, cook_time, directions, avg_ratings, count_submissions, user_id)
    else: 
        message = "enter recipe"  
    
    if success == True:
        output = render_template("submitted_recipe.html",recipe_name=recipe_name,message=message)
    else:
        output = render_template("add_new.html", message=message)
    
    return output

@app.route("/remove_recipes", methods=["POST"])
def remove_items():
    checked_boxes = request.form.getlist("check")
    for recipe in checked_boxes:
        result = delete_recipe(recipe)
    #session['my_recipes'] = get_recipes_by_user(session['user_id'])
    return redirect(url_for('my_recipes', user_id = session['user_id']))

#### Remove the below routes later for testing development only

@app.route('/test_insert')
def test_insert():
    '''
    test_recipe_name = "homemade_pizza"
    test_ingredients = ["1 pre-made pizza crust",
                            "1/2 cup pizza sauce",
                            "1 cup shredded mozzarella cheese",
                            "1/4 cup sliced pepperoni",
                            "1/4 cup sliced black olives",
                            "1/4 cup sliced mushrooms",
                            "1/4 cup diced bell peppers",
                            "1/4 cup diced onions",
                            "1/4 cup grated Parmesan cheese"]
    test_cooking_time= 45
    test_directions = ["Preheat your oven to 425°F.",
                           "Place the pre-made pizza crust on a baking sheet or pizza stone.",
                           "Spread the pizza sauce evenly over the crust, leaving a small border around the edges.",
                           "Sprinkle the shredded mozzarella cheese evenly over the sauce.",
                           "Arrange the pepperoni, black olives, mushrooms, bell peppers, and onions on top of the cheese.",
                           "Sprinkle the grated Parmesan cheese over the toppings.",
                           "Place the pizza in the preheated oven and bake for 12-15 minutes, or until the crust is golden brown and the cheese is melted and bubbly.",
                           "Remove the pizza from the oven and let it cool for a few minutes before slicing.",
                           "Slice the pizza into wedges and serve hot. Enjoy your delicious homemade pizza!"]
    directions_str = ''
    for item in test_directions:
        directions_str= directions_str + item
    
    ingr_str = ''
    for item in test_ingredients:
        ingr_str = ingr_str + "," + item
        
    test_avg_ratings = 2.5
    test_total_rating_submissions = 2
    test_user= "garci446" '''

    test_user_id = "JP"
    test_password = "123"
    test_first_name = "Jon" 
    test_last_name = "Paul" 
    test_email = "jp@gmail.com"
    
    # Attempt to create the user and capture the result
    creation_success = create_user(test_user_id, test_password, test_first_name, test_last_name, test_email)
    
    # Prepare a response message with user details
    user_details = f"User ID: {test_user_id}, Name: {test_first_name} {test_last_name}, Email: {test_email}"
    
    # Decide on the response based on whether the user was successfully created
    if creation_success:
        print(f"User created successfully: {user_details}")
        return f"User created successfully: {user_details}", 200  # HTTP status code 200 for OK
    else:
        print("Failed to create user")
        return f"Failed to create user. Details attempted: {user_details}", 400  # HTTP status code 400 for Bad Request


@app.route('/view_db')
def view_db():
    db = getattr(g, '_database', None)
    db = g._database = sqlite3.connect('RecipEASYDB')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    result = ["Table Values:"]
    for t in tables :
        result.append("[%s]"%t)
        
        sql = "SELECT * from %s ;"%t
        #result.append("<%s>"%sql)
        cursor.execute(sql)
        for row in cursor.fetchall() : 
            result.append(row)
       
        result.append("")
    db.close()
    #test_output = [str(val) for val in test_output]
    return (result) 

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)

