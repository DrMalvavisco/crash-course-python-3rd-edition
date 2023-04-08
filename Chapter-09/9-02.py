"""
Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant () for each instance.
"""
class Restaurant:
    """A class that defines a restaurant with a cuisine type."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes a Restaurant with its name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant's name and cuisine type."""
        print(f'Restaurant name is: {self.restaurant_name.title()}, our cuisine type is: {self.cuisine_type.title()}.')

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f'The restaurant is open!')
    
little_lemon = Restaurant('little lemon', 'desserts')
el_fogon =  Restaurant('el fogon', 'mexican food')
las_tres_estrellas = Restaurant('las tres estrellas', 'cortes argentinos')

little_lemon.describe_restaurant()
el_fogon.describe_restaurant()
las_tres_estrellas.describe_restaurant()


