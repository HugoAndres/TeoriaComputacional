z='A'
F=['q4']
s='q1'
delta={ ('q1','a','A'):('q2','BA'),
        ('q1','','A'):('q4',''),
        ('q2','a','B'):('q2','BB'),
        ('q2','b','B'):('q3',''),
        ('q3','b','B'):('q3',''),
        ('q3','','A'):('q4','A')
       }

pila=[z]

def transicion(estado,sigma,gamma):
    global delta,pila
    if(estado,sigma,gamma) not in delta.keys():
        print("Error")
        exit(0)
    t=delta[(estado,sigma,gamma)]
    print((estado,sigma,gamma),"->",t)
    for g in t[1][::-1]:
        pila.append(g)
    print("pila:",pila[::-1])
    return t[0]

def procesaCadena (w):
    print("-------------------------------\n")
    global s,pila
    estado=s
    pila=[z]
    for sigma in w:
        gamma=pila.pop()
        estado = transicion(estado,sigma,gamma)
    gamma=pila.pop()
    if (estado,'', gamma) in delta.keys():
        t=delta[(estado,'',gamma)]
        print((estado,'', gamma),"->",t)
        estado=t[0]
        for g in t[1][::-1]:
            pila.append(g)
        print("pila:",pila[::-1])
    if estado in F:
        print(w, "pertence al lenguaje")
    else:
        print(w, "no pertenece al lenguaje")


cadenas =['a','ab','aaabbb','aaaabb','']
for w in cadenas:
    procesaCadena(w)
