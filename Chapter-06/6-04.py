"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 
(page 99) by replacing your series of print () calls with a loop that runs through the dictionary's keys and values. 
When you're sure that your loop works, add five more Python terms to your glossary. 
When you run your program again, these new words and meanings should automatically be included in the output.
"""
glossary = {'function':'A set of instructions that we can call in our program.',
            'if': 'An instruction for conditional execution of a set of code.',
            'for': 'A loop used for iterate over an iterator.',
            'IT': 'Acronym for Information Technologies.',
            'Python': 'A programming language created by Guido Van Rossum.',
            'OOP': 'Acronym for "Object Oriented Programming".',
            'WWW':'Acronym for World Wide Web.',
            'W3C':'Acronym for World Wide Web Consortium.',
            'AWS':'Acronym for Amazon Web Services.',
            'HTML':'HyperText Markup Language, used for structure and semantics of a website. '
}

for word, meaning in glossary.items():
    print(f'{word}:\n\t{meaning}')