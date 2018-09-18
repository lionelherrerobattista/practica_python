#Suma los dígitos de un numero
def sumar_digitos(n):
	resultado = 0
	numero = n
	while numero >= 1:
	  #Tomo el numero de la derecha
	  digito_derecha = numero % 10
	  resultado += digito_derecha
	  print (resultado)
	  #floor division (redondea el resultado de la division para abajo)
	  # /10 saca el numero a la derecha
	  numero = numero // 10
	return resultado

#Otra forma: (pasando nro. a str y a int)
"""def digit_sum(n):
  result = 0
  for i in str(n):
    result += int(i)
    print i
  return result"""

print ("El resultado es:", sumar_digitos(136))





