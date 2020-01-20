rivers = {
    'nile': 'egypt',
    'amazonas': 'brazil',
    'yangtsé': 'china',
    }
    
for name, country in rivers.items():
    print("The " + name.title() + " runs through " + country.title())

print("\nNames:")
for name in rivers.keys():
    print(name.title())
    
print("\nCountries:")
for country in rivers.values():
    print(country.title())
