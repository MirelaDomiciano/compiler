#import da biblioteca ply para a construção dos tokens
import ply.lex as lex

#lista de tokens
tokens = [
    'TIPO_INT', 'TIPO_FLOAT', 'TIPO_CHAR',
    'ATRIBUICAO', 'COLON',
    'SOMA', 'SUBTRACAO', 'MULTIPLICACAO', 'DIVISAO', 'RESTO',
    'PONTO', 'PONTO_VIRGULA', 'VIRGULA',
    'E', 'OU', 'NEGACAO',
    'IGUAL', 'MAIOR_IGUAL', 'MENOR_IGUAL', 'MAIOR', 'MENOR', 'DIFERENTE',
    'ABRE_PARENTESES', 'FECHA_PARENTESES',
    'INICIO', 'FIM', 'ENTRADA', 'SAIDA', 'COND_IF', 'COND_ELSE', 'REP_DURING', 'REP_THROUGH', 'BLOCO_DE_COMANDO'
]

#expressões regulares para tokens simples
t_ATRIBUICAO = r'='
t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_RESTO = r'%'
t_E = r'and'
t_OU = r'or'
t_NEGACAO = r'not'
t_IGUAL = r'=='
t_MAIOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_MAIOR = r'>'
t_MENOR = r'<'
t_DIFERENTE = r'!='
t_ABRE_PARENTESES = r'\('
t_FECHA_PARENTESES = r'\)'
t_VIRGULA = r','

#palavras reservadas
reserved = {
    'init': 'INIT',
    'pinguim': 'END',
    'pin': 'PIN',
    'pout': 'POUT',
    'pif': 'PIF',
    'paf': 'PAF',
    'phile': 'PHILE',
    'pegin': 'PEGIN',
    'pend': 'PEND'
}

#tokens com regras mais complexas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_REAL(t):
    r'[-]?[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'[-]?[0-9]+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)
    return t

#ignorar espaços e tabulações (não são tokens)
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