motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Append:
# ~ motorcycles.append('ducati')
# ~ print(motorcycles)

#Creación de lista dinámica:
# ~ motorcycles = []

# ~ motorcycles.append('honda')
# ~ motorcycles.append('yamaha')
# ~ motorcycles.append('suzuki')

#Insertar en un índice específico:
# ~ print(motorcycles)
# ~ motorcycles.insert(0, 'ducati')

#Del:
# ~ del motorcycles[0]
# ~ print(motorcycles)
# ~ del motorcycles[1]

#Pop:
# ~ popped_motorcycle = motorcycles.pop()
# ~ print(motorcycles)
# ~ print(popped_motorcycle)

# ~ last_owned = motorcycles.pop()
# ~ print('The last motorcycle I owned was a ' + last_owned.title() + '.')


# ~ first_owned = motorcycles.pop(0)
# ~ print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Remove (por valor):
# ~ motorcycles.remove('honda')
# ~ print(motorcycles)

too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
