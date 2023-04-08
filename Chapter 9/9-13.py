"""
Dice: Make a class Die with one attribute called sides, which has a default value of 6. 
Write a method called roll die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint


class Die:
    """A class that defines a dice."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


six_die = Die(6)
ten_die = Die(10)
twenty_die = Die(20)

print('Rolling 6 side die 10 times...')
for roll in range(10):
    six_die.roll_die()

print('Rolling 10 side die 10 times...')
for roll in range(10):
    ten_die.roll_die()

print('Rolling 20 side die 10 times...')
for roll in range(10):
    twenty_die.roll_die()
