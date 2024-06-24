import os

def translate_to_python(command_descriptions, filename, output_folder_py):
    print("Translating to Python")
    translated_code = ""
    array_of_atribs = []
    indent_level = 0
    program_started = False

    for command in command_descriptions:
        if ";"in command:
            command = command.replace(";", " ")
        if command == "INICIO_PROGRAMA":
            program_started = True
            continue
        elif command == "FIM_PROGRAMA":
            break

        if not program_started:
            continue

        if "INICIO" in command:
            indent_level += 1
            continue
        
        elif "FIM" in command:
            indent_level -= 1
            continue

        if "REP_DURING" in command:
            condition = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"while {condition}:\n"
            
        elif "COND_IF" in command:
            condition = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"if {condition}:\n"
        
        elif "COND_ELSE" in command:
            translated_code += "    " * indent_level + "else:\n"
        
        elif "ATRIBUICAO" in command:
            assignment = command.replace("ATRIBUICAO => ", "").strip()
            assignment = assignment.replace("->", "=").strip()
            assignment = assignment.replace(";", "").strip()
            array_of_atribs.append(assignment.split("=")[0].strip())
            translated_code += "    " * indent_level + f"{assignment}\n"
        
        elif "EXPRESSAO" in command:
            expression = command.split("=>")[1].strip()
            expression = expression.replace("->", "=").strip()
            translated_code += "    " * indent_level + f"{expression}\n"
        
        elif "COMPARACAO" in command:
            comparison = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"if {comparison}:\n"
        
        elif "ENTRADA" in command:
            var_name = command.split("ENTRADA")[1].strip()
            if var_name in array_of_atribs:
                translated_code += "    " * indent_level + f"{var_name} = int(input())\n"
            else:
                translated_code += "    " * indent_level + f"{var_name} = input()\n"
        
        elif "SAIDA" in command:
            output_vars = command.split("SAIDA")[1].strip()
            translated_code += "    " * indent_level + f"print({output_vars})\n"

    output_file = os.path.join(output_folder_py, filename)
    with open(output_file, 'w') as file:
        file.write(translated_code)

if __name__ == "__main__":
    example_commands = [
        "INICIO_PROGRAMA",
        "ATRIBUICAO => x : 5;",
        "COND_IF => CONDICAO x == 5",
        "INICIO",
        "ATRIBUICAO => y : 10;",
        "FIM",
        "COND_ELSE",
        "INICIO",
        "ATRIBUICAO => y : 20;",
        "FIM",
        "FIM_PROGRAMA"
    ]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    Outpath = os.path.join(script_dir, 'output_py/output.py')
    translate_to_python(example_commands, Outpath, ".")
