#19. Escriba un programa de Python para comprobar si una cadena comienza con caracteres especificados.

cadena = "TeoriaComputacional"
caracter = "e"
print(cadena)
if caracter in cadena[0]:
    print ("La cadena empieza con ",caracter)
else:
    print ("La cadena NO empieza con" ,caracter)
