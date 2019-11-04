#14. Escriba una funci�n de Python para obtener una cadena hecha de los primeros tres caracteres de una cadena especificada. Si la longitud de la cadena es menor que 3, devuelva la cadena original.
#Funci�n y resultado de la muestra:
#First_three ('ipy') -> ipy
#First_three ('python') -> pyt

def First_three(cadena):
    tamaño=len(cadena)
    print("La cadena es:",cadena)
    if tamaño < 3:
        print("La cadena es menor de 3 caracteres: ", cadena)
    else:
        caracteres = cadena[:3]
        print(caracteres)

cadena = "to"
First_three(cadena)


