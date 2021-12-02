import codecs
import os
import sys

from a_lex import *
from a_sintac import *
from tabulate import tabulate

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


print ('\nThis is the entry: %s\n'%chain)

lexer = lex.lex()

lexer.input( chain )


tipo = []
valor = []
linea = []
posicion = []
matriz = []
i = 0
while True:
    tok = lexer.token()
    if not tok: 
        break 
    tipo.append(tok.type)
    valor.append(tok.value)
    linea.append(tok.lineno)
    posicion.append(tok.lexpos)
    matriz.append([tipo[i],valor[i],linea[i],posicion[i]])
    i = i+1

print(tabulate(matriz, headers=["Token","Valor","Linea","Posición"], showindex="always", tablefmt="grid", colalign=("center","center")))

# Build the parser
parser = yacc.yacc()

result = parser.parse(chain)

print('\nThe steps are: ')
for i in steps:
    print(i)

if (result is None):
    print("The result it is not longer computable")
else:
    print('\nThe result of the operation is: %s'%result)


