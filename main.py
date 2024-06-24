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

for filename in all_files:
    file_path = os.path.join(path, filename)
    
    if is_lagartixa_file(filename):
        print(f"Compilando arquivo: {file_path}\n")

        tokens = tokenize_file(file_path)
        print("Tokens:", tokens)
        
        parse_file(file_path, folder_txt, folder_py)

    else:
        print(f"Erro: O arquivo não possui a extensão .tixa \n")

# Gera executáveis para os scripts Python gerados
generate_executables(folder_py, folder_spec, folder_exe)
