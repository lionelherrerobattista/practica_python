cities = {
        'los angeles': {
            'country': 'united states',
            'population': 3792621,
            'fact': "Founded in 1781",
            },
        'paris': {
            'country': 'france',
            'population': 2140526,
            'fact': "Europe's major center",
            },
        'moscow': {
            'country': 'russia',
            'population': 15000000,
            'fact': "Coldest megacity in Earth",
            },
    }
    
for city, information in cities.items():
    name = city
    print("Name: " + name.title())
    
    for data, description in information.items():
            print("\t" + data.title() + ": " + str(description).title())
    
    
    
