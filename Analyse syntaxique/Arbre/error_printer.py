from lexeur_non_automate import tokens_to_lexique

def error_printer(function,tokens,tree,wanted_tokens):
    value = tokens[0]
    if type(value) == tuple:
        if value[0] == 1:
            #make a copy of code
            #code = tree.get_code().copy()
            #value_str = code[value[1]-1][1]
            value_str = "error"
        elif value[0] == 2:
            value_str = str(value[1])
        else:
            value_str = str(value[1])
    else:
        value_str = tokens_to_lexique([value])[0]
    tokens_index = tree.get_tokens_index()
    file = tree.get_file_path()
    index = len(tokens_index) - len(tokens)
    line, column = tokens_index[index][0], tokens_index[index][1]
    error_string = ""
    with open(file, 'r') as f:
        lines = f.readlines()
        current_line = lines[line-1]
        error_string += f"Fichier \"{file}\", ligne {line}, fonction {function}\n"
        error_string += current_line
        error_string += " "*(column-1) + "^"*len(value_str) + "\n"
        error_string += f"Erreur syntaxique: {value_str}\n"
        attendue = tokens_to_lexique(wanted_tokens)
        error_string += "Attendue: "
        for mot in attendue:
            error_string += mot + " "
        raise Exception(error_string)