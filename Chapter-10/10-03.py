"""
Simpler Code: The program file_reader py in this section uses a temporary variable, 
lines, to show how splitlines () works. 
You can skip the temporary variable and loop directly over the list that splitlines () returns:
for line in contents.splitlines ():
Remove the temporary variable from each of the programs in this section, to make them more concise.
"""
from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()

print('Printing  by reading the entire file:')
print(content)

print('Printing by iterating over list:')
for line in content.splitlines():
    print(line)