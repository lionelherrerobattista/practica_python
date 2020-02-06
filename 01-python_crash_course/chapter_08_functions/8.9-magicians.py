def show_magicians(magicians):
    """Shows magicians in a list"""
    print("List of magicians:")
    for magician in magicians:
        print(magician.title())
        
magicians = ['merlin', 'harry potter', 'gandalf']
show_magicians(magicians)
