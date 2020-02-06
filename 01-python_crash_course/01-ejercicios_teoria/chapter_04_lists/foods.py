my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #copio la lista
# ~ friend_foods = my_foods #apunta a la misma lista


my_foods.append('canoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
