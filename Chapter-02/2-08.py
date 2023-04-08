"""
File Extensions: Python has a removesuffix() method that works exactly like removeprefix().
Assign the value 'python_notes.txt' to a variable called filename. 
Then use the removesuffix() method to display the filename whitout the file extension, like some file browsers do.
"""

# Example with removeprefix()
url = 'https://www.google.com'
print(f'Domain name: {url.removeprefix("https://")}')

filename = 'python_notes.txt'
print(f'Filename without extension: {filename.removesuffix(".txt")}')