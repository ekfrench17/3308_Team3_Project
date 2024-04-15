###############################################################################
## This is starter code for RecipEASY Flask App
##
## Instructions:
## start vitual environment with . venv/bin/activate
## then run flask --app recipeasy_app run
###############################################################################


###############################################################################

from flask import Flask, url_for, make_response, render_template, g
import sqlite3
import random
import datetime

# create app to use in this Flask application
app = Flask(__name__)  

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

@app.route('/recipe')
def recipe():
    return render_template("recipe_display.html")

@app.route('/explore')
def explore():
    return render_template("explore.html")

@app.route('/community')
def community():
    return 'community page'

@app.route('/add_new')
def add():
    return render_template("add_new.html")

@app.route('/test_insert')
def test_insert():
    db = getattr(g, '_database', None)
    test_recipe_name = "Homemade Pizza"
    test_ingredients = ("pre-made pizza crust",
                            "cup pizza sauce",
                            "shredded mozzarella cheese",
                            "sliced pepperoni",
                            "sliced black olives",
                            "sliced mushrooms",
                            "diced bell peppers",
                            "diced onions",
                            "grated Parmesan cheese")
    test_quantity = ["1",
                         "1/2 cup",
                         "1 cup",
                         "1/4 cup",
                         "1/4 cup",
                         "1/4 cup",
                         "1/4 cup",
                         "1/4 cup",
                         "1/4 cup"]
    test_cooking_time= "45 minutes"
    test_directions = ["Preheat your oven to 425°F.",
                           "Place the pre-made pizza crust on a baking sheet or pizza stone.",
                           "Spread the pizza sauce evenly over the crust, leaving a small border around the edges.",
                           "Sprinkle the shredded mozzarella cheese evenly over the sauce.",
                           "Arrange the pepperoni, black olives, mushrooms, bell peppers, and onions on top of the cheese.",
                           "Sprinkle the grated Parmesan cheese over the toppings.",
                           "Place the pizza in the preheated oven and bake for 12-15 minutes, or until the crust is golden brown and the cheese is melted and bubbly.",
                           "Remove the pizza from the oven and let it cool for a few minutes before slicing.",
                           "Slice the pizza into wedges and serve hot. Enjoy your delicious homemade pizza!"]
    test_avg_ratings = 2.5
    test_total_rating_submissions = 2
    test_user= "garci446" 
    db = g._database = sqlite3.connect('RecipEasyDB')
    cursor = db.cursor()
    cursor.execute("INSERT INTO RecipesTable Values(?,?,?,?,?,?,?,?,?,?);",(
                                                        None,
                                                        test_recipe_name,
                                                        test_ingredients[1],
                                                        test_quantity[1],
                                                        test_cooking_time,
                                                        test_directions[0],
                                                        test_avg_ratings,
                                                        test_total_rating_submissions,
                                                        test_user,
                                                        datetime.datetime.now().timestamp()                                             
        )) 
    cursor.execute("SELECT * FROM RecipesTable;")
    test_output = cursor.fetchall()
    test_output = [str(val) for val in test_output]
    db.close()
    return(test_output)
###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.

    
    app.run(host='0.0.0.0', port=3308)

