#40. Escriba un programa Python para contar las vocales de un texto dado. 
cadena1="Escriba un programa Python para contar las vocales de un texto dado."
cadena = cadena1.lower()
vocal = "aeiou"
print("texto: ",cadena)
print("numero de vocales:")
for x in vocal:
    ocurrencias = cadena.count(x)
    print(x,ocurrencias)

