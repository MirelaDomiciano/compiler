import ply.yacc as yacc
from lexer import tokens
import os

# Regras gramaticais

def p_program(p):
    '''program : INICIO statement_list FIM'''
    p[0] = ('program', p[2])

def p_type_specifier(p):
    '''type_specifier : TIPO_INT
                      | TIPO_FLOAT
                      | TIPO_CHAR'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : assignment
                 | input
                 | output
                 | if_statement
                 | while_statement
                 | for_statement
                 | declaration'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : VARIAVEL ATRIBUICAO expression PONTO_VIRGULA'''
    p[0] = ('assign', p[1], p[3])

def p_input(p):
    '''input : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES PONTO_VIRGULA'''
    p[0] = ('input', p[3])

def p_output(p):
    '''output : SAIDA ABRE_PARENTESES output_list FECHA_PARENTESES PONTO_VIRGULA'''
    p[0] = ('output', p[3])

def p_output_list(p):
    '''output_list : expression
                   | output_list VIRGULA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_expression(p):
    '''expression : term
                  | expression SOMA term
                  | expression SUBTRACAO term
                  | expression MENOR term
                  | expression MAIOR term
                  | expression IGUAL term
                  | expression DIFERENTE term
                  | expression MENOR_IGUAL term
                  | expression MAIOR_IGUAL term
                  | expression E term
                  | expression OU term'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('binop', p[2], p[1], p[3])

def p_term(p):
    '''term : factor
            | term MULTIPLICACAO factor
            | term DIVISAO factor'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = ('binop', p[2], p[1], p[3])

def p_factor(p):
    '''factor : INT
              | FLOAT
              | CHAR
              | VARIAVEL
              | ABRE_PARENTESES expression FECHA_PARENTESES
              | NEGACAO factor
              | factor RESTO factor'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = ('neg', p[2])
    else:
        p[0] = ('binop', p[2], p[1], p[3])

def p_if_statement(p):
    '''if_statement : COND_IF ABRE_PARENTESES expression FECHA_PARENTESES INICIO statement_list FIM
                    | COND_IF ABRE_PARENTESES expression FECHA_PARENTESES INICIO statement_list FIM COND_ELSE INICIO statement_list FIM'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if-else', p[3], p[6], p[10])

def p_while_statement(p):
    '''while_statement : REP_DURING ABRE_PARENTESES expression FECHA_PARENTESES INICIO statement_list FIM'''
    p[0] = ('while', p[3], p[6])

def p_for_statement(p):
    '''for_statement : REP_THROUGH ABRE_PARENTESES VARIAVEL PONTO_VIRGULA expression PONTO_VIRGULA expression FECHA_PARENTESES INICIO statement_list FIM'''
    p[0] = ('for', p[3], p[5], p[7], p[10])

def p_declaration(p):
    '''declaration : type_specifier VARIAVEL PONTO_VIRGULA'''
    p[0] = ('declare', p[1], p[2])

def p_error(p):
    if p:
        print(f"Erro de sintaxe: {p.value} na linha {p.lineno}")
    else:
        print("Erro de sintaxe no final do arquivo")

parser = yacc.yacc()

def parse_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    result = parser.parse(data, tracking=True)
    print(result)

if __name__ == "__main__":
    # Obtém o caminho absoluto do arquivo
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'exemplo.txt')
    parse_file(file_path)
