"""
Imported Restaurant: Using your latest Restaurant class, store it in a module.
Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant's methods 
to show that the import statement is working properly.
"""
from restaurant import Restaurant

restaurant = Restaurant('little lemon', 'desserts', 250)

restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.number_served)
