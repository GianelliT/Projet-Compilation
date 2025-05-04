from lexeur_non_automate import file_to_token, tokenize, delete_comments


#----------------------Test tokenize----------------------#

def test_tokenize_sujet_test(file):
    with open(file, 'r') as f:
        code = f.read()
    assert tokenize(code) == [33, ('Ada', 1), 46, ('Text_IO', 1), 48, 31, ('Ada', 1), 46, ('Text_IO', 1), 48, 0, 23, ('unDebut', 1), 16, 0, 13, ('aireRectangle', 1), 49, ('larg', 1), 47, ('integer', 1), 48, ('long', 1), 47, ('integer', 1), 50, 26, ('integer', 1), 16, 0, ('aire', 1), 47, ('integer', 1), 48, 0, 6, 0, ('aire', 1), 47, 34, ('larg', 1), 42, ('long', 1), 48, 0, 26, ('aire', 1), 0, 10, ('aireRectangle', 1), 48, 0, 13, ('perimetre', 1), 46, ('Rectangle', 1), 49, ('larg', 1), 47, ('o786GH786jhg', 1), ('integer', 1), 48, ('long', 1), 47, ('integer', 1), 50, 26, ('integer', 1), 16, 0, ('p', 1), 47, ('integer', 1), 0, 6, 0, ('p', 1), 47, 34, ('larg', 1), 42, (2, 2), 40, ('long', 1), 42, (2, 2), 48, 0, 26, ('p', 1), 0, 10, ('perimetreRectangle', 1), 48, 0, 41, 41, ('VARIABLES', 1), 0, ('choix', 1), 47, ('integer', 1), 48, 0, 41, 41, ('PROCEDURE', 1), ('PRINCIPALE', 1), 0, 6, 0, ('choix', 1), 47, 34, (2, 2), 48, 0, 14, ('choix', 1), 34, (1, 2), 0, 28, ('valeur', 1), 47, 34, ('perimetreRectangle', 1), 49, (2, 2), 51, (3, 2), 50, 48, 0, ('put', 1), 49, ('valeur', 1), 50, 48, 0, 8, ('valeur', 1), 47, 34, ('aireRectangale', 1), 49, (2, 2), 51, (3, 2), 50, 48, 0, ('put', 1), 49, ('valeur', 1), 50, 48, 0, 10, 14, 48, 0, 10, ('unDebut', 1), 48]

def test_tokenize_test1(file):
    with open(file, 'r') as f:
        code = f.read()
    assert tokenize(code) == [23, ('MonProgramme', 1), 16, 0, ('Nombre', 1), 47, ('Integer', 1), 48, 0, 6, 0, ('x', 1), 34, (2, 2), 0, 41, 41, ('Test', 1), 0, 14, ('Nombre', 1), ('mod', 1), (2, 2), 34, (0, 2), 28, 0, ('x', 1), 34, ('x', 1), 40, (3, 2), 0, 8, 0, ('x', 1), 34, (4, 2), 0, 10, 14, 48, 0, 10, ('MonProgramme', 1), 48]

def test_tokenize_test2(file):
    with open(file, 'r') as f:
        code = f.read()
    assert tokenize(code) == [23, ('MonProgramme', 1), 16, 0, ('A', 1), 51, ('B', 1), 51, ('Somme', 1), 47, ('Integer', 1), 48, 0, 6, 0, ('A', 1), 47, 34, (5, 2), 48, 0, ('B', 1), 47, 34, (7, 2), 48, 0, 0, ('Somme', 1), 47, 34, ('A', 1), 40, ('B', 1), 48, 0, 10, ('MonProgramme', 1), 48]

#----------------------Test deletete_comments----------------------#

def test_delete_comments(file):
    with open(file, 'r') as f:
        code = f.read()
    tokens = tokenize(code)
    assert delete_comments(tokens) == [33, ('Ada', 1), 46, ('Text_IO', 1), 48, 31, ('Ada', 1), 46, ('Text_IO', 1), 48, 0, 23, ('unDebut', 1), 16, 0, 13, ('aireRectangle', 1), 49, ('larg', 1), 47, ('integer', 1), 48, ('long', 1), 47, ('integer', 1), 50, 26, ('integer', 1), 16, 0, ('aire', 1), 47, ('integer', 1), 48, 0, 6, 0, ('aire', 1), 47, 34, ('larg', 1), 42, ('long', 1), 48, 0, 26, ('aire', 1), 0, 10, ('aireRectangle', 1), 48, 0, 13, ('perimetre', 1), 46, ('Rectangle', 1), 49, ('larg', 1), 47, ('o786GH786jhg', 1), ('integer', 1), 48, ('long', 1), 47, ('integer', 1), 50, 26, ('integer', 1), 16, 0, ('p', 1), 47, ('integer', 1), 0, 6, 0, ('p', 1), 47, 34, ('larg', 1), 42, (2, 2), 40, ('long', 1), 42, (2, 2), 48, 0, 26, ('p', 1), 0, 10, ('perimetreRectangle', 1), 48, 0, ('choix', 1), 47, ('integer', 1), 48, 0, 6, 0, ('choix', 1), 47, 34, (2, 2), 48, 0, 14, ('choix', 1), 34, (1, 2), 0, 28, ('valeur', 1), 47, 34, ('perimetreRectangle', 1), 49, (2, 2), 51, (3, 2), 50, 48, 0, ('put', 1), 49, ('valeur', 1), 50, 48, 0, 8, ('valeur', 1), 47, 34, ('aireRectangale', 1), 49, (2, 2), 51, (3, 2), 50, 48, 0, ('put', 1), 49, ('valeur', 1), 50, 48, 0, 10, 14, 48, 0, 10, ('unDebut', 1), 48]

def test_delete_comments_test1(file):
    with open(file, 'r') as f:
        code = f.read()
    tokens = tokenize(code)
    assert delete_comments(tokens) == [23, ('MonProgramme', 1), 16, 0, ('Nombre', 1), 47, ('Integer', 1), 48, 0, 6, 0, ('x', 1), 34, (2, 2), 0, 14, ('Nombre', 1), ('mod', 1), (2, 2), 34, (0, 2), 28, 0, ('x', 1), 34, ('x', 1), 40, (3, 2), 0, 8, 0, ('x', 1), 34, (4, 2), 0, 10, 14, 48, 0, 10, ('MonProgramme', 1), 48]

def test_delete_comments_test2(file):
    with open(file, 'r') as f:
        code = f.read()
    tokens = tokenize(code)
    assert delete_comments(tokens) == [23, ('MonProgramme', 1), 16, 0, ('A', 1), 51, ('B', 1), 51, ('Somme', 1), 47, ('Integer', 1), 48, 0, 6, 0, ('A', 1), 47, 34, (5, 2), 48, 0, ('B', 1), 47, 34, (7, 2), 48, 0, 0, ('Somme', 1), 47, 34, ('A', 1), 40, ('B', 1), 48, 0, 10, ('MonProgramme', 1), 48]

#----------------------Test file_to_token----------------------#

def test_file_to_token():
    assert file_to_token("Analyse Lexicale/Tests/sujet_test.txt") == [33, ('Ada', 1), 46, ('Text_IO', 1), 48, 31, ('Ada', 1), 46, ('Text_IO', 1), 48, 0, 23, ('unDebut', 1), 16, 0, 13, ('aireRectangle', 1), 49, ('larg', 1), 47, ('integer', 1), 48, ('long', 1), 47, ('integer', 1), 50, 26, ('integer', 1), 16, 0, ('aire', 1), 47, ('integer', 1), 48, 0, 6, 0, ('aire', 1), 47, 34, ('larg', 1), 42, ('long', 1), 48, 0, 26, ('aire', 1), 0, 10, ('aireRectangle', 1), 48, 0, 13, ('perimetre', 1), 46, ('Rectangle', 1), 49, ('larg', 1), 47, ('o786GH786jhg', 1), ('integer', 1), 48, ('long', 1), 47, ('integer', 1), 50, 26, ('integer', 1), 16, 0, ('p', 1), 47, ('integer', 1), 0, 6, 0, ('p', 1), 47, 34, ('larg', 1), 42, (2, 2), 40, ('long', 1), 42, (2, 2), 48, 0, 26, ('p', 1), 0, 10, ('perimetreRectangle', 1), 48, 0, ('choix', 1), 47, ('integer', 1), 48, 0, 6, 0, ('choix', 1), 47, 34, (2, 2), 48, 0, 14, ('choix', 1), 34, (1, 2), 0, 28, ('valeur', 1), 47, 34, ('perimetreRectangle', 1), 49, (2, 2), 51, (3, 2), 50, 48, 0, ('put', 1), 49, ('valeur', 1), 50, 48, 0, 8, ('valeur', 1), 47, 34, ('aireRectangale', 1), 49, (2, 2), 51, (3, 2), 50, 48, 0, ('put', 1), 49, ('valeur', 1), 50, 48, 0, 10, 14, 48, 0, 10, ('unDebut', 1), 48]

def test_file_to_token_test1():
    assert file_to_token("Analyse Lexicale/Tests/test1.txt") == [23, ('MonProgramme', 1), 16, 0, ('Nombre', 1), 47, ('Integer', 1), 48, 0, 6, 0, ('x', 1), 34, (2, 2), 0, 14, ('Nombre', 1), ('mod', 1), (2, 2), 34, (0, 2), 28, 0, ('x', 1), 34, ('x', 1), 40, (3, 2), 0, 8, 0, ('x', 1), 34, (4, 2), 0, 10, 14, 48, 0, 10, ('MonProgramme', 1), 48]
    
def test_file_to_token_test2():
    assert file_to_token("Analyse Lexicale/Tests/test2.txt") == [23, ('MonProgramme', 1), 16, 0, ('A', 1), 51, ('B', 1), 51, ('Somme', 1), 47, ('Integer', 1), 48, 0, 6, 0, ('A', 1), 47, 34, (5, 2), 48, 0, ('B', 1), 47, 34, (7, 2), 48, 0, 0, ('Somme', 1), 47, 34, ('A', 1), 40, ('B', 1), 48, 0, 10, ('MonProgramme', 1), 48]

#----------------------Main----------------------#

if __name__ == "__main__":

    test_tokenize_sujet_test("Analyse Lexicale/Tests/sujet_test.txt")
    print("tokenize sujet_test OK")
    test_tokenize_test1("Analyse Lexicale/Tests/test1.txt")
    print("tokenize test1 OK")
    test_tokenize_test2("Analyse Lexicale/Tests/test2.txt")
    print("tokenize test2 OK")

    test_delete_comments("Analyse Lexicale/Tests/sujet_test.txt")
    print("delete_comments OK")
    test_delete_comments_test1("Analyse Lexicale/Tests/test1.txt")
    print("delete_comments test1 OK")
    test_delete_comments_test2("Analyse Lexicale/Tests/test2.txt")
    print("delete_comments test2 OK")

    test_file_to_token()
    print("file_to_token OK")
    test_file_to_token_test1()
    print("file_to_token test1 OK")
    test_file_to_token_test2()
    print("file_to_token test2 OK")





