import os
from lexer import tokenize_file
from myParser import parse_file

# Definindo os diretórios
base_dir = os.path.dirname(os.path.abspath(__file__))
folder_txt = os.path.join(base_dir, 'files_txt/')
folder_py = os.path.join(base_dir, 'files_py/')
folder_src = os.path.join(base_dir, 'src_files/')

# Criando os diretórios se não existirem
os.makedirs(folder_txt, exist_ok=True)
os.makedirs(folder_py, exist_ok=True)
os.makedirs(folder_src, exist_ok=True)

# Função para verificar a extensão do arquivo
def tixa_example(filename):
    return filename.endswith('.tixa')



# Processando cada arquivo no diretório src_files
for filename in all_files:
    file_path = os.path.join(folder_src, filename)

    if tixa_example(filename):
        print(f"Compilando arquivo: {file_path}\n")

        print("Tokens:")
        try:
            tokens = tokenize_file(file_path)
            for token in tokens:
                print(token)
        except Exception as e:
            print(f"Erro ao tokenizar o arquivo {filename}: {e}")
            continue

        print("\nParsing:")
        try:
            parse_file(file_path, folder_txt, folder_py)
            print(f"Parsing do arquivo {filename} concluído com sucesso.\n")
        except Exception as e:
            print(f"Erro ao fazer o parsing do arquivo {filename}: {e}")

    else:
        print(f"Erro: O arquivo '{filename}' não possui a extensão .tixa e não será processado.\n")
