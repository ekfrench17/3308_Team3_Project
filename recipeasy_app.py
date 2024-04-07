###############################################################################
## This is starter code for RecipEASY Flask App
##
## Instructions:
## start vitual environment with . venv/bin/activate
## then run flask --app recipeasy_app run
###############################################################################


###############################################################################
import prefix

from flask import Flask, url_for, make_response, render_template

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

###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)

