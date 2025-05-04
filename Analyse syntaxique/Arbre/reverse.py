from tree import *
from error_printer import error_printer

def reverseinter(tokens, tree, parent):
    if tokens[0]==27:
        tree.add_node("reverse", parent)
        tokens.pop(0)
    elif type(tokens[0])==tuple:
        if tokens[0][0] in [1,2,3]:
            pass
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29]:
        pass
    else: 
        error_printer("reverseinter", tokens, tree, [27,1,2,3,39,47,7,18,20,11,29])
