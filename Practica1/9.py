#9. Escriba un programa de Python para eliminar los caracteres que tienen valores de �ndice impar de una cadena dada.

cadena = "teoria"
lista = list(cadena)
posicion = []
impar = 0
print("La cadena: ",cadena)
for n in lista:
    if impar % 2 == 0:
        posicion.append(n)
    impar+=1
print("Eliminando impares:" ,''.join(posicion))
