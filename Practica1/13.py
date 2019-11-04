#13. Escriba una funci�n Python para obtener una cadena de 4 copias de los dos �ltimos caracteres de una cadena especificada (la longitud debe ser al menos 2).
#Funci�n y resultado de la muestra:
#Insert_end ('Python') -> onononon
#Insert_end ('Ejercicio') -> ioioioio

def Insert_end(cadena):
    tamaño = len(cadena)
    if tamaño > 2:
        caracteres = cadena[tamaño -2:]
        print(caracteres *4)
    else:
        print("La cadena es menor de 2 caracteres")

cadena = "ESCOM"
print("La cadena es:",cadena)
Insert_end(cadena)
