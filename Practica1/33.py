#33. Escriba un programa de Python para quitar un conjunto de caracteres de una cadena. 
#Ejemplo:
#quitar_caracteres("institucional","aeiou") -> 'nsttcnl'

def elimina_caracteres(cadena,caracter):
    s_sin_vocales = ""
    for letra in cadena:
        if letra not in caracter:
            s_sin_vocales += letra
    print(s_sin_vocales)
    return s_sin_vocales



palabra = "institucional"
caracter="aeiou"
print(palabra)
print("caracteres a eliminar: ",caracter)
elimina_caracteres(palabra,caracter)
