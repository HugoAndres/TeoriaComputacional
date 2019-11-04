#4. Escriba un programa de Python para obtener una cadena de una cadena dada, donde todas las apariciones de su primer car�cter se han cambiado a '$', excepto el propio primer car�cter.
#Cadena de ejemplo: 'regresar'
#Resultado esperado: 'reg$esa$'

cadena = 'regresar'

caracter = cadena[:1]
sobra = cadena[1:]
print(cadena)
print(caracter)
for n in sobra:
    if caracter == n:
        print("$")
    else:
        print(n)
        
