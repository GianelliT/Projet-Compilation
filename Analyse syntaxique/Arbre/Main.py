import os

from tree import *
from lexeur_non_automate import *
from fichier import *

def process_file(file_path):
    # On récupère les tokens, le lexique (['1','Resultat'..) et les indexs (ligne colonne de chaque token)
    tokens, code, index = file_to_token(file_path)
    # On crée un arbre vide et on lui donne le code, les tokens et les indexs
    arbre = Arbre()
    arbre.set_code(code)
    arbre.set_tokens_index(index)
    arbre.set_file_path(file_path)
    # On appelle l'axiome de la grammaire, qui va recursivement appeler les autres fonctions 
    # et construire l'arbre en consommant les tokens
    try:
        fichier(tokens, arbre, arbre.add_node("FICHIER", arbre.add_node("PROGRAM", "start")))
    except Exception as e:
        # Si on a une erreur, on affiche l'erreur, l'arbre actuel et le nombre de tokens restant
        print("Erreur lors de la construction de l'arbre de dérivation\n",e)
        print("Tokens restant: ", len(tokens))
        
    # On informe que tous les tokens ont été consommés, l'arbre est terminé
    if len(tokens) == 0:
        print(f"Tous les tokens pour le fichier {file_path} ont été consommés")
    
    # On creer le premier fichier de l'arbre de dérivation
    arbre.render()
    # Ensuite on applique l'élagage et on créer le deuxième fichier
    name = arbre.get_file_path().split('/')[-1].split('.')[0]
    elagage(name+"_arbre")
    display(name+"_arbre_elag")
    # On applique la rotation et on créer le troisième fichier
    effective_rotate_gauche(name+"_arbre_elag")
    display(name+"_arbre_elag_rotation")
    # On deplace les fichiers dans les dossiers correspondants
    # On creer les dossiers si ils n'existent pas
    if not os.path.exists("ArbresIntermediaires"):
        os.mkdir("ArbresIntermediaires")
    if not os.path.exists("ArbresElagues"):
        os.mkdir("ArbresElagues")
    if not os.path.exists("diagraph"):
        os.mkdir("diagraph")
    os.system(f"mv {name}_arbre {name}_arbre_elag {name}_arbre_elag_rotation ./diagraph")
    os.system(f"mv {name}_arbre.pdf {name}_arbre_elag.pdf ./ArbresIntermediaires")
    os.system(f"mv {name}_arbre_elag_rotation.pdf ./ArbresElagues")

def process_all_files(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            print(f"\nTraitement du fichier : {file_path}")
            process_file(file_path)


directory_path = "Analyse lexicale/Tests/"
process_all_files(directory_path)
#process_file("Analyse lexicale/Tests/test_if_cond.txt",1)
