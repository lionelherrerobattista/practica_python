cars = ['bmw', 'audi', 'toyota', 'subaru']

# Orden alfabético (lista modificada permanentemente):
# ~ cars.sort()
# ~ print(cars)
# Orden alfabético invertido (lista modificada permanentemente):
# ~ cars.sort(reverse = True)
# ~ print(cars)

#Orden alfabético sin modificar:
# ~ print("Here is the original list:")
# ~ print(cars)
# ~ print("\nHere is the sorted list:")
# ~ print(sorted(cars))
# ~ print(sorted(cars, reverse=True)) #invertida
# ~ print("\nHere is the original list again:")
# ~ print(cars)

#Orden invertido:
print(cars)
cars.reverse()
print(cars)
