"""More Guests:
You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
Start with your program from exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
Use insert() to add one new guest to the beginning of your list.
Use insert() to add one new guest to the middle of your list.
Use append() to add one new guest to the end of your list.
Print a new set of invitation messages, one for each person in your list."""

"""Changing Guest List:
You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations.
You'll have to think of someone else to invite.

Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can't make it.
Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
Print a second set of invitation messages, one for each person who is still in your list."""

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




