#Función que devuelve el texto que recibe al revés
def girar_texto(text):
	
	auxiliar = []
	reverso = ""
	#Guardo el texto en un auxiliar, letra por letra
	for i in text:
		auxiliar.append(i)
	#Recorro el auxilar y concateno cada letra a una cadena
	for i in range(len(auxiliar)-1, -1, -1):
		reverso = reverso + auxiliar[i]
		
	return reverso


