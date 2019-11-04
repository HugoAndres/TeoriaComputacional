#7. Escriba un programa de Python para quitar el car�cter de una posici�n dada de una cadena no vac�a.


#Si la cadena es vacia poner: ""
cadena = "ESCOM"
n = 3
tamaño = len(cadena)

if tamaño == 0:
    print("La cadena es vacia,no es posible eliminar")
else:
    cadena2= cadena[n:]
    cadena1= cadena[:n-1]
    print(cadena1+cadena2)
