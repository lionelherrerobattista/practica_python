def make_album(artist, title):
    album = {'artist': artist, 'title': title}
    
    return album
    
while True:
    print("\nEnter artist and title of the album")
    print("(write 'q' to exit)")
    
    artist = input("Artist: ")
    if artist == 'q':
        break
        
    title = input("Title: ")
    if title == 'q':
        break
    
    new_album = make_album(artist, title)
    
    print(new_album)
    
