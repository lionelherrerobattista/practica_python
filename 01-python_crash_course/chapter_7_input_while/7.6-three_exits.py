prompt = "\nTell me your age and I will tell you how much you have to pay:"
prompt += "\n(Type 'quit' to exit) "

age = ''
# conditional test
while age != 'quit':
    age = input(prompt)
    
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("\nYour ticket is free.")
        elif age <= 12:
            print("\nYour ticket is $10.")
        else:
            print("\nYour ticket is $15.")

    
# active variable
active = True

# ~ while active:
    # ~ age = input(prompt)
    
    # ~ if age == 'quit':
        # ~ active = False
    # ~ else:    
        # ~ age = int(age)
        
        # ~ if age < 3:
            # ~ print("\nYour ticket is free.")
        # ~ elif age <= 12:
            # ~ print("\nYour ticket is $10.")
        # ~ else:
            # ~ print("\nYour ticket is $15.")


# break:
# ~ while True:
    # ~ age = input(prompt)
    
    # ~ if age == 'quit':
        # ~ break
    
    # ~ age = int(age)
    
    # ~ if age < 3:
        # ~ print("\nYour ticket is free.")
    # ~ elif age <= 12:
        # ~ print("\nYour ticket is $10.")
    # ~ else:
        # ~ print("\nYour ticket is $15.")
