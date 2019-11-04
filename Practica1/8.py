#8. Escriba un programa de Python para cambiar una cadena dada a una nueva cadena donde se intercambiaron los caracteres primero y �ltimo.

cadena = "TEORIA"
tamaño = len(cadena)
primero = cadena[0]
ultimo = cadena[tamaño-1]
nuevacadena = cadena[1:len(cadena)-1]

print(ultimo+nuevacadena+primero)
