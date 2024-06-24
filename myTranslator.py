import os

def translate_to_python(command_descriptions, filename, output_folder_py):
    print("Translating to Python")
    global translated_code
    translated_code = ""
    array_of_atribs = []
    indent_level = 0
    program_started = False

    for command in command_descriptions:
        if command == "INICIO_PROGRAMA":
            program_started = True
            continue
        elif command == "FIM_PROGRAMA":
            break

        if not program_started:
            continue

        if "INICIO" in command and command != "INICIO_PROGRAMA":
            indent_level += 1
            continue
        
        elif "FIM" in command and command != "FIM_PROGRAMA":
            indent_level -= 1
            continue

        if "REP_DURING" in command:
            condition = command.split("=>")[1].strip()
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO ", "").strip()
            translated_code += "    " * indent_level + f"while {condition}:\n"
        
        elif "REP_THROUGH" in command:
            loop_parameters = command.split("=>")[1].strip()
            var, start_condition, end_condition = loop_parameters.split(";")
            translated_code += "    " * indent_level + f"for {var.strip()} in range({start_condition.strip()}, {end_condition.strip()}):\n"
        
        elif "COND_IF" in command:
            condition = command.split("=>")[1].strip()
            if "CONDICAO" in condition:
                condition = condition.replace("CONDICAO ", "").strip()
            translated_code += "    " * indent_level + f"if {condition}:\n"
        
        elif "COND_ELSE" in command:
            indent_level -= 1
            translated_code += "    " * indent_level + "else:\n"
            indent_level += 1
        
        elif "ATRIBUICAO" in command:
            assignment = command.replace("ATRIBUICAO => ", "").strip()
            if "EXPRESSAO" in assignment:
                assignment = assignment.replace("EXPRESSAO =>", "").strip()
            if ":" in assignment:
                assignment = assignment.replace(":", "=").strip()
            if "TERMO" in assignment:
                assignment = assignment.replace("TERMO ", "").strip()
            array_of_atribs.append(assignment.split(" =")[0])
            translated_code += "    " * indent_level + f"{assignment}\n"
        
        elif "EXPRESSAO" in command:
            expression = command.split("=>")[1].strip()
            if "TERMO" in expression:
                expression = expression.replace("TERMO ", "").strip()
            translated_code += "    " * indent_level + f"{expression}\n"
        
        elif "COMPARACAO" in command:
            comparison = command.split("=>")[1].strip()
            translated_code += "    " * indent_level + f"if {comparison}:\n"
            indent_level += 1
        
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
        "ATRIBUICAO => x : 5",
        "COND_IF => CONDICAO x == 5",
        "INICIO",
        "ATRIBUICAO => y : 10",
        "FIM",
        "COND_ELSE",
        "INICIO",
        "ATRIBUICAO => y : 20",
        "FIM",
        "FIM_PROGRAMA"
    ]
    translate_to_python(example_commands, "output.py", ".")
