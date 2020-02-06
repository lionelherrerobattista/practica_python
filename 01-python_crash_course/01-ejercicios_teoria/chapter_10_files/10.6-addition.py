

while True:
    print("\nWrite two numbers to add:")
    print("(or write 'q' to exit)")

    try:
        number_one = input("\nNumber one: ")
        if number_one == 'q':
            break
        number_one = int(number_one)
    except ValueError:
        print("\nYou must enter a number!")
        continue

    try:
        number_two = input("Number two: ")
        if number_two == 'q':
            break
        number_two = int(number_two)
    except ValueError:
        print("\nYou must enter a number!")
        continue
        
    addition = number_one + number_two
    print("Result: " + str(addition))
