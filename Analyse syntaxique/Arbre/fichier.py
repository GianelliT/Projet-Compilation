from os import error
from tree import *
from ident import *
from decl import *
from instr import *
from error_printer import error_printer

def fichier(tokens,tree,parent):
    if tokens[0] == 33:
        tree.add_node("with",parent)
        tokens.pop(0)
        ident(tokens,tree,tree.add_node("IDENT", parent))
        if tokens[0] == 44 : 
            tree.add_node(".",parent)
            tokens.pop(0)
            ident(tokens,tree,tree.add_node("IDENT", parent))
            if tokens[0] == 46 :
                tree.add_node(";",parent)
                tokens.pop(0)
                if tokens[0] == 31 :
                    tree.add_node("use",parent)
                    tokens.pop(0)
                    ident(tokens,tree,tree.add_node("IDENT", parent))
                    if tokens[0] == 44 : 
                        tree.add_node(".",parent)
                        tokens.pop(0)
                        ident(tokens,tree,tree.add_node("IDENT", parent))
                        if tokens[0] == 46 :
                            tree.add_node(";",parent)
                            tokens.pop(0)
                            if tokens[0] == 23 :
                                tree.add_node("procedure",parent)
                                tokens.pop(0)
                                ident(tokens,tree,tree.add_node("IDENT", parent))
                                if tokens[0] == 16 :
                                    tree.add_node("is",parent)
                                    tokens.pop(0)
                                    #decletoile(tokens,tree,tree.add_node("DECLETOILE", parent))
                                    decletoile(tokens,tree,parent)
                                    if tokens[0] == 6 :
                                        tree.add_node("begin",parent)
                                        tokens.pop(0)
                                        #instrplus(tokens,tree,tree.add_node("INSTRPLUS", parent))
                                        instrplus(tokens,tree,parent)
                                        if tokens[0] == 10 :
                                            tree.add_node("end",parent)
                                            tokens.pop(0)
                                            #identinter(tokens,tree,tree.add_node("IDENTINTER", parent))
                                            identinter(tokens,tree,parent)
                                            if tokens[0] == 46 :
                                                tree.add_node(";",parent)
                                                tokens.pop(0)
                                                if len(tokens) == 0 :
                                                    tree.add_node("EOF",parent)
                                                else :
                                                    raise Exception(f"Erreur : Il reste des tokens : {tokens}")
                                            else :
                                                error_printer("fichier", tokens, tree, [46])
                                        else :
                                            error_printer("fichier", tokens, tree, [10])
                                    else :
                                        error_printer("fichier", tokens, tree, [6])
                                else :
                                    error_printer("fichier", tokens, tree, [16])
                            else :
                                error_printer("fichier", tokens, tree, [23])
                        else :
                            error_printer("fichier", tokens, tree, [46])
                    else :
                        error_printer("fichier", tokens, tree, [44])
                else :
                    error_printer("fichier", tokens, tree, [31])
            else :
                error_printer("fichier", tokens, tree, [46])
        else :
            error_printer("fichier", tokens, tree, [44])
    else :
        error_printer("fichier", tokens, tree, [33])