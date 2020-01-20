prompt = "How many people are in the dinner group? "
people = input(prompt)

people = int(people) # Casteo a int para comparar

if people >= 8:
    print("Sorry. You'll have to wait for a table.")
else:
    print("Your table is ready.")


