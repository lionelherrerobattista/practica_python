prompt = "\nTell me your age and I will tell you how much you have to pay:"
prompt += "\n(Type 'quit' to exit) "

age = ''

while True:
    age = input(prompt)
    
    if age == 'quit':
        break;
    
    age = int(age)
    
    if age < 3:
        print("\nYour ticket is free.")
    elif age <= 12:
        print("\nYour ticket is $10.")
    else:
        print("\nYour ticket is $15.")
