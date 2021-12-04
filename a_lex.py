import ply.lex as lex
import re

tokens = [
    'PLUS', 'SUBSTRACTION', 'MULTIPLICATION', 'DIVISON',
    'OPARENTHESIS', 'CPARENTHESIS', 'OBRACKETS', 'CBRACKETS',
    'FPROGRAM', 'FINSTRUCTION', 'INTEGER', 'DECIMAL'
    ]
    
t_ignore = ' \t'
t_PLUS = r'\+'
t_SUBSTRACTION = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISON = r'\/'
t_OPARENTHESIS = r'\('
t_CPARENTHESIS = r'\)'
t_OBRACKETS = r'\['
t_CBRACKETS = r'\]'
t_FPROGRAM = r'\$'
t_FINSTRUCTION = r'\\r'

def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

def t_DECIMAL( t ):
    r'\d+\.\d+'
    t.value = float( t.value )
    return t

def t_INTEGER( t ):
    r'\d+'
    t.value = int( t.value )
    return t

def t_error( t ):
    print("Ilegal caracter '%s'" % t.value[0])
    t.lexer.skip(1)
