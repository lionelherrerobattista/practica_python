# ~ import pizza # importa todas las funciones
# ~ from pizza import make_pizza #importo una sola función
# Alias:
# ~ from pizza import make_pizza as mp
import pizza as p

# ~ pizza.make_pizza(16, 'pepperoni')
# ~ pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# ~ make_pizza(16, 'pepperoni')
# ~ make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Alias:
# ~ mp(16, 'pepperoni')
# ~ mp(12, 'mushrooms', 'green peppers', 'extra cheese')

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
