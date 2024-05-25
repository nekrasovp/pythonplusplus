import ply.yacc as yacc
from pythonplusplus.lexer import tokens

# Precedence rules for the arithmetic operators
precedence = (
    ('left', 'PLUS'),
    ('left', 'INCREMENT'),
    ('left', 'EQUALS'),
)

def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
    | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]

def p_expression_assign(p):
    'expression : NAME EQUALS expression'
    p[0] = ('=', p[1], p[3])

def p_expression_increment(p):
    'expression : NAME INCREMENT'
    p[0] = ('+=', p[1], 1)

def p_expression_binop(p):
    '''expression : expression PLUS expression'''
    p[0] = ('+', p[1], p[3])

def p_expression_name(p):
    'expression : NAME'
    p[0] = p[1]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()