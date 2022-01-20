from itertools import chain, combinations

def conjunto_potencia(iterable):
  s = list(iterable)
  return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

Q=['q0','q1','q2','q3','q4','q5']
s='q0'
F=['q3','q5']
Sigma=['a','b']
DELTA = {('q0','a'): ['q0','q1'],
        ('q0','b'): ['q0','q4'],
        ('q1','a'): ['q2'],
        ('q2','a'): ['q2'],
        ('q2','b'): ['q2'],
        ('q2','c'): ['q3'],
        ('q4','b'): ['q5'],
        ('q5','a'): ['q5'],
        ('q5','b'): ['q5'],
        }

print("Sigma:\n",Sigma)
print("\n")

Sprima=(s,)
print("Sprima:\n",Sprima)
print("\n")

Qprima=list(conjunto_potencia(Q))
print("Qprima:\n",Qprima)
print("\n")

Sigmaprima=Sigma

###print("Construyendo Fprima")
Fprima=[]
for x in Qprima:
   ### print(x)
    for q in x: 
     ###print(q)
     if q in F:
      Fprima.append(x)
      break
print("Fprima:\n",Fprima)
print("\n")

delta = { }
for X in Qprima:
    for s in Sigmaprima:
        estados_siguientes=[]
        for q in X:
            estados_q_s = DELTA[(q,s)]
            for qaux in estados_q_s:
                if not (qaux in estados_siguientes):
                    estados_siguientes.append(qaux)
        estados_siguientes.sort()
        delta[(X,s)]=tuple(estados_siguientes)

print("DELTA:\n",delta)

print("\n PRUEBAS DE CODIGO.")
def transicion(X,s):
    global delta, Sigmaprima
    if not (s in Sigmaprima):
       ### print(s,"no está en el alfabeto")
        return False, ''
    estados_siguientes=delta[(X,s)]
    return True,estados_siguientes

w=['a',' ','b','aaaac','c','aabc']
for c in w:
    estado=Sprima
    for l in c:
        Y,estado=transicion(estado,l)
    if Y==True and (estado in Fprima):
         print(c,"--->Si está en el lenguaje")
    else:
         print(c,"--->No está en el lenguaje")
