import ply.lex as lex
import re
import codecs
import os
import sys

tokens = [
    'PLUS', 'SUBSTRACTION', 'MULTIPLICATION', 'DIVISON',
    'OPARENTHESIS', 'CPARENTHESIS', 'OBRACKETS', 'CBRACKETS',
    'FPROGRAM', 'FINSTRUCTION', 'INTEGER', 'DECIMAL'
    ]

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

def t_DECIMAL( t ):
    r'\d+\.\d+'
    t.value = float( t.value )
    return t

def t_INTEGER( t ):
    r'\d'
    t.value = int( t.value )
    return t

def t_error( t ):
    print("Ilegal caracter '%s'" % t.value[0])
    t.lexer.skip(1)

def searchFiles( c_directory ):
    current_files = []
    selectedFile = ''
    response = False
    cont = 1

    for base, dirs, files in os.walk( c_directory ):
        current_files.append( files )
    
    for c_file in files:
        print( str( cont ) +  ". " + c_file)
        cont += 1

    while not response:
        selectedFile = input('\nSelect your test: ')
        for c_file in files:
            if c_file == files[int( selectedFile ) - 1]:
                response = True
                break

    print("You are did selected the test \'%s' \n" % files[int( selectedFile ) - 1])
    return files[int( selectedFile ) - 1]

directory = os.getcwd() + '/test'
m_file = searchFiles( directory )
test = directory + '/' + m_file
print(test)
fp = codecs.open( test, "r", "utf-8")
chain = fp.read()
fp.close()

lexer = lex.lex()

lexer.input( chain )

while True:
    token = lexer.token()
    if not token : break
    print( token )
