#32. Escriba un programa de Python para invertir palabras en una cadena. 

def invertir(frase):
    return ' '.join(list(map(lambda x: x[::-1], frase.split())))

print(invertir("hola como estas"))
