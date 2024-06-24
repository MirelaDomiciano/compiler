import os
import ply.yacc as yacc
from lexer import tokens, lexer
from myTranslator import translate_to_python

# Definindo a precedência dos operadores
precedence = (
    ('left', 'OU'),
    ('left', 'E'),
    ('left', 'MENOR', 'MAIOR', 'MENOR_IGUAL', 'MAIOR_IGUAL', 'IGUAL', 'DIFERENTE'),
    ('left', 'SOMA', 'SUBTRACAO'),
    ('left', 'MULTIPLICACAO', 'DIVISAO', 'RESTO'),
    ('right', 'NEGACAO')
)

# Definição da gramática
def p_programa(p):
    '''programa : INICIO_PROGRAMA declaracoes comandos FIM_PROGRAMA'''
    p[0] = ('programa', p[2], p[3])

def p_declaracoes(p):
    '''declaracoes : declaracao declaracoes
                   | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_declaracao(p):
    '''declaracao : TIPO_INT VARIAVEL PONTO_VIRGULA
                  | TIPO_FLOAT VARIAVEL PONTO_VIRGULA
                  | TIPO_CHAR VARIAVEL PONTO_VIRGULA'''
    p[0] = ('declaracao', p[1], p[2])

def p_comandos(p):
    '''comandos : comando comandos
                | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_comando(p):
    '''comando : atribuicao
               | condicional
               | repeticao
               | entrada
               | saida'''
    p[0] = p[1]

def p_atribuicao(p):
    '''atribuicao : VARIAVEL ATRIBUICAO expressao PONTO_VIRGULA'''
    p[0] = ('atribuicao', p[1], p[3])

def p_condicional(p):
    '''condicional : COND_IF ABRE_PARENTESES expressao FECHA_PARENTESES bloco
                   | COND_IF ABRE_PARENTESES expressao FECHA_PARENTESES bloco COND_ELSE bloco'''
    if len(p) == 6:
        p[0] = ('condicional', p[3], p[5])
    else:
        p[0] = ('condicional', p[3], p[5], p[7])

def p_repeticao(p):
    '''repeticao : REP_DURING ABRE_PARENTESES expressao FECHA_PARENTESES bloco'''
    p[0] = ('repeticao', 'during', p[3], p[5])

def p_entrada(p):
    '''entrada : ENTRADA ABRE_PARENTESES VARIAVEL FECHA_PARENTESES PONTO_VIRGULA'''
    p[0] = ('entrada', p[3])

def p_saida(p):
    '''saida : SAIDA ABRE_PARENTESES expressao FECHA_PARENTESES PONTO_VIRGULA'''
    p[0] = ('saida', p[3])

def p_bloco(p):
    '''bloco : INICIO comandos FIM'''
    p[0] = p[2]

def p_expressao(p):
    '''expressao : expressao SOMA expressao
                 | expressao SUBTRACAO expressao
                 | expressao MULTIPLICACAO expressao
                 | expressao DIVISAO expressao
                 | expressao RESTO expressao
                 | expressao MENOR expressao
                 | expressao MAIOR expressao
                 | expressao MENOR_IGUAL expressao
                 | expressao MAIOR_IGUAL expressao
                 | expressao IGUAL expressao
                 | expressao DIFERENTE expressao
                 | expressao E expressao
                 | expressao OU expressao
                 | SUBTRACAO expressao %prec NEGACAO
                 | NEGACAO expressao
                 | ABRE_PARENTESES expressao FECHA_PARENTESES
                 | VARIAVEL
                 | INT 
                 | FLOAT 
                 | CHAR 
                 | STRING 
                 | expressao VIRGULA expressao'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 3:
        p[0] = (p[1], p[2])
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

def parse_file(input_filename, folder_txt, folder_py):
    
    print(f"Parsing file: {input_filename}")

    # Lista de comandos parseados
    command_descriptions = []

    with open(input_filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("startProgram"):
                command_descriptions.append("INICIO_PROGRAMA")
            elif line.startswith("endProgram"):
                command_descriptions.append("FIM_PROGRAMA")
            elif line.startswith("start"):
                command_descriptions.append("INICIO")
            elif line.startswith("end"):
                command_descriptions.append("FIM")
            elif line.startswith("if"):
                condition = line.split("(")[1].split(")")[0]
                command_descriptions.append(f"COND_IF => {condition}")
            elif line.startswith("else"):
                command_descriptions.append("COND_ELSE")
            elif line.startswith("during"):
                condition = line.split("(")[1].split(")")[0]
                command_descriptions.append(f"REP_DURING => {condition}")
            elif line.startswith("int") or line.startswith("float") or line.startswith("char") or line.startswith("string"):
                assignment = line.replace("int ", "").replace("float ", "").replace("char ", "").replace("string ", "")
                command_descriptions.append(f"ATRIBUICAO => {assignment.replace('=', '->')}")
            elif line.startswith("in"):
                var = line.split("(")[1].split(")")[0]
                command_descriptions.append(f"ENTRADA {var}")
            elif line.startswith("out"):
                var = line.split("(")[1].split(")")[0]
                command_descriptions.append(f"SAIDA {var}")
            elif line.startswith("start"):
                command_descriptions.append("INICIO")
            elif line.startswith("end"):
                command_descriptions.append("FIM")
            else:
                command_descriptions.append(f"EXPRESSAO => {line}")

    output_py = os.path.join(folder_py, os.path.basename(input_filename).replace(".tixa", ".py"))
    translate_to_python(command_descriptions, output_py, folder_py)

    # Escreve os comandos parseados em um arquivo de saída .txt
    output_file_txt = os.path.join(folder_txt, os.path.basename(input_filename).replace(".tixa", ".txt"))
    with open(output_file_txt, 'w') as file:
        for command in command_descriptions:
            file.write(command + "\n")

def examples_tixa(filename):
    return filename.endswith('.tixa')

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder_txt = os.path.join(base_dir, 'files_txt')
    folder_py = os.path.join(base_dir, 'files_py')
    src_folder = os.path.join(base_dir, 'src')

    os.makedirs(folder_txt, exist_ok=True)
    os.makedirs(folder_py, exist_ok=True)

    all_files = os.listdir(src_folder)
    for filename in all_files:
    
        file_path = os.path.join(src_folder, filename)
    
        if examples_tixa(filename):
        
            parse_file(file_path, folder_txt, folder_py)
            print("\n")
            
        else:
            print(f"Erro: O arquivo '{filename}' não possui a extensão .pin e não será processado.\n")

