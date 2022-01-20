tokens = ('a','b','c')    
t_a =r'a'  
t_b=r'b'
t_c=r'c'

def t_error(t):
    print("Caracter ilegal ",t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()

def p_S(p):
    '''S : a A
         | b B
         | c S
         | empty'''
    pass

def p_A(p):
    '''A : a S
         | b C
         | c A
         | empty'''
    pass

def p_B(p):
    '''B : b B
         | a A
         | empty'''
    pass

def p_C(p):
    '''C : b C
         | a S
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
