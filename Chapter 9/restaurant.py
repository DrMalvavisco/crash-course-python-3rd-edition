"""A module with a Restaurant class"""


class Restaurant:
    """A class that defines a restaurant with a cuisine type."""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initializes a Restaurant with its name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Prints restaurant's name and cuisine type."""
        print(
            f'Restaurant name is: {self.restaurant_name.title()}, our cuisine type is: {self.cuisine_type.title()}.')

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
