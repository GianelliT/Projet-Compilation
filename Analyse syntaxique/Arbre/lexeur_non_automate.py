import re

keywords = ['access', 'and', 'begin','Character\'Val', 'else', 'elsif', 'end', 'false', 'for', 'function', 'if', 'in', 'is', 'loop', 'new', 'not', 'null', 'or', 'out', 'procedure', 'record', 'rem', 'return', 'reverse', 'then', 'true', 'type', 'use', 'while', 'with']

operators = ['=', '/=', '>', '<', '+', '-', '*', '/', 'rem', '-', '.', ':', ';', '(', ')', ',']

token_specification = [
    ('CHARVAL', r'Character\'Val'),
    ('INTEGER', r'\d+(?!([a-zA-Z]))'), 
    ('MISMATCHVAR', r'\d[0-9a-zA-Z]+'),
    ('IDENT', r'[a-zA-Z]([a-zA-Z0-9_])*'),
    ('CHARACTER', r"'[ -~]'"), 
    ('OP', r'|'.join(map(re.escape, operators))),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]'),
    ('APOSTROPHE', r"'"),
    ('MISMATCH', r'.')
]

token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

def tokenize(code,file): 
    tokens = []
    count_line = 1
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        last_newline_index = code.rfind('\n', 0, mo.start())
        column = mo.start() - last_newline_index

        if kind == 'IDENT' and value in keywords:
            tokens.append([keywords.index(value)+4, count_line, column])
        elif kind == 'CHARVAL':
            tokens.append([7, count_line, column])
        elif kind != 'SKIP' and kind != 'NEWLINE':
            if kind == 'IDENT':
                tokens.append([(1, value), count_line, column])
            elif kind == 'INTEGER':
                if int(value) > 2147483647:
                    error_printer(value, count_line, column, file)
                else:
                    tokens.append([(2, int(value)), count_line, column])
            elif kind == 'CHARACTER':
                tokens.append([(3, value[1]), count_line, column])
            elif kind == 'OP':
                tokens.append([operators.index(value)+len(keywords)+4, count_line, column])
            elif kind == 'APOSTROPHE':
                tokens.append([(8, "commentaire"), count_line, column])
            elif kind == 'MISMATCH' or kind == 'MISMATCHVAR':
                if code.rfind('--', last_newline_index, mo.start()) == -1:
                    error_printer(value, count_line, column, file)
        elif kind == 'NEWLINE':
            count_line += 1
            tokens.append([0])
        elif kind == 'SKIP':
            pass
        
    return tokens

def error_printer(value,line,column,file):
    print(f"Fichier \"{file}\", ligne {line}")
    with open(file, 'r') as f:
        lines = f.readlines()
        current_line = lines[line-1]
        print(current_line.replace('\n', ''))
        print(" "*(column-1) + "^"*len(value))
        print(f"Erreur dans le lexeur: {value} n'est pas un token valide\n")
    

def delete_comments(code):
    tokens = []
    i = 0
    while i < len(code):
        if code[i][0] != len(keywords)+operators.index('-')+4:
            tokens.append(code[i])
            i += 1
        elif code[i][0] == len(keywords)+operators.index('-')+4 :
            if code[i+1][0] == len(keywords)+operators.index('-')+4:
                i += 2
                while code[i][0] != 0:
                    i += 1
                i += 1
            else:
                tokens.append(code[i])
                i += 1
    return tokens

def get_code_lexical(code): #prend en paramètre le code tokenizé
    code_lexical_provisoire = []
    code_lexical = []
    for token in code:
        if type(token[0]) != int and token[0][0] == 1:
            if token[0][1] not in code_lexical_provisoire:
                code_lexical_provisoire.append(token[0][1])
    for i in range(len(code_lexical_provisoire)):
        code_lexical.append((str(i+1), code_lexical_provisoire[i]))
    return code_lexical

def remove_newline(code):
    while [0] in code:
        code.remove([0])
    return code

def remove_accents(input_str):
    accents = {
        'a': 'aàáâãäå',
        'e': 'eèéêë',
        'i': 'iìíîï',
        'o': 'oòóôõö',
        'u': 'uùúûü',
        'A': 'AÀÁÂÃÄÅ',
        'E': 'EÈÉÊË',
        'I': 'IÌÍÎÏ',
        'O': 'OÒÓÔÕÖ',
        'U': 'UÙÚÛÜ'
    }

    for char, accented_chars in accents.items():
        for accented_char in accented_chars:
            input_str = input_str.replace(accented_char, char)

    return input_str
   
def get_token_final(code): #prend en paramètre le code tokenizé
    code_lexical = get_code_lexical(code)
    tokens_final = []
    tokens_index = []
    for token in code:
        if type(token[0]) == int:
            tokens_final.append(token[0])
            tokens_index.append(token[1:])
        elif type(token[0]) != int and token[0][0] == 1:
            for j in code_lexical:
                if j[1] == token[0][1]:
                    tokens_final.append((1, int(j[0])))
                    tokens_index.append(token[1:])
        elif type(token[0]) != int and token[0][0] == 2:
            tokens_final.append(token[0])
            tokens_index.append(token[1:])
        elif type(token[0]) != int and token[0][0] == 3:
            tokens_final.append(token[0])
            tokens_index.append(token[1:])
    return tokens_final , tokens_index

def tokens_to_lexique(tokens):
    lex = []
    for token in tokens:
        if token == 0:
            lex.append('NEWLINE')
        elif token == 1:
            lex.append('IDENT')
        elif token == 2:
            lex.append('INTEGER')
        elif token == 3:
            lex.append('CHARACTER')
        elif token-4<len(keywords):
            lex.append(keywords[token-4])
        elif token-4<len(keywords)+len(operators):
            lex.append(operators[token-len(keywords)-4])
        else:
            lex.append(token)
    return lex

def get_lexique():
    global keywords
    global operators
    with open('lexique.txt', 'w') as file:
        file.write('1  -> IDENT\n')
        file.write('2  -> INTEGER\n')
        file.write('3  -> CHARACTER\n')
        for i in range(len(keywords)):
            if i+4 <= 9:
                file.write(str(i+4) + '  -> ' + keywords[i] + '\n')
            else:
                file.write(str(i+4) + ' -> ' + keywords[i] + '\n')
        for i in range(len(operators)):
            file.write(str(i+len(keywords)+4) + ' -> ' + operators[i] + '\n')
            
def file_to_token(file):
    with open(file, 'r') as f:
        code = f.read()
        code = remove_accents(code)
        tokens = tokenize(code, file)
        tokens = delete_comments(tokens)
        code_lexical = get_code_lexical(tokens)
        tokens = remove_newline(tokens)
        tokens_final , tokens_index = get_token_final(tokens)
        #print("TOKENS: \n", tokens, "\nCODE LEXICAL: \n", code_lexical, "\nTOKENS FINAUX: \n", tokens_final, "\nINDEX: \n", tokens_index)
        return tokens_final, code_lexical , tokens_index
