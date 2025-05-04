from tree import *
from ident import *
from mode import *
from type  import *
from error_printer import error_printer

def params(tokens, tree, parent):
    if tokens[0]==47:
        #tree.add_node("(", parent)
        tokens.pop(0)
        #paramplus(tokens, tree, tree.add_node("PARAMPLUS", parent))
        paramplus(tokens, tree, parent)
        if tokens[0]==48:
            #tree.add_node(")", parent)
            tokens.pop(0)
        else: 
            error_printer("params", tokens, tree, [48])
    else:
        error_printer("params", tokens, tree, [47])

def paramsinter(tokens, tree, parent):
    if tokens[0]==47:
        params(tokens, tree, tree.add_node("PARAMS", parent))
    elif tokens[0] in [26,16]:
        pass
    else:
        error_printer("paramsinter", tokens, tree, [47,26,16])

def param(tokens, tree, parent):
    if type(tokens[0])==tuple:
        if tokens[0][0] == 1:
            #identplus(tokens, tree, tree.add_node("IDENTPLUS", parent))
            identplus(tokens, tree, parent)
            if tokens[0]==45:
                tree.add_node(":", parent)
                tokens.pop(0)
                #modeinter(tokens, tree, tree.add_node("MODEINTER", parent))
                modeinter(tokens, tree, parent)
                typ(tokens, tree, tree.add_node("TYPE", parent))
            else:
                error_printer("param", tokens, tree, [45])
        else:
            error_printer("param", tokens, tree, [1])
    else:
        error_printer("param", tokens, tree, [1])

def paramplus(tokens, tree, parent):
    if type(tokens[0])==tuple:
        if tokens[0][0] == 1:
            param(tokens, tree, tree.add_node("PARAM", parent))
            #paramplus2(tokens, tree, tree.add_node("PARAMPLUS2", parent))
            paramplus2(tokens, tree, parent)
        else:
            error_printer("paramplus", tokens, tree, [1])
    else:
        error_printer("paramplus", tokens, tree, [1])

def paramplus2(tokens, tree, parent):
    if tokens[0]==46:
        #tree.add_node(";", parent)
        tokens.pop(0)
        param(tokens, tree, tree.add_node("PARAM", parent))
        #paramplus2(tokens, tree, tree.add_node("PARAMPLUS2", parent))
        paramplus2(tokens, tree, parent)
    elif tokens[0]==48:
        pass
    else: 
        error_printer("paramplus2", tokens, tree, [46,48])