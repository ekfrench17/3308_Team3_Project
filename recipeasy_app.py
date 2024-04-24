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

from recipeAPI import add_recipe, get_recipe_data, get_all_recipes, my_recently_added, get_recipes_by_user

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
    ##Will need to pass session ['user_id'] to html for configuring dynamic endpoints
    ##The code below is for testing and will need to be removed after login table has been setup


    
    session['user_id'] = 'garci449'
    return render_template("home_page.html", user_id=session['user_id'])

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

@app.route('/recently_added/<user_id>')
def pull_recent_user_recipes (user_id):
    ##is logic is built around testing and should be refined one seccion['user_id'] has been established
    ##session["user_id"]  = "garcitest"
    #Below is set a test until a session variable that catches the user id created
    user_recent_recipes = my_recently_added(user_id)
    return render_template("my_recent_recipes.html", user_recent_recipes=user_recent_recipes)


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
        result = "enter recipe"
    return recipe

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