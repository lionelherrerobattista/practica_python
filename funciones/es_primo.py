#Comprueba si el numero es primo
#Devuelve True = es primo o False = no es primo
def es_primo(x):
	
	contador_divisores = 0
	resultado = True
	
	if x != 0:
		for i in range(1, x + 1):
			#Busco la cantidad de divisores del numero
			if x % i == 0:
				contador_divisores += 1
			#Si tiene más de dos divisores no es primo
			if contador_divisores > 2:
				resultado = False
				break
	else:
		resultado = False
		
	return resultado
	
#Otra forma:
"""
def is_prime(x):
  print x
  #Si es menor a 2 es NO es primo
  if x < 2:
    return False
  else:
	#Si hay otro divisor, dejando afuera a 1 y a sí mismo, NO es primo
    for n in range(2, x-1):
      if x % n == 0:
        return False
    else:
      return True
"""

if es_primo(82):
	print ("Es un numero primo")
else:
	print ("No es primo")
