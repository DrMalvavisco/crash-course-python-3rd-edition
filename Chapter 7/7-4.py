"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit value. 
As they enter each topping, print a message saying you'll add that topping to their pizza.
"""
prompt = """Which topping you want to add to the pizzza?
Enter 'quit' to finish adding toppings: """
topping = ""

while topping != 'quit':

    topping = input(prompt).strip()

    if topping != 'quit':
        print(f'Adding {topping} to the pizza!')
