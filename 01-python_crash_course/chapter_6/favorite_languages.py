#Muchos elementos, separar en varias líneas.
# ~ favorite_languages = {
    # ~ 'jen': 'python',
    # ~ 'sarah': 'c',
    # ~ 'edward': 'ruby',
    # ~ 'phil': 'python',
    # ~ }

#Print muy largo, separar en varias líneas.    
# ~ print("Sarah's favorite language is " +
    # ~ favorite_languages['sarah'].title() +
    # ~ ".")

# Loop:
# ~ for name, language in favorite_languages.items():
    # ~ print(name.title() + "'s favorite language is " + language.title() + ".")

# Solo las keys:
# ~ friends = ['phil', 'sarah']

# ~ for name in favorite_languages.keys():
    # ~ print(name.title())
    
    # ~ if name in friends:
        # ~ print(" Hi " + name.title() +
            # ~ ", I see your favorite language is " +
            # ~ favorite_languages[name].title() + "!")

# El método keys() devuelve una lista de claves
# ~ if 'erin' not in favorite_languages.keys():
    # ~ print("Erin, please take our poll!")
    
# Claves ordenadas:
# ~ for name in sorted(favorite_languages.keys()):
    # ~ print(name.title() + ", thank your for taking the poll.")

# Valores del diccionario:
# ~ print("The following languages have been mentioned:")
# ~ for language in favorite_languages.values():
    # ~ print(language.title())
    
# Valores sin repetir:
# ~ print("The following languages have been mentioned:")
# ~ for language in set(favorite_languages.values()):
    # ~ print(language.title())
    
# Listas dentro de un diccionario:
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
    else:
        print("\n" + name.title() + "'s favorite language is:")
    for language in languages:
        print("\t" + language.title())

