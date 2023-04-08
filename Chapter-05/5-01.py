"""5-1. Conditional Tests: Write a series of conditional tests. 
Print a statement describing each test and your prediction for the results of each test.
Look closely at your results, and make sure you understand why each line evaluates to True or False.
Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.
"""
car = "camaro"

print('I think car == "camaro" is True')
print(car == 'camaro')

print('I think car != "ferrari" is True')
print(car != 'ferrari')

print('I think car == car is True')
print(car == car)

print('I think car < "ferrari" is True')
print(car < 'ferrari')

print('I think car > "audi" is True')
print(car > 'audi')

#False conditions 

print('I think car == "audi" is False')
print(car == 'audi')

print('I think car == car.lower() is False')
print(car ==  car.lower())

print('I think car < "audi" is False')
print(car < 'audi')

print('I think car.lower() == car.upper() is False')
print(car.lower() == car.upper())

print('I think car != "camaro" is False')
print(car != 'camaro')
