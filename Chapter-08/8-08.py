"""8-8. User Albums: Start with your program from Exercise 8-7. 
Write a while loop that allows users to enter an album's artist and title. 
Once you have that information, call make_album() with the user's input and 
print the dictionary that's created. Be sure to include a quit value in the while loop.
"""
def make_album(artist, title, n_songs=None):
    album = {'name': artist, 'title': title}
    if n_songs:
        album['n_songs'] = n_songs
    return album

while True:
    print('\n Album information:')
    print("(enter 'q' at any time to quit)")

    name = input('Album artist: ')
    if name == 'q':
        break

    title = input('Album title: ')
    if title == 'q':
        break

    n_songs = input('N. of songs (Optional, press enter to skip): ')
    print(make_album(name, title, int(n_songs))) if n_songs else print(make_album(name, title)) 


    
