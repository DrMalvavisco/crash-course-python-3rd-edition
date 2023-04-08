"""4-5. Summing a Million: Make a list of the numbers from one to one million, 
and then use min() and max() to make sure your list actually starts at one and ends at one million. 
Also, use the sum() function to see how quickly Python can add a million numbers.
"""

numbers = list(range(1,1_000_001))

print(f'Min value: {min(numbers)}\nMax value: {max(numbers)}\nSum of the numbers: {sum(numbers)}')