"""
Guest: Write a program that prompts the user for their name. 
When they respond, write their name to a file called guest.txt.
"""
from pathlib import Path
path = Path('guest.txt')
guest = input('What is your name?: ')
path.write_text(guest)
