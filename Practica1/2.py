#2. Escriba un programa de Python para contar el n�mero de caracteres (frecuencia de caracteres) en una cadena.
#Cadena de ejemplo: �google.com '
#Resultado previsto: {'o': 3, 'g': 2, '': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

from collections import Counter

p = "google.com"
Counter(p)
print(p)
print("\n",Counter(p))
