import re
import token
from webbrowser import get

keywords = ['access', 'and', 'begin','Character\'Val', 'else', 'elsif', 'end', 'false', 'for', 'function', 'if', 'in', 'is', 'loop', 'new', 'not', 'null', 'or', 'out', 'procedure', 'record', 'rem', 'return', 'reverse', 'then', 'true', 'type', 'use', 'while', 'with']

operators = ['=', '/=', '>', '<', '+', '-', '*', '/', 'rem', '-', '.', ':', ';', '(', ')', ',']

token_specification = [
    ('MISMATCHVAR', r'\d[0-9a-zA-Z]+'),
    ('IDENT', r'[a-zA-Z]([a-zA-Z0-9_])*'),
    ('INTEGER', r'\d+'),
    ('CHARACTER', r"'[ -~]'"), 
    ('OP', r'|'.join(map(re.escape, operators))),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]'),
    ('MISMATCH', r'.')
]

token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

def tokenize(code): #prend en paramètre le code brut
    tokens = []
    count_line = 1
    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'IDENT' and value in keywords:
            tokens.append(keywords.index(value)+4)
        elif kind != 'SKIP' and kind != 'NEWLINE':
            if kind == 'IDENT' :
                tokens.append((1, value))
            elif kind == 'INTEGER' :
                tokens.append((2, int(value)))
            elif kind == 'CHARACTER' :
                tokens.append((3, value[1]))
            elif kind == 'OP' :
                tokens.append(operators.index(value)+len(keywords)+4)
            elif kind == 'MISMATCH' or kind == 'MISMATCHVAR':
                print("erreur à la ligne: ", count_line, ',', value)
                break
        elif kind == 'NEWLINE':
            count_line += 1
            tokens.append(0)
        elif kind == 'SKIP':
            pass
    return tokens

def delete_comments(code): #prend en paramètre le code tokenizé
    tokens = []
    i = 0
    while i < len(code):
        if code[i] != len(keywords)+operators.index('-')+4:
            tokens.append(code[i])
            i += 1
        elif code[i] == len(keywords)+operators.index('-')+4:
            while code[i] != 0:
                i += 1
            i += 1
    return tokens

def get_code_lexical(code): #prend en paramètre le code tokenizé
    code_lexical_provisoire = []
    code_lexical = []
    for i in code:
        if type(i) != int and i[0] == 1:
            if i[1] not in code_lexical_provisoire:
                code_lexical_provisoire.append(i[1])
    for i in range(len(code_lexical_provisoire)):
        code_lexical.append((str(i+1), code_lexical_provisoire[i]))
    return code_lexical

def remove_newline(code):
    while 0 in code:
        code.remove(0)
    return code
   
def get_token_final(code): #prend en paramètre le code tokenizé
    code_lexical = get_code_lexical(code)
    token_final = []
    for i in code:
        if type(i) == int:
            token_final.append(i)
        elif type(i) != int and i[0] == 1:
            for j in code_lexical:
                if j[1] == i[1]:
                    token_final.append((1, int(j[0])))
        elif type(i) != int and i[0] == 2:
            token_final.append(i)
        elif type(i) != int and i[0] == 3:
            token_final.append(i)
    return token_final


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
        tokens = tokenize(code)
        tokens = delete_comments(tokens)
        code_lexical = get_code_lexical(tokens)
        tokens = remove_newline(tokens)
        token_final = get_token_final(tokens)
        print("TOKENS: \n", tokens, "\nCODE LEXICAL: \n", code_lexical, "\nTOKENS FINAUX: \n", token_final)
        return token_final
file_to_token('Analyse lexicale/Tests/sujet_test.txt')
