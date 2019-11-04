#15. Escriba una funci�n Python para obtener la primera mitad de una cadena especificada de longitud par.
#Funci�n y resultado de la muestra:
#String_first_half ('Python') -> Pyt

def String_first_halt(cadena):
    tamaño = len(cadena)
    print("La cadena es:",cadena)
    par = tamaño%2
    if par != 0:
        print("No es de longitud par")
    else:
        subcadena = cadena[:len(cadena)//2]
        print(subcadena)

palabra = 'teoria'
String_first_halt(palabra)
