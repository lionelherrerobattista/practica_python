favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah', 'maria', 'juan']

for name in friends:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking the poll.")
    else:
        print(name.title() + ", please take the poll.")    
