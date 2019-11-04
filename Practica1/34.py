#34. Escriba el programa de Python para contar los caracteres repetidos en una cadena. 
#Cadena de ejemplo: 'thequickbrownfoxjumpsoverthelazydog'
#Resultado esperado :
#o 4
#e 3
#u 2
#h 2
#r 2
#t 2

cadena="thequickbrownfoxjumpsoverthelazydog"
abc = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
print(cadena)
print("numero de ocurrencias: \n")
for x in abc:
    ocurrencias = cadena.count(x)
    if ocurrencias >1:
        print(x,ocurrencias)
