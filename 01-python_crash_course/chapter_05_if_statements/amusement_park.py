age = 12

if age < 4:
    # ~ print("Your admmission cost is $0.")
    price = 0
elif age < 18:
    # ~ print("Your admission cost is $5.")
    price = 5
elif age < 65:
    price = 10
# ~ else:
elif age >= 65:
    # ~ print("Your admission cost is $10.")
    price = 5

print("Your admission cost is $" + str(price) + ".")
    
