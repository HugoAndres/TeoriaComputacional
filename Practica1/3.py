#3. Escriba un programa de Python para obtener una cadena hecha de los 2 primeros y los 2 �ltimos caracteres de una determinada cadena. Si la longitud de cadena es menor que 2, devuelve la cadena vac�a.
#Cadena de ejemplo: 'w3resource'
#Resultado Esperado: 'w3ce'
#Cadena de ejemplo: 'w3'
#Resultado Esperado: 'w3w3'
#Cadena de ejemplo: 'w'
#Resultado esperado: '' (Cadena vac�a)


cadena= 'teoria computacional'
if len(cadena)>=2:
    print("cadena:",cadena)
    print(cadena[:2])
    print(cadena[-2:])
else:
    print("cadena vacia")




