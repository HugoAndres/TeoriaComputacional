#20. Escriba un programa de Python para crear un cifrado de C�sar.
#Nota: En criptograf�a, una cifra de C�sar, tambi�n conocida como la cifra de C�sar, la cifra de cambio, el c�digo de C�sar o el cambio de C�sar, es una de las t�cnicas de cifrado m�s sencillas y conocidas. Es un tipo de cifrado de sustituci�n en el que cada letra en el texto plano se sustituye por una letra de un n�mero fijo de posiciones por el alfabeto. Por ejemplo, con un desplazamiento a la izquierda de 3, D ser�a reemplazado por A, E se convertir�a en B, y as� sucesivamente. El m�todo lleva el nombre de Julio C�sar, que lo utiliz� en su correspondencia privada.


abecedario = 'abcdefghijklmnñopqrstuvwxyz'

def cifrado_cesar(cadena,clave):
    t_cifrado= ''
    for letra in cadena:
        suma = abecedario.find(letra)+clave
        modulo =int(suma)%len(abecedario)
        t_cifrado= t_cifrado+str(abecedario[modulo])
    return t_cifrado


palabra = "Teoriacomputacional"
cadena = palabra.lower()
clave = 2
print(abecedario)
print(clave)
print("cadena:" ,palabra)
print("cifrado: ",cifrado_cesar(cadena,clave))
