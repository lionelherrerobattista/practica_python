current_number = 0 # inicio la variable

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue # salta a la siguiente iteración
    
    print(current_number)
