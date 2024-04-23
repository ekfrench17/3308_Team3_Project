###############################################################################
## This is starter code for RecipEASY Flask App
##
## Instructions:
## start vitual environment with . venv/bin/activate
## then run flask --app recipeasy_app run
###############################################################################


###############################################################################
import sqlite3
import random
import datetime
from flask import Flask, url_for, make_response, render_template, session, request, g, redirect

from recipeAPI import add_recipe, get_recipe_data, get_all_recipes

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

############### Changes ########
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session["user_id"] = None  # Adjust based on your user ID strategy

        password = request.form['password']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        response = create_user('RecipEASYDB.db', session["user_id"], password, first_name, last_name, email)
        return response
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session["user_id"] = request.form['username']
        password = request.form['password']
        if validate_login('RecipEASYDB.db', session["userid"], password):
            session['user_id'] = session["userid"]  # Store username in session
            return redirect(url_for('home'))  # Redirect to home after login
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from session
    return redirect(url_for('home'))


################### 



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

@app.route('/community')
def community():
    return render_template("community.html")

@app.route('/add_new')
def add():
    if request.method == "POST":
        result = request.form
    else: 
        result = "enter recipe"
    return render_template("add_new.html",result=result)

@app.route('/submitted_recipe', methods=["POST"])
def submitted_recipe():
    if request.method == "POST":
        # result is a dictionary; example;
        # {"cook_time":"5","directions":"heat over stove","ingredients":"broth, seasoning","recipeName":"soup"}
        result = request.form
        user_id = "garci446" 
        avg_ratings = 0
        count_submissions = 1
        recipename, ingredients = result['recipeName'], result['ingredients']
        recipe = [recipename, ingredients]
    else: 
        result = "enter recipe"
    return recipe

@app.route('/test_insert')
def test_insert():
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
    test_user= "garci446" 
    # add_recipe function from recipeAPI.py module
    test_output = add_recipe(test_recipe_name, ingr_str, test_cooking_time, directions_str, test_avg_ratings, test_total_rating_submissions, test_user)
    return(test_output)

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

