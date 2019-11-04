#17. Escriba una funci�n Python para convertir una cadena dada en may�sculas si contiene al menos 2 caracteres en may�sculas en los primeros 4 caracteres.



def funcion(cadena):
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnñopqrstuvwxyz"
    contador = 0
    for i in range(0,4):
        for n in range(0,len(mayusculas)):
            if cadena[i]==mayusculas[n]:   
                   contador +=1
    if contador>=2:
        print(cadena.upper())
    else:
        print("La cadena tiene solo una mayuscula en los primeros 4 caracteres.")
        

cadena = "HuGoAndres"
print("La cadena es:",cadena)
funcion(cadena)
           


