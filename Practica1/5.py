#5. Escriba un programa de Python para obtener una sola cadena de dos cadenas dadas, separadas por un espacio, adem�s de intercambiar los dos primeros caracteres de cada cadena.
#Cadenas de ejemplo: 'abc', 'xyz'
#Resultado Esperado: 'xyc abz'

cadena1='aeiuo'
cadena2='abcde'

aux1= cadena1[:2]
aux2= cadena2[:2]

aux3= cadena1[2:]
aux4= cadena2[2:]

print(cadena1,cadena2)
print(aux2+aux3+' '+aux1+aux4)



