#21. Escriba un programa Python para agregar un prefijo a todas las l�neas de una cadena multil�nea.

prefijo = "sobre"
texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"\


listaPalabras = texto.split()

for w in listaPalabras:
    print(prefijo+w)
