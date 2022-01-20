Q=['q0', 'q1', 'q2']
Sigma=['a','b']
F=['q0','q1']
s='q0'
delta = { ('q0','b'):'q0',
	  ('q0','a'):'q1',
	  ('q1','b'):'q0',
	  ('q1','a'):'q2',
	  ('q2','a'):'q2',
	  ('q2','b'):'q2' }

print(Q,Sigma,F,s,delta)

w=['b','aaaab','ab','ba','aba','bb','aaaaaaaaaaaa','']

def transicion(estado, sigma):
	global Sigma,delta

	STATUS=True
	if sigma not in Sigma:
	   STATUS=False
	   return '',STATUS

	if (estado,sigma) not in delta.keys():
	   STATUS=False
	   return '',STATUS

	estado_siguiente= delta[(estado, sigma)]
	print("Transición (", estado,",",sigma,") ->",estado_siguiente)
	return estado_siguiente,STATUS
	
#transicion(s,'a')

for cadena in w:
    estado = s
    for c in cadena:
        estado,STATUS=transicion(estado,c)
        if not STATUS:
           break
    if STATUS and estado in F: 
       print(cadena,"si está en el lenguaje")
    else:
       print(cadena,"no está en el lenguaje")



