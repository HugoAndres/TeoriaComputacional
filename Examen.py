from itertools import chain,combinations

def powerset(iterable):
    s=list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))
Q=['q0','q1']
Qprima=list(powerset(Q))

print(Qprima)

s='q0'
F=['q1']
Sigma=['a','b']

DELTA={('q0','a'):['q0','q1'],
       ('q0','b'):['q1'],
       ('q1','b'):['q0','q1']
       }

sprima=(s,)

Sigmaprima=Sigma

print("Qprima",Qprima)
print("")

Fprima=[]
for X in Qprima:
    print(X)
    for q in X:
        print(q)
        if q in F:
            Fprima.append(X)
            break

delta={}

for X in Qprima:
    for sigma in Sigmaprima:
        estados_siguientes=[]
        for q in X:
            estados_q_s= DELTA[(q,s)]
            for m in estados_q_s:
                if not (m in estados_siguientes):
                    estados_siguientes.append(m)
                    estados_siguientes.sort()
                    delta[(X,s)]=tuple(estados_siguientes)

def transicion(X,s):
    global delta, Sigmaprima
    if not (s in Sigmaprima):
        print(s,"no está en el alfabeto")
        return False, ''
    estados_siguientes=delta[(X,s)]
    return True,estados_siguientes

w=['aaab','','b','ba']
for c in w:
    estado=sprima
    for l in c:
        Y,estado=transicion(estado,l)
        if Y==True and (estado in Fprima):
            print (c,"So está en el lenguaje")
        else:
            print(c,"no está en el lenguaje")