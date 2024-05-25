import ply.lex as lex

# List of token names
tokens = (
    'INCREMENT',
    'NAME',
    'NUMBER',
    'PLUS',
    'EQUALS',
    'NEWLINE'
)

# Regular expression rules for simple tokens
t_INCREMENT = r'\+\+'
t_PLUS = r'\+'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Ignore spaces and tabs
t_ignore = ' \t'

# Define a rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule for newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
