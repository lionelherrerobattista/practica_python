#Función que calcula el factorial de un numero 
#y devuelve el factorial
def factorial(x):
	factorial = x
	#range se ejecuta hasta x-1
	if x != 0:
	  for i in range(1, x):
		  factorial = factorial * (x - i) #uso x -1 en lugar de factorial (sino cambia valor de x)
	else:
	  factorial = 1
	  
	return factorial
  
print (factorial(0))
