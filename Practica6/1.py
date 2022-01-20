tokens = ('a','b')    
t_a =r'a'  
t_b=r'b'

def t_error(t):
    print("Caracter ilegal ",t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_S(p):
    '''S : b A
         | a C'''
    pass

def p_A(p):
    '''A : b S
         | a B'''
    pass

def p_B(p):
    '''B : a A
         | b C'''
    pass

def p_C(p):
    '''C : a S
         | b B
         | empty'''
    pass

def p_empty(p):
    'empty :'
    pass

s= ''

def p_error(p):
    global s
    if p:
        print("Error de sintaxis en ",p.value)
        print(s,"no esta en el lenguaje")
    else:
        print("Error de sintaxis en EOF")
        print(s,"no esta en el lenguaje")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s =  input('> ')
    except EOFError:
        break
    if not s: 
        continue
    t = yacc.parse(s)
