"""
Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162)
or Exercise 9-4 (page 166). 
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
"""
class Restaurant:
    """A class that defines a restaurant with a cuisine type."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initializes a Restaurant with its name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Prints restaurant's name and cuisine type."""
        print(f'Restaurant name is: {self.restaurant_name.title()}, our cuisine type is: {self.cuisine_type.title()}.')

    def open_restaurant(self):
        """Prints a message indicating that the restaurant is open."""
        print(f'The restaurant is open!')
    
    def set_number_served(self, number_served):
        """Updates the value of number_served"""
        if number_served >= self.number_served:
            self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increments number served"""
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """A child class of a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

    def get_flavors(self):
        """Prints the flavors of the stand."""
        for flavor in self.flavors:
            print(f'{flavor}')


stand = IceCreamStand('ice ice baby', 'ice creams', ['lemon', 'vainilla', 'straw berry', 'mint'])
stand.get_flavors()