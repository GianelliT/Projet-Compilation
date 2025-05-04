from tree import *
from error_printer import error_printer

def mode(tokens, tree, parent):
    if tokens[0]==15:
        tree.add_node("in",parent)
        tokens.pop(0)
        #mode2(tokens,tree,tree.add_node("MODE2",parent))
        mode2(tokens,tree,parent)
    else:
        error_printer("mode", tokens, tree, [15])

def mode2(tokens, tree, parent):
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            pass
    elif tokens[0]==22:
        tree.add_node("out",parent)
        tokens.pop(0)
    elif tokens[0]==4:
        pass
    else:
        error_printer("mode2", tokens, tree, [1,22,4])

def modeinter(tokens, tree, parent):
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            pass
    elif tokens[0]==15:
        mode(tokens,tree,tree.add_node("MODE",parent))
    elif tokens[0]==4:
        pass
    else:
        error_printer("modeinter", tokens, tree, [1,15,4])
