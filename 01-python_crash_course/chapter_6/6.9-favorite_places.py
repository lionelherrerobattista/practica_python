favorite_places = {
    'juan': ['brazil', 'france', 'india'],
    'maria': ['russia', 'ukraine'],
    'josé': ['italy'],
    }
    
for person, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + person.title() + "'s favorite places are:")
    else:
        print("\n" + person.title() + "'s favorite place is:")
        
    for place in places:
        print("\t " + place.title())
