import re
from graphviz import Digraph, Source
from numpy import add
import os

class Arbre:
    
    def __init__(self):
        self.graph = Digraph('unix', filename='gram.gv', node_attr={'color': 'lightblue2', 'style': 'filled'})
        self.last = 0
        self.code = []
        self.tokens_index = []
        self.file_path = ""
        self.labels = []
    
    def add_node(self, label, parent):
        label = str(label)
        if label == "start" or parent == "start":
            pass
        elif self.labels[parent-1] in ["IDENT","IDENTPLUS","IDENTPLUS2","IDENTINTER"]:
            for i in self.code:
                if i[0] == label:
                    label = i[1]
                    
       
        name = str(self.last + 1)
        self.last += 1
        self.graph.node(name, label)
        if parent != "start":
            parent = str(parent)
            self.graph.edge(parent, name)
        self.labels.append(label)
        return self.last
    
    def set_code(self, code):
        self.code = code 
        
    def get_code(self):
        return self.code
    
    def get_tokens_index(self):
        return self.tokens_index
    
    def get_file_path(self):
        return self.file_path
    
    def set_tokens_index(self, tokens_index):
        self.tokens_index = tokens_index

    def set_file_path(self, file_path):
        self.file_path = file_path
            
    def render(self, view=False):
        # get only the file name
        name = self.file_path.split('/')[-1].split('.')[0]
        self.graph.filename = name+"_arbre"
        self.graph.render(view=view)
        
nonTerminals = ["FICHIER", "IDENT", "IDENTPLUS", "IDENTPLUS2", "IDENTINTER", "DECL", "DECL1", "DECL2", "DECLETOILE", "DECLETOILE2", "CHAMPS", "CHAMPSPLUS", "CHAMPSPLUS2", "TYPE", "PARAMS", "PARAMSINTER", "PARAM", "PARAMPLUS", "PARAMPLUS2", "MODE", "MODE2", "MODEINTER", "EXP", "EXPR1", "EXPR2", "EXACCES", "EXPRINTER", "EXPRPLUS", "EXPRPLUS2", "INSTR", "INSTR2", "INSTRPLUS", "INSTRPLUS2", "REVERSEINTER", "OP", "OPE'", "OP_PRIME", "OPE1", "OP1_PRIME", "OPE2", "OP2_PRIME", "OPE3", "OP3_PRIME", "OPE4", "OP4_PRIME", "OPE5", "OP5_PRIME", "OPE6", "OP6_PRIME", "OPE7", "OPE8", "ELSE", "THEN", "COMPARATEUR", "ORDRE", "EGAL", "ADD", "MULT", "ELSEINTER", "ELSIFETOILE", "ASSIGNINTER", "ENTIER", "CARACTER", "EGALITE"]

def elagage_parsing(file):
    ## Cette première partie de la fonction permet le parsing du fichier .gv
    with open(file, 'r+') as f:
        lines = f.readlines()
        liste = []
        for i in lines[2:-1]:
            nombre = ""
            j = 0
            while i[j] != " ":
                j+=1
                nombre += i[j]
            j+=1
            nombre = int(nombre)
            if i[j] == "[":
                liste.append([nombre])
                label = ""
                j+=7
                while i[j] != "]":
                    label += i[j]
                    j+=1
                liste[nombre-1].append(label)
            else:
                j+=3
                nombre2 = ""
                while i[j] != "\n": 
                    nombre2 += i[j]
                    j+=1
                liste[int(nombre)-1].append(int(nombre2))
        #print(liste)
        return liste

def elagage_non_terminaux(liste):
    ## Cette deuxième partie de la fonction permet de supprimer les feuilles qui sont des non terminaux
    i = 0
    while i < len(liste):
        if len(liste[i]) == 2 and liste[i][1] in nonTerminals:
            indice = liste[i][0]
            liste.remove(liste[i])
            for j in liste:
                k = 0
                while k < len(j):
                    if j[k] == indice:
                        j.remove(j[k])
                    elif  type(j[k]) == int: 
                        if j[k] >= indice:
                            index = j.index(j[k])
                            j[index] -= 1 
                        k+=1
                    else:
                        k+=1
        else:
            i+=1 
    return liste

def elagage_fils_unique(liste):
    ## Cette troisième partie de la fonction permet de supprimer les noeuds qui ont un seul fils
    i = 0                           
    while i < len(liste):
        if len(liste[i]) == 3:
            indice = liste[i][2]
            liste[i] = [liste[i][0]] + liste[liste[i][2] - 1][1:]
            liste.remove(liste[indice-1])
            j = 0
            while j < len(liste):
                for k in liste[j]:
                    if type(k) == int:
                        if k > indice:
                            index = liste[j].index(k)
                            liste[j][index] -= 1
                j+=1
        else:
            i+=1
    return liste

def elagage_reconstitution(file, liste):
    ## Cette quatrième partie de la fonction permet de reconstituer le fichier
    name = os.path.basename(file)
    # if file name as elag the name, fonction is rotation
    if "elag" in name:
        fonction = "_rotation"
    else:
        fonction = "_elag"
    with open(name + fonction, 'w') as f:
        f.write("digraph unix {\n")
        f.write("\tnode [color=lightblue2 style=filled]\n")
        for i in liste:
            f.write("\t" + str(i[0]) + " [label=" + i[1] + "]\n")
        for i in liste:
            for j in i[2:]:
                f.write("\t" + str(i[0]) + " -> " + str(j) + "\n")
        f.write("}")

def remonte_operateur(liste):
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OPE7":
            newString = liste[i+1][1][:2] + liste[i+2][1] + "\""
            liste[i][1] = newString
            liste[i].remove(i+2)
            liste[i].remove(i+3)
            liste.remove(liste[i+1])
            liste.remove(liste[i+1])
            j = 0
            while j < len(liste):
                for k in liste[j]:
                    if type(k) == int:
                        if k > i + 1:
                            index = liste[j].index(k)
                            liste[j][index] -= 2
                j+=1
        else:
            i-=1
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OP5_PRIME" or liste[i][1] == "OP6_PRIME":
            liste[i][1] = liste[i+1][1]
            liste[i].remove(i+2)
            liste.remove(liste[i+1])
            j = 0
            while j < len(liste):
                for k in liste[j]:
                    if type(k) == int:
                        if k > i + 1:
                            index = liste[j].index(k)
                            liste[j][index] -= 1
                j+=1
        else:
            i-=1
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OPE5" or liste[i][1] == "OPE6":
            noeud = liste[i]
            branchement = [liste[i]]
            while len(noeud) >= 3:
                noeud = liste[noeud[-1]-1]
                branchement.append(noeud)
            cut = False
            for j in range(len(branchement) - 1):
                if len(branchement[j]) == 3 and j != len(branchement) - 2:
                    cut = True
                    liste[branchement[j][0]-1][1] = branchement[j+1][1]
                    for k in range(2, len(branchement[j+1])):
                        liste[branchement[j][0]-1].append(branchement[j+1][k])
                    liste[branchement[j][0]-1].remove(branchement[j+1][0])
                    liste.remove(branchement[j+1])
                    removed = j+1
                    j = 0
                    while j < len(liste):
                        for k in liste[j]:
                            if type(k) == int:
                                if k > branchement[removed][0]:
                                    index = liste[j].index(k)
                                    liste[j][index] -= 1
                        j+=1
                    break
                else:
                    liste[branchement[j][0]-1][1] = branchement[j+1][1]
            if not cut:
                liste[branchement[-2][0]-1].remove(branchement[-1][0])
                liste.remove(branchement[-1])
                j = 0
                while j < len(liste):
                    for k in liste[j]:
                        if type(k) == int:
                            if k > branchement[-1][0]:
                                index = liste[j].index(k)
                                liste[j][index] -= 1
                    j+=1
        else:
            i-=1
    #i = len(liste) - 1
    # while i >= 0:
    #     if liste[i][1] == "EXPR1":
    #         liste[i][1] = liste[i+2][1]
    #         liste[i].remove(i+2)
    #         liste.remove(liste[i+1])
    #         j = 0
    #         while j < len(liste):
    #             for k in liste[j]:
    #                 if type(k) == int:
    #                     if k > i + 1:
    #                         index = liste[j].index(k)
    #                         liste[j][index] -= 1
    #             j+=1
    #         valueLast = liste[i][-1]
    #         liste[i].remove(valueLast)
    #         liste.remove(liste[valueLast-1])
    #         j = 0
    #         while j < len(liste):
    #             for k in liste[j]:
    #                 if type(k) == int:
    #                     if k > valueLast:
    #                         index = liste[j].index(k)
    #                         liste[j][index] -= 1
    #             j+=1
            
    #         for elem in liste[i+1][2:]:
    #             liste[i].append(elem)
    #         liste[i].remove(i+2)
    #         liste.remove(liste[i+1])
    #         j = 0
    #         while j < len(liste):
    #             for k in liste[j]:
    #                 if type(k) == int:
    #                     if k > i + 1:
    #                         index = liste[j].index(k)
    #                         liste[j][index] -= 1
    #             j+=1
    #     else:
    #         i-=1
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "ORDRE":
            newString = liste[i+1][1][:2] + liste[i+2][1][1:]
            liste[i][1] = newString
            liste[i].remove(i+2)
            liste[i].remove(i+3)
            liste.remove(liste[i+1])
            liste.remove(liste[i+1])
            j = 0
            while j < len(liste):
                for k in liste[j]:
                    if type(k) == int:
                        if k > i + 1:
                            index = liste[j].index(k)
                            liste[j][index] -= 2
                j+=1
        else:
            i-=1    
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OP4_PRIME" or liste[i][1] == "OP3_PRIME":
            liste[i][1] = liste[i+1][1]
            liste[i].remove(i+2)
            liste.remove(liste[i+1])
            j = 0
            while j < len(liste):
                for k in liste[j]:
                    if type(k) == int:
                        if k > i + 1:
                            index = liste[j].index(k)
                            liste[j][index] -= 1
                j+=1
        else:
            i-=1
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OPE4" or liste[i][1] == "OPE3":
            valueLast = liste[i][-1]
            liste[i][1] = liste[valueLast-1][1]
            liste[i].append(liste[valueLast-1][2])
            liste[i].remove(valueLast)
            liste.remove(liste[valueLast-1])
            j = 0
            while j < len(liste):
                for k in liste[j]:
                    if type(k) == int:
                        if k > valueLast:
                            index = liste[j].index(k)
                            liste[j][index] -= 1
                j+=1
        else:
            i-=1

    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OP1_PRIME":
            if liste[i+2][1]=='then':
                liste[i][1] = '"and then"'
                liste[i].remove(i+2)
                liste[i].remove(i+3)
                liste.remove(liste[i+1])
                liste.remove(liste[i+1])
                j = 0
                while j < len(liste):
                    for k in liste[j]:
                        if type(k) == int:
                            if k > i + 1:
                                index = liste[j].index(k)
                                liste[j][index] -= 2
                    j+=1
            elif liste[i+1][1]=='and' :
                liste[i][1] = liste[i+1][1]
                liste[i].remove(i+2)
                liste.remove(liste[i+1])
                j = 0
                while j < len(liste):
                    for k in liste[j]:
                        if type(k) == int:
                            if k > i + 1:
                                index = liste[j].index(k)
                                liste[j][index] -= 1
                    j+=1
        else:
            i-=1
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OPE1":
            noeud = liste[i]
            branchement = [liste[i]]
            while len(noeud) >= 3:
                noeud = liste[noeud[-1]-1]
                branchement.append(noeud)
            cut = False
            for j in range(len(branchement) - 1):
                if len(branchement[j]) == 3 and j != len(branchement) - 2:
                    cut = True
                    liste[branchement[j][0]-1][1] = branchement[j+1][1]
                    for k in range(2, len(branchement[j+1])):
                        liste[branchement[j][0]-1].append(branchement[j+1][k])
                    liste[branchement[j][0]-1].remove(branchement[j+1][0])
                    liste.remove(branchement[j+1])
                    removed = j+1
                    j = 0
                    while j < len(liste):
                        for k in liste[j]:
                            if type(k) == int:
                                if k > branchement[removed][0]:
                                    index = liste[j].index(k)
                                    liste[j][index] -= 1
                        j+=1
                    break
                else:
                    liste[branchement[j][0]-1][1] = branchement[j+1][1]
            if not cut:
                liste[branchement[-2][0]-1].remove(branchement[-1][0])
                liste.remove(branchement[-1])
                j = 0
                while j < len(liste):
                    for k in liste[j]:
                        if type(k) == int:
                            if k > branchement[-1][0]:
                                index = liste[j].index(k)
                                liste[j][index] -= 1
                    j+=1
        else:
            i-=1

    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OP_PRIME":
            if liste[i+2][1]=='else':
                liste[i][1] = '"or else"'
                liste[i].remove(i+2)
                liste[i].remove(i+3)
                liste.remove(liste[i+1])
                liste.remove(liste[i+1])
                j = 0
                while j < len(liste):
                    for k in liste[j]:
                        if type(k) == int:
                            if k > i + 1:
                                index = liste[j].index(k)
                                liste[j][index] -= 2
                    j+=1
            elif liste[i+1][1]=='or' :
                liste[i][1] = liste[i+1][1]
                liste[i].remove(i+2)
                liste.remove(liste[i+1])
                j = 0
                while j < len(liste):
                    for k in liste[j]:
                        if type(k) == int:
                            if k > i + 1:
                                index = liste[j].index(k)
                                liste[j][index] -= 1
                    j+=1
        else:
            i-=1
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "OP":
            noeud = liste[i]
            branchement = [liste[i]]
            while len(noeud) >= 3:
                noeud = liste[noeud[-1]-1]
                branchement.append(noeud)
            cut = False
            for j in range(len(branchement) - 1):
                if len(branchement[j]) == 3 and j != len(branchement) - 2:
                    cut = True
                    liste[branchement[j][0]-1][1] = branchement[j+1][1]
                    for k in range(2, len(branchement[j+1])):
                        liste[branchement[j][0]-1].append(branchement[j+1][k])
                    liste[branchement[j][0]-1].remove(branchement[j+1][0])
                    liste.remove(branchement[j+1])
                    removed = j+1
                    j = 0
                    while j < len(liste):
                        for k in liste[j]:
                            if type(k) == int:
                                if k > branchement[removed][0]:
                                    index = liste[j].index(k)
                                    liste[j][index] -= 1
                        j+=1
                    break
                else:
                    liste[branchement[j][0]-1][1] = branchement[j+1][1]
            if not cut:
                liste[branchement[-2][0]-1].remove(branchement[-1][0])
                liste.remove(branchement[-1])
                j = 0
                while j < len(liste):
                    for k in liste[j]:
                        if type(k) == int:
                            if k > branchement[-1][0]:
                                index = liste[j].index(k)
                                liste[j][index] -= 1
                    j+=1
        else:
            i-=1



    # while i >= 0:
    #     if liste[i][1] == "OP_PRIME":
    #         if liste[i+2][1]=='else':
    #             liste[i][1] = ""or else""
    #             liste[i].remove(i+2)
    #             liste[i].remove(i+3)
    #             liste.remove(liste[i+1])
    #             liste.remove(liste[i+1])
    #             j = 0
    #             while j < len(liste):
    #                 for k in liste[j]:
    #                     if type(k) == int:
    #                         if k > i + 1:
    #                             index = liste[j].index(k)
    #                             liste[j][index] -= 2
    #                 j+=1
    #         elif liste[i+1][1]=='or' : 
    #             liste[i][1] = liste[i+1][1]
    #             liste[i].remove(i+2)
    #             liste.remove(liste[i+1])
    #             j = 0
    #             while j < len(liste):
    #                 for k in liste[j]:
    #                     if type(k) == int:
    #                         if k > i + 1:
    #                             index = liste[j].index(k)
    #                             liste[j][index] -= 1
    #                 j+=1
    #         else : 
    #             print("je devrais pas être là")
    #     else:
    #         i-=1
    # i = len(liste) - 1
    # while i >= 0:
    #     if liste[i][1] == "OP":
    #         valueLast = liste[i][-1]
    #         liste[i][1] = liste[valueLast-1][1]
    #         # if len(liste[valueLast-1]) != 2:
    #         #     liste[i].append(liste[valueLast-1][2])
    #             # liste[i].remove(valueLast)
    #             # liste.remove(liste[valueLast-1])
    #             # j = 0
    #             # while j < len(liste):
    #             #     for k in liste[j]:
    #             #         if type(k) == int:
    #             #             if k > valueLast:
    #             #                 index = liste[j].index(k)
    #             #                 liste[j][index] -= 1
    #             #     j+=1
    #     else:
    #         i-=1

    

    # i = len(liste) - 1
    # while i >= 0:
    #     if liste[i][1] == "or" and len(liste[i]) == 3:
    #         liste[i][1] = liste[i+1][1]
    #         liste[i].remove(i+2)
    #         liste[i].append(liste[i+1][2])
    #         liste[i].append(liste[i+1][3])
    #         liste.remove(liste[i+1])
    #         j = 0
    #         while j < len(liste):
    #             for k in liste[j]:
    #                 if type(k) == int:
    #                     if k > i + 1:
    #                         index = liste[j].index(k)
    #                         liste[j][index] -= 1
    #             j+=1
    #     else:
    #         i-=1 

    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "not":
            liste[i-1][1] = liste[i][1]
   #         print(liste[i-1])
    #        print(i)
            liste[i-1].remove(i+1)
            liste.remove(liste[i])
            j = 0
            while j < len(liste):
                for k in liste[j]:
                    if type(k) == int:
                        if k > i:
                            index = liste[j].index(k)
                            liste[j][index] -= 1
                j+=1
            i-=2
        else:
            i-=1
    return(liste)

def elagage(file):
    liste = elagage_parsing(file)
    liste = elagage_non_terminaux(liste)
    liste = elagage_fils_unique(liste)
    #print(liste)
    liste = remonte_operateur(liste)
    #print(liste)
    elagage_reconstitution(file, liste)

def display(file,view=False):
    with open(file, 'r') as f:
        contenu_dot = f.read()
    source = Source(contenu_dot, filename=file, format="pdf")
    source.render(view=view)

### ROTATION DROITE ET GAUCHE ###
def dfs(node, tree):
    if tree[node-1][1] in ['"/"', '"*"', 'rem']:
        if len(tree[tree[node-1][3]-1]) > 3:
            if tree[tree[node-1][3]-1][1] in ['"/"', '"*"', 'rem']:
                rotate_gauche(tree, node, tree[node-1][3])
    elif tree[node-1][1] in ['"+"', '"-"']:
        if len(tree[tree[node-1][3]-1]) > 3:
            if tree[tree[node-1][3]-1][1] in ['"+"', '"-"']:
                rotate_gauche(tree, node, tree[node-1][3])
    elif tree[node-1][1] in ['or', '"or else"']:
        if len(tree[tree[node-1][3]-1]) > 3:
            if tree[tree[node-1][3]-1][1] in ['or', '"or else"']:
                rotate_gauche(tree, node, tree[node-1][3])
    elif tree[node-1][1] in ['and', '"and then"']:
        if len(tree[node-1]) > 3:
            if tree[tree[node-1][3]-1][1] in ['and', '"and then"']:
                rotate_gauche(tree, node, tree[node-1][3])
    elif tree[node-1][1] in ['ACCES','"."']:
        if len(tree[node-1]) > 3:
            if tree[tree[node-1][3]-1][1] in ['"."']:
                tree[node-1][1] = '"."'
                rotate_gauche(tree, node, tree[node-1][3])

    if len(tree[node-1]) > 2:
        for child in tree[node-1][2:]:
            dfs(child, tree)

def rotate_gauche(tree, racine, pivot):
    id_parent = get_parent(racine, tree)
    for i in range(2, len(tree[id_parent-1])):
        if tree[id_parent-1][i] == racine:
            tree[id_parent-1][i] = pivot
            tree[racine-1].remove(pivot)
            tree[racine-1].append(tree[pivot-1][2])
            tree[pivot-1].remove(tree[pivot-1][2])
            tree[pivot-1].insert(2, racine)
    if tree[pivot-1][1] in ['"/"', '"*"', 'rem']:
        if tree[tree[pivot-1][3]-1][1] in ['"/"', '"*"', 'rem']:
            rotate_gauche(tree, pivot, tree[pivot-1][3])
    elif tree[pivot-1][1] in ['"+"', '"-"']:
        if tree[tree[pivot-1][3]-1][1] in ['"+"', '"-"']:
            rotate_gauche(tree, pivot, tree[pivot-1][3])
    elif tree[pivot-1][1] in ['or', '"or else"']:
        if tree[tree[pivot-1][3]-1][1] in ['or', '"or else"']:
            rotate_gauche(tree, pivot, tree[pivot-1][3])
    elif tree[pivot-1][1] in ['and', '"and then"']:
        if tree[tree[pivot-1][3]-1][1] in ['and', '"and then"']:
            rotate_gauche(tree, pivot, tree[pivot-1][3])
    elif tree[pivot-1][1] in ['ACCES','"."']:
        if tree[tree[pivot-1][3]-1][1] in ['"."']:
            rotate_gauche(tree, pivot, tree[pivot-1][3])
    
    return tree

def get_parent(node, tree):
    for i in tree:
        if node in i[2:]:
            return i[0]
    return 0

def sup_parenthese(liste):
    i = len(liste) - 1
    while i >= 0:
        if liste[i][1] == "EXP":
            try:
                for elem in liste[i][2:]:
                    for elem2 in liste:
                        if elem2 == [elem, '"("']:
                            liste.remove(elem2)
                            liste[i].remove(elem)
                        elif elem2 == [elem, '")"']:
                            liste.remove(elem2)
                            liste[i].remove(elem)
                if len(liste[i]) == 3:
                    j = 0
                    for elem in liste:
                        if liste[i][0] in elem[1:]:
                            j = elem[0]
                            break
                    liste[j-1].remove(liste[i][0])
                    for elem in liste[i][2:]:
                        liste[j-1].append(elem)
                    liste.remove(liste[i])
            except:
                pass
        i-=1
            
    
    
##def dfs(node, tree):
##    print(tree)
##    print(node)
##    modifyed = False
##    if tree[node-1][1] == "INSTR":
##        for child in tree[node-1][2:]:
##                if tree[child-1][1] == '"/"':
##                    if tree[tree[child-1][3]-1][1] == '"*"':
##                        print("je suis passé par la")
##                        print(tree[child-1][3])
##                        print(child)
##                        rotate_gauche(node-1, tree, child, tree[child-1][3])
##                        modifyed = True
##
##                elif tree[child-1][1] == '"*"':
##                    if tree[tree[child-1][3]-1][1] == '"/"':
##                        print("je suis passé par la")
##                        print(tree[child-1][3])
##                        print(child)
##                        rotate_gauche(node-1, tree, child, tree[child-1][3])
##                        modifyed = True
##    print(tree[node-1])
##    if modifyed:
##        dfs(node, tree)
##    elif len(tree[node-1]) > 2:
##        for child in tree[node-1][2:]:
##            dfs(child, tree)
##
##
##def rotate_gauche(node, tree, racine, pivot):
##    print(tree[node])
##    print(racine)
##    print(pivot)
##    for k in range(2, len(tree[node])):
##        print("coucou")
##        print(tree[node][k])
##        if tree[node][k] == racine:
##            print("COUCOU")
##            tree[node][k] = pivot
##            tree[racine-1].remove(pivot)
##            tree[racine-1].append(tree[pivot-1][2])
##            tree[pivot-1].remove(tree[pivot-1][2])
##            tree[pivot-1].append(racine)
##    print(tree)
##    return tree
##
def compare_list_of_lists(list1, list2):
    if len(list1) != len(list2):
        return False

    for sublist1, sublist2 in zip(list1, list2):
        if sublist1 != sublist2:
            return False

    return True

def effective_rotate_gauche(file):
    liste=elagage_parsing(file)
   # print("je suis la")
   # print(liste)
    compteur = 0
    while True:
        liste_cop = []
        for elem in liste:
            liste_cop.append(elem.copy())
        dfs(1, liste)
        
        if compare_list_of_lists(liste, liste_cop) or compteur > 1000:
            break
        else:
            compteur += 1
   # print("maintenant ici")
   # print(liste)
    sup_parenthese(liste)
    elagage_reconstitution(file, liste)
    

##def rotation_reconstitution(file, liste):
##    ## Cette quatrième partie de la fonction permet de reconstituer le fichier
##    name = os.path.basename(file)
##    with open("arbre_fin.txt", 'w') as f:
##        f.write("digraph unix {\n")
##        f.write("\tnode [color=lightblue2 style=filled]\n")
##        for i in liste:
##            f.write("\t" + str(i[0]) + " [label=" + i[1] + "];\n")
##        for i in liste:
##            for j in i[2:]:
##                f.write("\t" + str(i[0]) + " -> " + str(j) + ";\n")
##        f.write("}")
##
##def parse_file(file_path):
##    with open(file_path, 'r') as f:
##        dot_content = f.read()
##
##    lines = dot_content.split('\n')
##    liste = []
##
##    for line in lines:
##        if line.strip() and ";" in line:
##            if line.strip() and "[" in line:
##                parts = line.split()
##                node_id = int(parts[0])
##                label = parts[1][7:-2]
##                liste.append([node_id, label])
##
##    return liste
##