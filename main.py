# esse arquivo é responsável por fazer a chamada das funções de tokenização e parsing com os arquivos de teste
#import das funções de tokenização e parsing
from lexer import tokenize_file
from myParser import parse_file
from myTranslator import translate_to_python
from builder import generate_executables
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'src_files')

spec_dir = os.path.dirname(os.path.abspath(__file__))
folder_spec = os.path.join(spec_dir, 'output_spec/') 
txt_dir = os.path.dirname(os.path.abspath(__file__))
folder_txt = os.path.join(txt_dir, 'files_txt/') 
py_dir = os.path.dirname(os.path.abspath(__file__))
folder_py = os.path.join(py_dir, 'files_py/') 
exe_dir = os.path.dirname(os.path.abspath(__file__))
folder_exe = os.path.join(exe_dir, 'files_exe/') 

os.makedirs(path, exist_ok=True)
os.makedirs(folder_txt , exist_ok=True)
os.makedirs(folder_py, exist_ok=True)
os.makedirs(folder_spec, exist_ok=True)
os.makedirs(folder_exe, exist_ok=True)

all_files = os.listdir(path)

def is_lagartixa_file(filename):
    return filename.endswith('.tixa')

#para cada arquivo, tokeniza e faz o parsing
for filename in all_files:
    file_path = os.path.join(path, filename)
    
    if is_lagartixa_file(filename):
        #diz qual arquivo está sendo compilado, que é o arquivo que está sendo tokenizado e parseado
        print(f"Compilando arquivo: {file_path}\n")

        # Tokenize o arquivo
        tokens = tokenize_file(file_path)
        print("Tokens:", tokens)

        # Parse o arquivo
        parse_output_file_txt = os.path.join(folder_txt , filename.replace('.tixa', '.txt'))
        parse_output_file_py = os.path.join(folder_py, filename.replace('.tixa', '.py'))
        parse_file(file_path, parse_output_file_txt)

        # Carregar comandos do arquivo parseado
        with open(parse_output_file_txt, 'r') as parsed_file:
            command_descriptions = parsed_file.readlines()

        # Traduzir comandos para Python
        translate_to_python(command_descriptions, filename.replace('.tixa', '.py'), folder_py)
        print("\n")

    else:
        print(f"Erro: O arquivo '{filename}' não possui a extensão .tixa e não será processado.\n")

# Gera executáveis para os scripts Python gerados
generate_executables(folder_py, folder_spec, folder_exe)
