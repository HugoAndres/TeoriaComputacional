#12. Escriba un programa de Python que acepte una secuencia de palabras separada por comas como entrada e imprima las palabras en forma ordenada (alfanum�ricamente).


palabras = ['hola','como','estas','yo','muy','bien']
print("Palabras: ",palabras)
palabras.sort(key = str)
print("Ordenadas: ",palabras)
