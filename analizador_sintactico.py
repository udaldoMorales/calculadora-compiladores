import ply.yacc as yacc
from analizador_lexico import tokens
from analizador_lexico import lexer

# resultado del analisis
resultado_gramatica = []
steps = []

def p_expression_plus(p):
	'expression : expression PLUS term'
	p[0] = p[1] + p[3]
	steps.append('Suma: ' + str(p[1]) + ' + ' + str(p[3]) + ' = ' + str(p[0]))

def p_expression_SUBSTRACTION(p):
	'expression : expression SUBSTRACTION term'
	p[0] = p[1] - p[3]
	steps.append('Resta: ' + str(p[1]) + ' - ' + str(p[3]) + ' = ' + str(p[0]))

def p_expression_term(p):
	'expression : term'
	p[0] = p[1]
	#steps.append('Asignación (E = T): ' + str(p[0]) + ' = ' + str(p[1]))

def p_term_MULTIPLICATION(p):
	'term : term MULTIPLICATION factor'
	p[0] = p[1] * p[3]
	steps.append('Multiplicación: ' + str(p[1]) + ' * ' + str(p[3]) + ' = ' + str(p[0]))

def p_term_division(p):
	'term : term DIVISON factor'
	p[0] = p[1] / p[3]
	steps.append('Division: '  + str(p[1]) + ' / ' + str(p[3]) + ' = ' + str(p[0]))

def p_term_factor(p):
	'term : factor'
	p[0] = p[1]
	#steps.append('Asignación (T = F): ' + str(p[0]) + ' = ' + str(p[1]))


def p_factor_int(p):
	'factor : INTEGER'
	p[0] = p[1]
	#steps.append('Asignación (F = int): ' + str(p[0]) + ' = ' + str(p[1]))

def p_factor_dec(p):
	'factor : DECIMAL'
	p[0] = p[1]
	#steps.append('Asignación (F = dec): ' + str(p[0]) + ' = ' + str(p[1]))

def p_factor_expr(p):
	'factor : OPARENTHESIS expression CPARENTHESIS'
	p[0] = p[2]
	#steps.append('Asignación (F = (E)): ' + str(p[0]) + ' = ' + str(p[2]))

def p_factor_brack_expr(p):
	'factor : OBRACKETS expression CBRACKETS'
	p[0] = p[2]
	#steps.append('Asignación (F = [E]): ' + str(p[0]) + ' = ' + str(p[2]))


def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sintactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    result = parser.parse(data)

    resultado_gramatica.append(str("The steps are:"))
    for i in steps:
        resultado_gramatica.append(str(i))

    if (result is None):
        resultado_gramatica.append(str("\nThe result it is not longer computable"))
    else:
        resultado_gramatica.append(str("\nThe result of the operation is: "))
        resultado_gramatica.append(str(result))

    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s: continue

        prueba_sintactica(s)
