#16. Escriba una funci�n Python para invertir una cadena si su longitud es un m�ltiplo de la suma de los tres �ltimos d�gitos de su No. de Boleta.

def funcion(cadena,digitos):
    boleta = list(digitos)
    
    for i in range(0,len(boleta)):
        boleta[i]=int(boleta[i])
    print (boleta)
    posicion=len(boleta)
    suma = boleta[posicion-1] +boleta[posicion-2]+boleta[posicion-3]
    longitud = len(cadena)
    if longitud%suma==0:
        invertir = cadena[::-1]
        print(invertir)
    else:
        print(suma," no es multiplo de ",longitud)

boleta = "2014020813"
palabra= "jdhfgrythusjdlruthbdhgfu"
print(palabra)
funcion(palabra,boleta)



