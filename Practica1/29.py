#29. Escriba un programa de Python para mostrar un n�mero en alineaci�n izquierda, derecha y central alineados en ancho 10. 
#Ejemplo:
#Original:  22                              
#Izq (ancho 10)  :22                     
#Der (ancho 10)  :        22             
#Cen (ancho 10)  :    22


numero = "33"
ancho = 10
print("Original: ",numero)
print("Izquierda: ",numero.ljust(ancho," "))
print("Derecha: ", numero.rjust(ancho," "))
print ("Central: ",numero.center(ancho, " ")) 
