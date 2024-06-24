import os
import subprocess
import shutil
import subprocess

def build_executable(script, spec_path, dist_path):
    #obtém o caminho absoluto para o script e a pasta de distribuição personalizada 'output_exe'
    script_path = os.path.abspath(script)
    spec_file = os.path.join(spec_path, os.path.basename(script).replace('.py', '.spec'))
    command = ['pyinstaller', '--onefile', '--specpath', spec_path, '--distpath', dist_path, script_path]
    
    try:
        #executa o comando para gerar o executável
        subprocess.check_call(command)
        print(f"Executável gerado para {script} com sucesso!")

        #apaga a pasta 'build' após a geração do executável
        build_folder = os.path.join(os.getcwd(), 'build')
        if os.path.exists(build_folder):
            shutil.rmtree(build_folder)
            print("Pasta 'build' removida com sucesso.")
        
        #apaga o arquivo .spec após a geração do executável
        if os.path.exists(spec_file):
            os.remove(spec_file)
            print(f"Arquivo .spec {spec_file} removido com sucesso.")
        spec_dir = os.path.dirname(os.path.abspath(__file__))
        folder_spec = os.path.join(spec_dir, 'output_spec/') 
        shutil.rmtree(folder_spec)
        
    except subprocess.CalledProcessError as e:
        #exibe uma mensagem de erro se a geração do executável falhar
        print(f"Erro ao gerar executável para {script}: {e}")

def generate_executables(scripts_folder, spec_folder, dist_folder_name):
    
    #obtém o caminho completo para a pasta de scripts e a pasta de distribuição
    dist_path = os.path.join(os.getcwd(), dist_folder_name)
    
    #cria a pasta de distribuição se não existir ainda
    os.makedirs(dist_path, exist_ok=True)

    #itera sobre os arquivos .py na pasta de scripts e gera executáveis para cada um
    for file_name in os.listdir(scripts_folder):
        if file_name.endswith('.py'):
            script_path = os.path.join(scripts_folder, file_name)
            build_executable(script_path, spec_folder, dist_path)