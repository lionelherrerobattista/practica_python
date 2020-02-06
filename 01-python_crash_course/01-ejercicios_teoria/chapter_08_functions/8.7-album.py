def make_album(artist, title, tracks=''):
    if tracks:
        album = {'artist': artist, 'title': title, 'tracks': tracks}
    else:
        album = {'artist': artist, 'title': title}
    
    return album

new_album = make_album('the beatles', 'abbey road')
print(new_album)


new_album = make_album('soda stereo', 'canción animal')
print(new_album)

new_album = make_album('oasis', 'definitely maybe')
print(new_album)

new_album = make_album('oasis', 'be here now', 10)
print(new_album)
