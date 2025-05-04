from tree import Arbre
from operateur import *
from error_printer import error_printer

def assigninter(tokens, tree, parent):
    if tokens[0] == 46:
        pass
    elif tokens[0] == 45:
        tree.add_node(":", parent)
        tokens.pop(0)
        if tokens[0] == 34:
            tree.add_node("=", parent)
            tokens.pop(0)
            exp(tokens, tree, tree.add_node("EXP", parent))
        else:
            error_printer("assigninter", tokens, tree, [34])
    else:
        error_printer("assigninter", tokens, tree, [45, 46])
