import ply.lex as lex

# Lista de tokens
tokens = [
    'INT',
    'FLOAT',
    'CHAR',
    'ATRIBUICAO',
    'PONTO_VIRGULA',
    'ABRE_PARENTESES',
    'FECHA_PARENTESES',
    'SOMA',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'MENOR',
    'MAIOR',
    'IGUAL',
    'DIFERENTE',
    'MENOR_IGUAL',
    'MAIOR_IGUAL',
    'E',
    'OU',
    'NEGACAO',
    'VIRGULA',
    'RESTO',
    'VARIAVEL'
]

# Definição de tokens para palavras reservadas
reserved = {
    'startProgram': 'INICIO_PROGRAMA',
    'endProgram': 'FIM_PROGRAMA',
    'start': 'INICIO',
    'end': 'FIM',
    'in': 'ENTRADA',
    'out': 'SAIDA',
    'if': 'COND_IF',
    'else': 'COND_ELSE',
    'during': 'REP_DURING',
    'through': 'REP_THROUGH',
    'int': 'TIPO_INT',
    'float': 'TIPO_FLOAT',
    'char': 'TIPO_CHAR'
}

tokens = tokens + list(reserved.values())

# Expressões regulares para tokens simples
t_ATRIBUICAO = r'->'
t_PONTO_VIRGULA = r';'
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_MENOR = r'<'
t_MAIOR = r'>'
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
t_E = r'&&'
t_OU = r'\|\|'
t_NEGACAO = r'!'
t_VIRGULA = r','
t_RESTO = r'%'

# Expressões regulares com ações
def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CHAR(t):
    r'\'[a-zA-Z]\''
    t.value = t.value[1]
    return t

def t_VARIAVEL(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'VARIAVEL')
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

def tokenize_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    lexer.input(data)
    tokens = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens

# Testar a tokenização diretamente no arquivo lexer.py (opcional)
if __name__ == "__main__":
    # Substitua 'arquivo_de_teste.pin' pelo caminho do arquivo que deseja testar
    tokens = tokenize_file('exemplo.txt')
    for token in tokens:
        print(token)