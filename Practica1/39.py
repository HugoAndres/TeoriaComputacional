#39. Escriba un programa de Python para intercambiar coma y punto en una cadena. 
#Cadena de ejemplo: "32.054,23"
#Resultado esperado: "32,054.23"

cadena="32.054,23"
print(cadena)
for x in cadena:
    if x == '.':
        x= x.replace(x,",")
        print(x)
    elif x == ',':
        x= x.replace(x,".")
        print(x)
    else:
        print(x)








