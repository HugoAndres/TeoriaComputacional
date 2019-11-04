#28. Escriba un programa de Python para formatear un n�mero con formato de porcentaje. 

numero =1/3
if numero>1:
    fraccion=numero/100
    print(numero)
    print ("{:.0%}".format(fraccion))
else:
    print(numero)
    print ("{:.0%}".format(numero))

