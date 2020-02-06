responses = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world," +
        " where would you go? ")
    
    responses[name] = place
    
    repeat = input("Would you like to" +
        "let another person respond? (yes / no) ")
    
    if repeat == 'no':
        active = False

# Muestro:
print("\n--- Poll Results ---")
for name, place in responses.items():
    print(name.title() + " would like to go to " + place.title())
