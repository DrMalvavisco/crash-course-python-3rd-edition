"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let's call it a glossary.
Think of five programming words you've learned about in the previous chapters. 
Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. 
You might print the word followed by a colon and then its meaning, 
or print the word on one line and then print its meaning indented on a second line. 
Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.
"""
glossary = {'function':'A set of instructions that we can call in our program.',
            'if': 'An instruction for conditional execution of a set of code.',
            'for': 'A loop used for iterate over an iterator.',
            'IT': 'Acronym for Information Technologies.',
            'Python': 'A programming language created by Guido Van Rossum.'
}

for word, meaning in glossary.items():
    print(f'{word}:\n\t{meaning}')