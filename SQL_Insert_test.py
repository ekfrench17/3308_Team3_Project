#!/usr/bin/bash

import sqlite3
import random
import datetime

def test_insert():
    conn = sqlite3.connect('RecipEasyDB')
    db = conn.cursor()
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
    db.execute("INSERT INTO RecipesTable Values(?,?,?,?,?,?,?,?,?,?);",(
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
    conn.commit()
    conn.close()
    print("INSERTION HAS COMPLETED")
    return
if __name__ == '__main__':
    test = test_insert()