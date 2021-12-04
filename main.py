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

inParts = chain.split('\n')

for iteration in range(0, len(inParts)):

    lexer = lex.lex()

    lexer.input( chain )
    #lexer.input( inParts[iteration] )

    tipo,valor,linea,posicion, matriz = [] ,[],[],[],[]
    i = 0

    while chain:
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
print('\n')

# Build the parser
startIndex, endIndex, temp = 0, 0, 0
for iteration2 in range(0, len(inParts)):
    parser = yacc.yacc()

    print('\nParsing for %s'%inParts[iteration2])

    result = parser.parse(inParts[iteration2].strip())
 
    endIndex = len(steps)
    startIndex = temp

    print('\nThe steps are ')
    for i in range(startIndex, endIndex):
        print(steps[i])

    temp = endIndex

    if (result is None):
        print("The result it is not longer computable")
    else:
        print('\nThe result of the operation is: %s\n'%result)

    parser = None

    #print('Steps at end')
    #print (steps)
