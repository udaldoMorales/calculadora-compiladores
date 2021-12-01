import ply.yacc as yacc
 
from a_lex import tokens

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

# Error rule for syntax errors
def p_error(p):
	print("\nSyntax error in input! %s"%(str(p.type)))
 
