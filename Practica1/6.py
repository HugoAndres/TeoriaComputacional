#6. Escribe una funci�n de Python que tome una lista de palabras y devuelva la longitud de la m�s larga.

def funcion(lista):
    cadena=lista[0]
    tamaño=len(lista[0])
    for palabra in lista:
        if tamaño <=len(palabra):
            cadena = palabra
            tamaño = len(palabra)
        else:
            cadena = cadena
    print("La cadena mas larga es:",cadena,len(cadena))

lista = ["hola","ESCOM","teoria","computacional","aaaaaaaaaaaaa"]
print(lista)
funcion(lista)
    

