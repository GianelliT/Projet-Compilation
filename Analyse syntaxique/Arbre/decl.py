from tree import Arbre
from ident import ident, identinter, identplus
from params import param, paramsinter
from type import typ
from champs import champsplus
from instr import instr, instrplus
from assign import assigninter
from error_printer import error_printer



def decl(tokens, tree, parent):
    if tokens[0] == 30:
        tree.add_node("type", parent)
        tokens.pop(0)
        ident(tokens, tree, tree.add_node("IDENT", parent))
        #decl1(tokens, tree, tree.add_node("DECL1", parent))
        decl1(tokens, tree, parent)
    elif tokens[0] == 13:
        tree.add_node("function", parent)
        tokens.pop(0)
        ident(tokens, tree, tree.add_node("IDENT", parent))
        #paramsinter(tokens, tree, tree.add_node("PARAMSINTER", parent))
        paramsinter(tokens, tree, parent)
        if tokens[0] == 26:
            tree.add_node("return", parent)
            tokens.pop(0)
            typ(tokens, tree, tree.add_node("TYPE", parent))
            if tokens[0] == 16:
                tree.add_node("is", parent)
                tokens.pop(0)
                #decletoile(tokens, tree, tree.add_node("DECLETOILE", parent))
                decletoile(tokens, tree, parent)
                if tokens[0] == 6:
                    tree.add_node("begin", parent)
                    tokens.pop(0)
                    #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
                    instrplus(tokens, tree, parent)
                    if tokens[0] == 10:
                        tree.add_node("end", parent)
                        tokens.pop(0)
                        #identinter(tokens, tree, tree.add_node("IDENTINTER", parent))
                        identinter(tokens, tree, parent)
                        if tokens[0] == 46:
                            #tree.add_node(";", parent)
                            tokens.pop(0)
                        else:
                            error_printer("decl", tokens, tree, [46])
                            
                    else:
                        error_printer("decl", tokens, tree, [10])
                else:
                    error_printer("decl", tokens, tree, [6])
            else:
                error_printer("decl", tokens, tree, [16])
        else:
            error_printer("decl", tokens, tree, [26])
    elif tokens[0] == 23:
        tree.add_node("procedure", parent)
        tokens.pop(0)
        ident(tokens, tree, tree.add_node("IDENT", parent))
        #paramsinter(tokens, tree, tree.add_node("PARAMSINTER", parent))
        paramsinter(tokens, tree, parent)
        if tokens[0] == 16:
            tree.add_node("is", parent)
            tokens.pop(0)
            #decletoile(tokens, tree, tree.add_node("DECLETOILE", parent))
            decletoile(tokens, tree, parent)
            if tokens[0] == 6:
                tree.add_node("begin", parent)
                tokens.pop(0)
                #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
                instrplus(tokens, tree, parent)
                if tokens[0] == 10:
                    tree.add_node("end", parent)
                    tokens.pop(0)
                    #identinter(tokens, tree, tree.add_node("IDENTINTER", parent))
                    identinter(tokens, tree, parent)
                    if tokens[0] == 46:
                        #tree.add_node(";", parent)
                        tokens.pop(0)
                    else:
                        error_printer("decl", tokens, tree, [46])
                else:
                    error_printer("decl", tokens, tree, [10])
            else:
                error_printer("decl", tokens, tree, [6])
        else:
            error_printer("decl", tokens, tree, [16])
    elif type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            #identplus(tokens, tree, tree.add_node("IDENTPLUS", parent))
            identplus(tokens, tree, parent)
            if tokens[0] == 45:
                tree.add_node(":", parent)
                tokens.pop(0)
                typ(tokens, tree, tree.add_node("TYPE", parent))
                #assigninter(tokens, tree, tree.add_node("ASSIGNINTER", parent))
                assigninter(tokens, tree, parent)
                if tokens[0] == 46:
                    #tree.add_node(";", parent)
                    tokens.pop(0)
                else:
                    error_printer("decl", tokens, tree, [46])
            else:
                error_printer("decl", tokens, tree, [45])
        else:
            error_printer("decl", tokens, tree, [1])
    else:
        error_printer("decl", tokens, tree, [1, 13, 23, 30])
                
def decl1(tokens, tree, parent):
    if tokens[0] == 46:
        #tree.add_node(";", parent)
        tokens.pop(0)
    elif tokens[0] == 16:
        tree.add_node("is", parent)
        tokens.pop(0)
        #decl2(tokens, tree, tree.add_node("DECL2", parent))
        decl2(tokens, tree, parent)
    else:
        error_printer("decl1", tokens, tree, [46, 16])

    
def decl2(tokens, tree, parent):
    if tokens[0] == 4:
        tree.add_node("access", parent)
        tokens.pop(0)
        ident(tokens, tree, tree.add_node("IDENT", parent))
        if tokens[0] == 46:
            #tree.add_node(";", parent)
            tokens.pop(0)
        else:
            error_printer("decl2", tokens, tree, [46])
    elif tokens[0] == 24:
        tree.add_node("record", parent)
        tokens.pop(0)
        #champsplus(tokens, tree, tree.add_node("CHAMPSPLUS", parent))
        champsplus(tokens, tree, parent)
        if tokens[0] == 10:
            tree.add_node("end", parent)
            tokens.pop(0)
            if tokens[0] == 24:
                tree.add_node("record", parent)
                tokens.pop(0)
                if tokens[0] == 46:
                    #tree.add_node(";", parent)
                    tokens.pop(0)
                else:
                    error_printer("decl2", tokens, tree, [46])
            else:
                error_printer("decl2", tokens, tree, [24])
        else:
            error_printer("decl2", tokens, tree, [10])
    else:
        error_printer("decl2", tokens, tree, [4, 24])
                
def decletoile(tokens, tree, parent):
    if tokens[0] == 6:
        pass
    elif type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            decl(tokens, tree, tree.add_node("DECL", parent))
            #decletoile(tokens, tree, tree.add_node("DECLETOILE", parent))
            decletoile(tokens, tree, parent)
        else:
            error_printer("decletoile", tokens, tree, [1])
    elif tokens[0] == 13 or tokens[0] == 23 or tokens[0] == 30:
        decl(tokens, tree, tree.add_node("DECL", parent))
        #decletoile(tokens, tree, tree.add_node("DECLETOILE", parent))
        decletoile(tokens, tree, parent)
    else:
        error_printer("decletoile", tokens, tree, [6, 13, 23, 30, 1])

def decletoile2(tokens, tree, parent):
    if tokens[0] == 6:
        pass
    elif type(tokens[0]) == tuple:
        if tokens[0][0] == 1:
            decl(tokens, tree, tree.add_node("DECL", parent))
            #decletoile(tokens, tree, tree.add_node("DECLETOILE", parent))
            decletoile(tokens, tree, parent)
        else:
            error_printer("decletoile2", tokens, tree, [1])
    elif tokens[0] == 13 or tokens[0] == 23 or tokens[0] == 30:
        decl(tokens, tree, tree.add_node("DECL", parent))
        #decletoile(tokens, tree, tree.add_node("DECLETOILE", parent))
        decletoile(tokens, tree, parent)
        return (tokens, tree)
    else:
        error_printer("decletoile2", tokens, tree, [6, 13, 23, 30, 1])