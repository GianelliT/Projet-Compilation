from tree import *
from ident import *
from error_printer import error_printer

def typ(tokens, tree, parent):
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            ident(tokens, tree, tree.add_node("IDENT", parent))
        else:
            error_printer("typ", tokens, tree, [1])
    elif tokens[0]==4 :
        tree.add_node("access", parent)
        tokens.pop(0)
        ident(tokens, tree, tree.add_node("IDENT", parent))
    else:
        error_printer("typ", tokens, tree, [1,4])
        
