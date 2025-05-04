from os import error
from tree import *
from error_printer import error_printer

def ident(tokens,tree,parent):
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            tree.add_node(tokens[0][1],parent)
            tokens.pop(0)
        else:
            error_printer("ident", tokens, tree, [1])
    else:
        error_printer("ident", tokens, tree, [1])
        
            

def identplus(tokens,tree,parent):
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            ident(tokens,tree,tree.add_node("IDENT",parent))
            #identplus2(tokens,tree,tree.add_node("IDENTPLUS2",parent))
            identplus2(tokens,tree,parent)
        else:
            error_printer("identplus", tokens, tree, [1])
    else:
        error_printer("identplus", tokens, tree, [1])
    
def identplus2(tokens,tree,parent):
    if tokens[0] == 49:
        tree.add_node(",",parent)
        tokens.pop(0)
        ident(tokens,tree,tree.add_node("IDENT",parent))
        #identplus2(tokens,tree,tree.add_node("IDENTPLUS2",parent))
        identplus2(tokens,tree,parent)
    elif tokens[0] == 45:
        pass
    else:
        error_printer("identplus2", tokens, tree, [49,45])
    
def identinter(tokens,tree,parent):
    if tokens[0] == 46:
        pass
    elif type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            ident(tokens,tree,tree.add_node("IDENT",parent))
        else:
            error_printer("identinter", tokens, tree, [1])
    else:
        error_printer("identinter", tokens, tree, [1,46])
            