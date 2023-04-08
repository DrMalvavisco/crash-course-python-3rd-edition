"""
Restaurant: Make a class called Restaurant. 
The init () method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant () that prints these two pieces of information, 
and a method called open_restaurant () that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. 
Print the two attributes individually, and then call both methods.
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
    


restaurant = Restaurant('little lemon', 'desserts')
print(f'(dot notation) Restaurant name is: {restaurant.restaurant_name}, cuisine type is: {restaurant.cuisine_type}')
restaurant.describe_restaurant()
restaurant.open_restaurant()

