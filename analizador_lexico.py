import ply.lex as lex
import re
import codecs
import os
import sys
from tabulate import tabulate


# resultado del analisis
resultado_lexema = []

tokens = [
    'PLUS', 'SUBSTRACTION', 'MULTIPLICATION', 'DIVISON',
    'OPARENTHESIS', 'CPARENTHESIS', 'OBRACKETS', 'CBRACKETS',
    'FPROGRAM', 'FINSTRUCTION', 'INTEGER', 'DECIMAL'
    ]

# Reglas de Expresiones Regualres para token de Contexto simple

t_ignore = r' '
t_PLUS = r'\+'
t_SUBSTRACTION = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISON = r'\/'
t_OPARENTHESIS = r'\('
t_CPARENTHESIS = r'\)'
t_OBRACKETS = r'\['
t_CBRACKETS = r'\]'
t_FPROGRAM = r'\$'
t_FINSTRUCTION = r'\;'

def t_newline( t ):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_DECIMAL( t ):
    r'\d+\.\d+'
    t.value = float( t.value )
    return t

#reconocer un numero entero de 2 o mas digitos
def t_INTEGER( t ):
    r'\d+'
    t.value = int( t.value )
    return t


def t_error( t ):
    print("Ilegal caracter '%s'" % t.value[0])
    t.lexer.skip(1)

# Prueba de ingreso
def prueba(data):
    global resultado_lexema

    lexer = lex.lex()

    lexer.input(data)

    resultado_lexema.clear()
    
    while True:
        token = lexer.token()
        if not token:
            break
        estado = "Linea {:4} Token {:16} Valor {:16} Posicion {:4}".format(str(token.lineno),str(token.type) ,str(token.value), str(token.lexpos) )
        resultado_lexema.append(estado)
    
    return resultado_lexema

 # instanciamos el analizador lexico
lexer = lex.lex()

if __name__ == '__main__':
    while True:
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)