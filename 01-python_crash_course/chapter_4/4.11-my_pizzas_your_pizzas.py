pizzas = ["muzzarella", "napolitana", "calabresa"]
friends_pizzas = pizzas[:] #creo una copia

pizzas.append('marinara')
friends_pizzas.append('margherita')

print("Mis pizzas favoritas son:")
for pizza in pizzas:
	print(pizza)

print("\nLas pizzas favoritas de mi amigo son:")
for pizza in friends_pizzas:
	print(pizza)
