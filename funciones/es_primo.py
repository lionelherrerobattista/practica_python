#Comprueba si el numero es primo
#Devuelve True = es primo o False = no es primo
def es_primo(x):
	
	contador_divisores = 0
	resultado = True
	
	if x != 0:
		for i in range(1, x + 1):
			print (i)
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

if es_primo(82):
	print ("Es un numero primo")
else:
	print ("No es primo")
