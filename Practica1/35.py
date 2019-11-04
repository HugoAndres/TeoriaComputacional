#35. Escriba un programa Python para imprimir el �ndice del car�cter en una cadena.
#Cadena de ejemplo: w3resource
#Resultado esperado:
#Car�cter actual w posici�n 0
#Car�cter actual 3 posici�n 1
#Car�cter actual r posici�n 2
#...


cadena = "w3resource"
print(cadena)
tamaño = len(cadena)
for x in range(0,tamaño):
    print("carácter actual",cadena[x],"posición",x)

