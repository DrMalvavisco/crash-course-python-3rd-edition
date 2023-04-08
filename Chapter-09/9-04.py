"""
Number Served: Start with your program from Exercise 9-1 (page 162). 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who've been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business.
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
        
    

restaurant = Restaurant('little lemon', 'desserts')
print(f'Number of customers served: {restaurant.number_served}')
restaurant.number_served = 10
print(f'Number of customers served: {restaurant.number_served}')

restaurant.set_number_served(20)
print(f'Number of customers served: {restaurant.number_served}')

restaurant.increment_number_served(100)
print(f'Number of customers served: {restaurant.number_served}')
