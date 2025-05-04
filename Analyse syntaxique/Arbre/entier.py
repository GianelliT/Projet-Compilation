from tree import Arbre
from error_printer import error_printer

def entier(tokens, tree, parent):
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 2:
            tree.add_node(tokens[0][1], parent)
            tokens.pop(0)
        else:
            error_printer("entier", tokens, tree, [2])
            
    else:
        error_printer("entier", tokens, tree, [2])