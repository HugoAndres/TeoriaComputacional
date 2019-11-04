#10. Escriba un programa de Python para contar las ocurrencias de cada palabra en una oraci�n determinada.

cadenaPalabras = "hugo hugo hugo hugo teoria hugo teoria computacional"

listaPalabras = cadenaPalabras.split()
frecuenciaPalab = []

for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
for n in range(0,len(listaPalabras)):
        print(listaPalabras[n], "|" ,frecuenciaPalab[n])
