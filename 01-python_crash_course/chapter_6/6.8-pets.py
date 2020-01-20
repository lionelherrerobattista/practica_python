milu = {
    'name': 'milu',
    'kind': 'dog',
    'owner': 'tintin',
    }
    
garfield = {
    'name': 'garfield',
    'kind': 'cat',
    'owner': 'jon',
    }

snoopy = {
    'name': 'snoopy',
    'kind': 'dog',
    'owner': 'charlie',
    }

pets = [milu, garfield, snoopy]

for pet in pets:
    name = pet['name']
    kind = pet['kind']
    owner = pet['owner']
    
    print("Name: " + name.title())
    print("Kind of animal: " + kind.title())
    print("Owner: " + owner.title() + "\n")


