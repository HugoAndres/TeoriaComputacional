#30. Escriba un programa en Python que coloque tres n�meros en el rango (0,256) en una cadena hexadecimal que inicie con '#' (Formato RGB de Python TkInter).
#Ejemplo: 
#(64, 204, 208) -> '#40ccd0'


n1=64
n2=204
n3=208

c1 = hex(n1).split('x')[-1]
c2 = hex(n2).split('x')[-1]
c3 = hex(n3).split('x')[-1]
print("("+str(n1)+","+str(n2)+","+str(n3)+")")
print("#"+c1+c2+c3)






