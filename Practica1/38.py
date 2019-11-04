#38. Escriba un programa Python para poner en min�sculas los primeros n caracteres de una cadena. 

cadena= "COMPUTACIONAL"
n =5
tamaño=len(cadena)
cademinusculas = cadena[0:n].lower()+cadena[n:tamaño]
print(cademinusculas)

