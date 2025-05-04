from calendar import c
import re
import unittest

tokens = ['access', 'and', 'begin', 'different', 'div', 'egal', 'else', 'elseif', 'end', 'entier', 'false', 'fois', 'for', 'function', 'ident', 'if', 'in', 'inf', 'inf_strict', 'is', 'loop', 'moins', 'new', 'not', 'null', 'or', 'out', 'plus', 'point', 'procedure', 'record', 'rem', 'return', 'reverse', 'sup', 'sup_strict', 'then', 'true', 'type', 'use', 'while', 'with']
operateur = ['+', '-', '*', '/', '<', '>', '<=', '>=', '=', '/=', 'and', 'or', 'not']

def open_file(filename):
    file = open(filename, 'r')
    return file

def read_file(file):
    caractere = file.read(1)
    while caractere != '':
        current_word = ''
        while caractere != ' ' and caractere != '\n' and caractere != '':
            if caractere == 'a':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'c':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'c':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'e':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 's':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 's':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == ' ' or caractere == '\n':
                                        caractere = file.read(1)
                                        print('TOKEN: access\n', end='')
                                        current_word = ''
                elif caractere == 'n':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'd':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: and\n', end='')
                            current_word = ''
            elif caractere == 'b':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'e':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'g':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'i':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'n':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == ' ' or caractere == '\n':
                                    caractere = file.read(1)
                                    print('TOKEN: begin\n', end='')
                                    current_word = ''
            elif caractere == 'd':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'i':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'f':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'f':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'e':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 'r':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == 'e':
                                        current_word += caractere
                                        caractere = file.read(1)
                                        if caractere == 'n':
                                            current_word += caractere
                                            caractere = file.read(1)
                                            if caractere == 't':
                                                current_word += caractere
                                                caractere = file.read(1)
                                                if caractere == ' ' or caractere == '\n':
                                                    caractere = file.read(1)
                                                    print('TOKEN: different\n', end='')
                                                    current_word = ''
                    elif caractere == 'v':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: div\n', end='')
                            current_word = ''
            elif caractere == 'e':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'g':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'a':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'l':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: egal\n', end='')
                                current_word = ''
                elif caractere == 'l':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 's':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'e':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: else\n', end='')
                                current_word = ''
                            elif caractere == 'i':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 'f':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == ' ' or caractere == '\n':
                                        caractere = file.read(1)
                                        print('TOKEN: elseif\n', end='')
                                        current_word = ''
                elif caractere == 'n':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'd':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: end\n', end='')
                            current_word = ''
                    elif caractere == 't':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'i':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'e':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 'r':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == ' ' or caractere == '\n':
                                        caractere = file.read(1)
                                        print('TOKEN: entier\n', end='')
                                        current_word = ''
            elif caractere == 'f':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'a':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'l':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 's':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'e':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == ' ' or caractere == '\n':
                                    caractere = file.read(1)
                                    print('TOKEN: false\n', end='')
                                    current_word = ''
                elif caractere == 'o':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'r':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: for\n', end='')
                            current_word = ''
                    elif caractere == 'i':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 's':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: fois\n', end='')
                                current_word = ''
                elif caractere == 'u':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'n':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'c':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 't':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 'i':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == 'o':
                                        current_word += caractere
                                        caractere = file.read(1)
                                        if caractere == 'n':
                                            current_word += caractere
                                            caractere = file.read(1)
                                            if caractere == ' ' or caractere == '\n':
                                                caractere = file.read(1)
                                                print('TOKEN: function\n', end='')
                                                current_word = ''
            elif caractere == 'i':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'n':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'd':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'e':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'n':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 't':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == ' ' or caractere == '\n':
                                        caractere = file.read(1)
                                        print('TOKEN: indent\n', end='')
                                        current_word = ''
                    elif caractere == ' ' or caractere == '\n':
                        caractere = file.read(1)
                        print('TOKEN: in\n', end='')
                        current_word = ''
                    elif caractere == 'f':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: inf\n', end='')
                            current_word = ''
                        elif caractere == '_':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 's':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 't':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == 'r':
                                        current_word += caractere
                                        caractere = file.read(1)
                                        if caractere == 'i':
                                            current_word += caractere
                                            caractere = file.read(1)
                                            if caractere == 'c':
                                                current_word += caractere
                                                caractere = file.read(1)
                                                if caractere == 't':
                                                    current_word += caractere
                                                    caractere = file.read(1)
                                                    if caractere == ' ' or caractere == '\n':
                                                        caractere = file.read(1)
                                                        print('TOKEN: inf_strict\n', end='')
                                                        current_word = ''
                elif caractere == 'f':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == ' ' or caractere == '\n':
                        caractere = file.read(1)
                        print('TOKEN: if\n', end='')
                        current_word = ''
                elif caractere == 's':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == ' ' or caractere == '\n':
                        caractere = file.read(1)
                        print('TOKEN: is\n', end='')
                        current_word = ''
            elif caractere == 'l':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'o':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'o':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'p':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: loop\n', end='')
                                current_word = ''
            elif caractere == 'm':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'o':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'i':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'n':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 's':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == ' ' or caractere == '\n':
                                    caractere = file.read(1)
                                    print('TOKEN: moins\n', end='')
                                    current_word = ''
            elif caractere == 'n':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'e':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'w':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: new\n', end='')
                            current_word = ''
                elif caractere == 'o':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 't':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: not\n', end='')
                            current_word = ''
                elif caractere == 'u':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'l':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'l':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: null\n', end='')
                                current_word = ''
            elif caractere == 'o':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'r':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == ' ' or caractere == '\n':
                        caractere = file.read(1)
                        print('TOKEN: or\n', end='')
                        current_word = ''
                elif caractere == 'u':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 't':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: out\n', end='')
                            current_word = ''
            elif caractere == 'p':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'l':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'u':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 's':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: plus\n', end='')
                                current_word = ''
                elif caractere == 'o':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'i':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'n':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 't':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == ' ' or caractere == '\n':
                                    caractere = file.read(1)
                                    print('TOKEN: point\n', end='')
                                    current_word = ''
                elif caractere == 'r':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'o':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'c':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'e':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 'd':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == 'u':
                                        current_word += caractere
                                        caractere = file.read(1)
                                        if caractere == 'r':
                                            current_word += caractere
                                            caractere = file.read(1)
                                            if caractere == 'e':
                                                current_word += caractere
                                                caractere = file.read(1)
                                                if caractere == ' ' or caractere == '\n':
                                                    caractere = file.read(1)
                                                    print('TOKEN: procedure\n', end='')
                                                    current_word = ''
            elif caractere == 'r':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'e':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'c':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'o':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'r':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 'd':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == ' ' or caractere == '\n':
                                        caractere = file.read(1)
                                        print('TOKEN: record\n', end='')
                                        current_word = ''
                    elif caractere == 'm':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: rem\n', end='')
                            current_word = ''
                    elif caractere == 't':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'u':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'r':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 'n':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == ' ' or caractere == '\n':
                                        caractere = file.read(1)
                                        print('TOKEN: return\n', end='')
                                        current_word = ''
            elif caractere == 's':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'u':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'p':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: sup\n', end='')
                            current_word = ''
                        elif caractere == '_':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 's':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == 't':
                                    current_word += caractere
                                    caractere = file.read(1)
                                    if caractere == 'r':
                                        current_word += caractere
                                        caractere = file.read(1)
                                        if caractere == 'i':
                                            current_word += caractere
                                            caractere = file.read(1)
                                            if caractere == 'c':
                                                current_word += caractere
                                                caractere = file.read(1)
                                                if caractere == 't':
                                                    current_word += caractere
                                                    caractere = file.read(1)
                                                    if caractere == ' ' or caractere == '\n':
                                                        caractere = file.read(1)
                                                        print('TOKEN: sup_strict\n', end='')
                                                        current_word = ''
            elif caractere == 't':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 'h':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'e':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'n':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: then\n', end='')
                                current_word = ''
                elif caractere == 'r':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'u':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'e':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: true\n', end='')
                                current_word = ''
                elif caractere == 'y':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'p':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'e':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: type\n', end='')
                                current_word = ''
            elif caractere == 'u':
                current_word += caractere
                caractere = file.read(1)
                if caractere == 's':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'e':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == ' ' or caractere == '\n':
                            caractere = file.read(1)
                            print('TOKEN: use\n', end='')
                            current_word = ''
            elif caractere == 'w':


                current_word += caractere
                caractere = file.read(1)
                if caractere == 'h':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 'i':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'l':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == 'e':
                                current_word += caractere
                                caractere = file.read(1)
                                if caractere == ' ' or caractere == '\n':
                                    caractere = file.read(1)
                                    print('TOKEN: while\n', end='')
                                    current_word = ''
                
                elif caractere == 'i':
                    current_word += caractere
                    caractere = file.read(1)
                    if caractere == 't':
                        current_word += caractere
                        caractere = file.read(1)
                        if caractere == 'h':
                            current_word += caractere
                            caractere = file.read(1)
                            if caractere == ' ' or caractere == '\n':
                                caractere = file.read(1)
                                print('TOKEN: with\n', end='')
                                current_word = ''
            elif caractere.isdigit():
                if current_word == '':
                    current_word += caractere
                    caractere = file.read(1)
                    while caractere.isdigit():
                        current_word += caractere
                        caractere = file.read(1)
                    if caractere == ' ' or caractere == '\n' or caractere == '':
                        print('ENTIER:', current_word)
                        current_word = ''
                    else:
                        while caractere != ' ' and caractere != '\n' and caractere != '':
                            current_word += caractere
                            caractere = file.read(1)
                        print('ERREUR')
                        current_word = ''
                else:
                    while caractere != ' ' and caractere != '\n' and caractere != '':
                        current_word += caractere
                        caractere = file.read(1)
                    print('VARIABLE:', current_word)
                    current_word = ''
            elif not caractere.isalpha():
                while caractere != ' ' and caractere != '\n' and caractere != '':
                    current_word += caractere
                    caractere = file.read(1)
                print('ERREUR')
                current_word = ''    
            # Lire le caractère suivant
            else:
                current_word += caractere
                caractere = file.read(1)
        if current_word != '':
            print('VARIABLE:', current_word)
        caractere = file.read(1)
    file.close()
    return 0


#-----------------TESTS-----------------#


def test_read_file():
    """Test de la fonction read_file"""
    assert read_file(open_file("lexeur/test1.txt")) == 0

def test_open_file():
    """Test de la fonction open_file"""
    assert open_file("lexeur/test1.txt") != None

#faire des fonctions de tests de fichiers test1, test2 etc
#def test_test1():
#    assert read_file(open_file("lexeur/test1.txt")) == 0

#def test_test2():
#    assert read_file(open_file("lexeur/test2.txt")) == 0
#if __name__ == '__main__':
#    test_open_file()
#    print("test_open_file() OK")
#    test_read_file()
#    print("test_read_file() OK")
#    test_test1()
#    print("test_test1() OK")
#    test_test2()
#    print("test_test2() OK")

#problèmes avec les tests, il faut que je les refasse

