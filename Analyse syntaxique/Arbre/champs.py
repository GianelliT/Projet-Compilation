from os import error
from tree import Arbre
from ident import identplus
from type import typ
from error_printer import error_printer

def champs(tokens, tree, parent):
    #identplus(tokens, tree, tree.add_node("IDENTPLUS", parent))
    identplus(tokens, tree, parent)
    if tokens[0] == 45:
        tree.add_node(":", parent)
        tokens.pop(0)
        typ(tokens, tree, tree.add_node("TYPE", parent))
        if tokens[0] == 46:
            #tree.add_node(";", parent)
            tokens.pop(0)
        else:
            error_printer("champs", tokens, tree, [46])
           
    else:
        error_printer("champs", tokens, tree, [45])
        
def champsplus(tokens, tree, parent):
    champs(tokens, tree, tree.add_node("CHAMPS", parent))
    #champsplus2(tokens, tree, tree.add_node("CHAMPSPLUS2", parent))
    champsplus2(tokens, tree, parent)

def champsplus2(tokens, tree, parent):
    if tokens[0] == 10:
        pass
    elif type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            champs(tokens, tree, tree.add_node("CHAMPS", parent))
            #champsplus2(tokens, tree, tree.add_node("CHAMPSPLUS2", parent))
            champsplus2(tokens, tree, parent)
        else:
            error_printer("champsplus2", tokens, tree, [1])
    else:
        error_printer("champsplus2", tokens, tree, [1, 10])
