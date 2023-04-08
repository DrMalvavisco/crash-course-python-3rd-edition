"""Shrinking Guest List: You just found out that your new dinner table won't arrive in time for the dinner, 
and now you have spaces for only two guests.

Start with the program from exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.

Use pop() to remove guests from your list one at time until only two names remain in your list. Each time you pop a name from your list,
print a message to that person letting them know you're sorry you can't invite them to dinner.

Print a message to each of the two people sill in your list, letting them know  they're still invited.

Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure actually have an empty list at
the end of your program."""

guests = ['Maradona', 'Messi', 'CR7', 'Robin Van Persie', 'Freddie', 'Elvis']

print(f'Hello {guests[0]}, please come to my dinner.')
print(f'Hello {guests[1]}, please come to my dinner.')
print(f'Hello {guests[2]}, please come to my dinner.')
print(f'Hello {guests[3]}, please come to my dinner.')
print(f'Hello {guests[4]}, please come to my dinner.')
print(f'Hello {guests[5]}, please come to my dinner.')

print(f"\nOh, {guests[3]} can't make the dinner, so sorry. New guests invitations.\n")

guests.insert(3, 'Steve Vai')
del guests[4]

print(f'Hello {guests[0]}, please come to my dinner.')
print(f'Hello {guests[1]}, please come to my dinner.')
print(f'Hello {guests[2]}, please come to my dinner.')
print(f'Hello {guests[3]}, please come to my dinner.')
print(f'Hello {guests[4]}, please come to my dinner.')
print(f'Hello {guests[5]}, please come to my dinner.')

print("\nI found a bigger table! that means, 3 more guests to my dinner!\n")

guests.insert(0, 'Shakira')
guests.insert(3, 'Robbie')
guests.append('Ramon')

print(f'Hello {guests[0]}, please come to my dinner.')
print(f'Hello {guests[1]}, please come to my dinner.')
print(f'Hello {guests[2]}, please come to my dinner.')
print(f'Hello {guests[3]}, please come to my dinner.')
print(f'Hello {guests[4]}, please come to my dinner.')
print(f'Hello {guests[5]}, please come to my dinner.')
print(f'Hello {guests[6]}, please come to my dinner.')
print(f'Hello {guests[7]}, please come to my dinner.')
print(f'Hello {guests[8]}, please come to my dinner.')

print("--------------------------------------------------\n")
print("Oh no, The table won't arrive at time!\n")

print(f"I'm so sorry {guests.pop()}, but I can't invite you to the dinner.")
print(f"I'm so sorry {guests.pop()}, but I can't invite you to the dinner.")
print(f"I'm so sorry {guests.pop()}, but I can't invite you to the dinner.")
print(f"I'm so sorry {guests.pop()}, but I can't invite you to the dinner.")
print(f"I'm so sorry {guests.pop()}, but I can't invite you to the dinner.")
print(f"I'm so sorry {guests.pop()}, but I can't invite you to the dinner.")
print(f"I'm so sorry {guests.pop()}, but I can't invite you to the dinner.")
print("--------------------------------------------------\n")
print(f'{guests[0]}, you are still invited to the dinner.')
print(f'{guests[1]}, you are still invited to the dinner.')

del guests[1]
del guests[0]

print(guests)