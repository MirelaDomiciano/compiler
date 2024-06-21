# import da biblioteca ply para a construção dos tokens
import ply.lex as lex

# Tokens fornecidos
tokens = [
    'TIPO_INT', 'TIPO_FLOAT', 'TIPO_CHAR',
    'VARIAVEL',
    'ATRIBUICAO', 'COLON',
    'SOMA', 'MAISMAIS', 'SUBTRACAO', 'MENOSMENOS', 'MULTIPLICACAO', 'DIVISAO', 'RESTO',
    'PONTO', 'PONTO_VIRGULA', 'VIRGULA',
    'E', 'OU', 'NEGACAO',
    'IGUAL', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'MAIOR', 'MENOR', 'DIFERENTE',
    'ABRE_PARENTESES', 'FECHA_PARENTESES',
    'INICIO', 'FIM',
    'ENTRADA', 'SAIDA',
    'COND_IF', 'COND_ELSE', 'REP_DURING', 'REP_THROUGH',
    'BLOCO_DE_COMANDO'
]

# Expressões regulares para tokens simples
t_ATRIBUICAO = r'<-'
t_SOMA = r'\+'
t_MAISMAIS = r'\+\+' 
t_SUBTRACAO = r'-'
t_MENOSMENOS = r'--' 
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_RESTO = r'%'
t_E = r'&'
t_OU = r'\|'
t_NEGACAO = r'\#'
t_IGUAL = r'\='
t_MAIOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_MAIOR = r'>'
t_MENOR = r'<'
t_DIFERENTE = r'\#='
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_VIRGULA = r','


#palavras reservadas
reserved = {
    'int': 'TIPO_INT',
    'float': 'TIPO_FLOAT',
    'char': 'TIPO_CHAR',
    'in': 'INICIO',
    'out': 'FIM',
    'if': 'COND_IF',
    'else': 'COND_ELSE',
    'through': 'REP_THROUGH',
    'during': 'REP_DURING',
    'start': 'INICIO',
    'end': 'FIM'
}

#tokens com regras mais complexas
def t_VARIAVEL(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'VARIAVEL')
    return t

def t_FLOAT(t):
    r'[-]?[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

def t_CHAR(t):
    r"\"([^\\'\n]|(\\.)|())\""
    t.value = t.value[1:-1]
    return t



#ignorar espaços e tabulações
t_ignore = ' \t'

#definir comportamento para novas linhas (incrementar o número da linha)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#tratar erros de caracteres ilegais
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

#construir o lexer
lexer = lex.lex()

#função para ler arquivo e tokenizar, imprimindo tokens no terminal
def tokenize_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)