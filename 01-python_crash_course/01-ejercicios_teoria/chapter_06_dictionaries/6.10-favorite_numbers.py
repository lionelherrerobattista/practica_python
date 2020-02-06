favorite_numbers = {
    'lionel': [8, 4],
    'matías': [5,1,3],
    'maría': [20],
    'gonzalo': [3,4],
    'graciela': [4],
    }
    
    
for person, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print("\n" + person.title() + "'s favorite numbers are:")
    else:
        print("\n" + person.title() + "'s favorite number is:")
        
    for number in numbers:
        print("\t " + str(number))
