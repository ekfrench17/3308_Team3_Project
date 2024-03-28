# How To Set Up Enviorment and Run Application

### Install Flask (If not already installed)

Open Terminal <br>

`pip install flask`

### Run a Local Server

In Terminal type:<br>

`export FLASK_APP=recipeasy.app.py`

`flask run`

This should provide address on local machine:<br>
ex: * Running on http://127.0.0.1:5000<br>




*********************************************************

### Steps for Setting Up SQL Database

In Terminal install SQLalchemy

`pip install flask-sqlalchemy`
    
    -this is a flask specific extension

In recipeasy_app.py import flask_sqlalchemy

`from flask_sqlalchemy import SQLAlchemy`

Create Database instance:



`db = SQLAlchemy(app)`


Create class models:

Example for profile:

`class User(db.Model):`
`   id =  db.Column(db.Integer. primary_key=True`
`   username = db.Column(db.String(20), unigue=True, nullable=False`
`   username = db.Column(db.String(120), unigue=True, nullable=False`
`   image_file = db.Column(db.String(20), unique=False, default='default.jpg')`
`   password = db.Column(db.String(60), nullable=False)`

`   def --repr--(self):`
`       return f"User('{self.username}', '{self.email}', '{self.image_file}')"`


* Use excel spread sheet for reference
* There will be differnt classes for each table


### In terminal


