prompt = "Write a number to check if it is a multiple of 10: "
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(str(number) + " is multiple of 10.")
