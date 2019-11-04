#36. Escriba un programa Python para comprobar si una cadena contiene todas las letras del alfabeto. 

palabra = "wertyuiopñlkjhgfdssazxcvbnbnm"
cadena= palabra.lower()

abc = "abcdefghijklmnñopqrstuvwxyz"

for x in abc:
    if not x in palabra:
        print("Falta la letra",x,"en la cadena.")
    else:
        print("Esta la letra",x,"en la cadena.")




