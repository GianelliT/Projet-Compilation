from operateur import *
from ident import *
from reverse import *
from operateur import *
from tree import *
from error_printer import error_printer

def instr(tokens,tree,parent): # Vérifié au 21/12
    if type(tokens[0])==tuple:
        if tokens[0][0] in [3,2]:
            #exp(tokens, tree, tree.add_node("EXP", parent))
            op(tokens, tree, tree.add_node("OP", parent))
            #instr2(tokens, tree,tree.add_node("INSTR2", parent))
            if tokens[0]==44:
                tree.add_node(".", parent)
                tokens.pop(0)
                ident(tokens, tree, tree.add_node("IDENT", parent))
                instr2(tokens, tree, parent)
            elif tokens[0]==46:
                #tree.add_node(";", parent)
                tokens.pop(0)
            else:
                error_printer("instr", tokens, tree, [44, 46])                
        elif tokens[0][0] == 1:
            parent2 = tree.add_node("ACCES", parent)
            while True:
                if type(tokens[0]) == tuple:
                    if tokens[0][0] == 1:
                        if tokens[1] == 45:
                            ident(tokens, tree, tree.add_node("IDENT", parent2))
                            #instr2(tokens, tree, tree.add_node("INSTR2", parent))
                            instr2(tokens, tree, parent)
                            break
                        else:
                            op(tokens, tree, tree.add_node("OP", parent2))
                            if tokens[0]==44:
                                parent2 = tree.add_node(".", parent2)
                                tokens.pop(0)
                            elif tokens[0]==46:
                                #tree.add_node(";", parent2)
                                tokens.pop(0)
                                break
                    else:
                        op(tokens, tree, tree.add_node("OP", parent2))
                        if tokens[0]==44:
                            parent2 = tree.add_node(".", parent2)
                            tokens.pop(0)
                        elif tokens[0]==46:
                            #tree.add_node(";", parent2)
                            tokens.pop(0)
                            break
                else:
                    op(tokens, tree, tree.add_node("OP", parent2))
                    if tokens[0]==44:
                        parent2 = tree.add_node(".", parent2)
                        tokens.pop(0)
                    elif tokens[0]==46:
                        #tree.add_node(";", parent2)
                        tokens.pop(0)
                        break

    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29,19]:
        parent2 = tree.add_node("ACCES", parent)
        while True:
            if type(tokens[0]) == tuple:
                if tokens[0][0] == 1:
                    if tokens[1] == 45:
                        ident(tokens, tree, tree.add_node("IDENT", parent2))
                        #instr2(tokens, tree, tree.add_node("INSTR2", parent))
                        instr2(tokens, tree, parent)
                        break
                    else:
                        op(tokens, tree, tree.add_node("OP", parent2))
                        if tokens[0]==44:
                            parent2 = tree.add_node(".", parent2)
                            tokens.pop(0)
                else:
                    op(tokens, tree, tree.add_node("OP", parent2))
                    if tokens[0]==44:
                        parent2 = tree.add_node(".", parent2)
                        tokens.pop(0)
            else:
                op(tokens, tree, tree.add_node("OP", parent))
                if tokens[0]==44:
                    tree.add_node(".", parent)
                    tokens.pop(0)
    elif tokens[0]==12:
        tree.add_node("for", parent)
        tokens.pop(0)
        ident(tokens, tree, tree.add_node("IDENT", parent))
        if tokens[0] == 15:
            tree.add_node("in", parent)
            tokens.pop(0)
            #reverseinter(tokens, tree, tree.add_node("REVERSEINTER", parent))
            reverseinter(tokens, tree, parent)
            exp(tokens, tree, tree.add_node("EXP", parent))
            if tokens[0] == 44:
                tree.add_node(".", parent)
                tokens.pop(0)
                if tokens[0] == 44:
                    tree.add_node(".", parent)
                    tokens.pop(0)
                    exp(tokens, tree, tree.add_node("EXP", parent))
                    if tokens[0] == 17:
                        tree.add_node("loop", parent)
                        tokens.pop(0)
                        #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
                        instrplus(tokens, tree, parent)
                        if tokens[0] == 10:
                            tree.add_node("end", parent)
                            tokens.pop(0)
                            if tokens[0] == 17:
                                tree.add_node("loop", parent)
                                tokens.pop(0)
                                if tokens[0] == 46:
                                    #tree.add_node(";", parent)
                                    tokens.pop(0)
                                else:
                                    error_printer("instr", tokens, tree, [46])
                            else:
                                error_printer("instr", tokens, tree, [17])
                        else:
                            error_printer("instr", tokens, tree, [10])
                    else:
                        error_printer("instr", tokens, tree, [17])
                else:
                    error_printer("instr", tokens, tree, [44])
            else:
                error_printer("instr", tokens, tree, [44])
        else:
            error_printer("instr", tokens, tree, [15])
    elif tokens[0]==14:
        tree.add_node("if", parent)
        tokens.pop(0)
        exp(tokens, tree, tree.add_node("EXP", parent))
        if tokens[0]==28:
            tree.add_node("then", parent)
            tokens.pop(0)
            #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
            instrplus(tokens, tree, parent)
            #elsifetoile(tokens, tree, tree.add_node("ELSIFETOILE", parent))
            elsifetoile(tokens, tree, parent)
            #elseinter(tokens, tree, tree.add_node("ELSEINTER", parent))
            elseinter(tokens, tree, parent)
            if tokens[0]==10:
                tree.add_node("end", parent)
                tokens.pop(0)
                if tokens[0]==14:
                    tree.add_node("if", parent)
                    tokens.pop(0)
                    if tokens[0]==46:
                        #tree.add_node(";", parent)
                        tokens.pop(0)
                    else:
                        error_printer("instr", tokens, tree, [46])
                else:
                    error_printer("instr", tokens, tree, [14])
            else:
                error_printer("instr", tokens, tree, [10])
        else:
            error_printer("instr", tokens, tree, [28])
        
    elif tokens[0]==32:
        tree.add_node("while", parent)
        tokens.pop(0)
        exp(tokens, tree, tree.add_node("EXP", parent))
        if tokens[0]==17:
            tree.add_node("loop", parent)
            tokens.pop(0)
            #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
            instrplus(tokens, tree, parent)
            if tokens[0]==10:
                tree.add_node("end", parent)
                tokens.pop(0)
                if tokens[0]==17:
                    tree.add_node("loop", parent)
                    tokens.pop(0)
                    if tokens[0]==46:
                        #tree.add_node(";", parent)
                        tokens.pop(0)
                    else:
                        error_printer("instr", tokens, tree, [46])
                else:
                    error_printer("instr", tokens, tree, [17])
            else:
                error_printer("instr", tokens, tree, [10])
        else:
            error_printer("instr", tokens, tree, [17])
    elif tokens[0]==6:
        tree.add_node("begin", parent)
        tokens.pop(0)
        #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
        instrplus(tokens, tree, parent)
        if tokens[0]==10:
            tree.add_node("end", parent)
            tokens.pop(0)
            if tokens[0]==46:
                #tree.add_node(";", parent)
                tokens.pop(0)
            else:
                error_printer("instr", tokens, tree, [46])
        else:
            error_printer("instr", tokens, tree, [10])
    elif tokens[0]==26:
        tree.add_node("return", parent)
        tokens.pop(0)
        #exprinter(tokens, tree, tree.add_node("EXPRINTER", parent))
        exprinter(tokens, tree, parent)
        if tokens[0]==46:
            #tree.add_node(";", parent)
            tokens.pop(0)
        else:
            error_printer("instr", tokens, tree, [46])
    else:
        error_printer("instr", tokens, tree, [39, 47, 7, 18, 20, 11, 29, 12, 14, 32, 6, 26])

def instr2(tokens,tree,parent): # Vérifié au 21/12
    if tokens[0] == 47:
        #exprplus(tokens, tree, tree.add_node("EXPRPLUS", parent))
        exprplus(tokens, tree, parent)
        if tokens[0]==46:
            #tree.add_node(";", parent)
            tokens.pop(0)
        else:
            error_printer("instr2", tokens, tree, [46])
    elif tokens[0]==45:
        tree.add_node(":", parent)
        tokens.pop(0)
        if tokens[0]==34:
            tree.add_node("=", parent)
            tokens.pop(0)
            exp(tokens, tree, tree.add_node("EXP", parent))
            if tokens[0]==46:
                #tree.add_node(";", parent)
                tokens.pop(0)
            else:
                error_printer("instr2", tokens, tree, [46])
        else:
            error_printer("instr2", tokens, tree, [34])
            
    elif tokens[0]==46:
        #tree.add_node(";", parent)
        tokens.pop(0)
    else:
        error_printer("instr2", tokens, tree, [47, 45, 46])

def instrplus(tokens,tree,parent): # Vérifié au 21/12
    if type(tokens[0])==tuple:
        if tokens[0][0] in [3,2,1]:
            instr(tokens, tree, tree.add_node("INSTR", parent))
            #instrplus2(tokens, tree, tree.add_node("INSTRPLUS2", parent))
            instrplus2(tokens, tree, parent)
    elif tokens[0] in [39, 12, 32, 14, 26, 47, 7, 18, 20, 11, 29, 6, 19]:
        instr(tokens, tree, tree.add_node("INSTR", parent))
        #instrplus2(tokens, tree, tree.add_node("INSTRPLUS2", parent))
        instrplus2(tokens, tree, parent)
    else:
        error_printer("instrplus", tokens, tree, [39, 12, 32, 14, 26, 47, 7, 18, 20, 11, 29, 6, 3, 2, 1])

def instrplus2(tokens,tree,parent): # Vérifié au 21/12
    if type(tokens[0])==tuple:
        if tokens[0][0] in [3,2,1]:
            #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
            instrplus(tokens, tree, parent)
    elif tokens[0] in [39, 12, 32, 14, 26, 47, 7, 18, 20, 11, 29, 6, 19]:
        #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
        instrplus(tokens, tree, parent)
    elif tokens[0] in [8, 9, 10]:
        pass
    else:
        error_printer("instrplus2", tokens, tree, [39, 12, 32, 14, 26, 47, 7, 18, 20, 11, 29, 6, 3, 2, 1, 8, 9, 10])

def elseinter(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0]==8:
        tree.add_node("else", parent)
        tokens.pop(0)
        #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
        instrplus(tokens, tree, parent)
    elif tokens[0]==10:
        pass
    else:
        error_printer("elseinter", tokens, tree, [8, 10])

def elsifetoile(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [8, 10]:
        pass
    elif tokens[0]==9:
        tree.add_node("elsif", parent)
        tokens.pop(0)
        exp(tokens, tree, tree.add_node("EXP", parent))
        if tokens[0]==28:
            tree.add_node("then", parent)
            tokens.pop(0)
            #instrplus(tokens, tree, tree.add_node("INSTRPLUS", parent))
            instrplus(tokens, tree, parent)
            #elsifetoile(tokens, tree, tree.add_node("ELSEIF*", parent))
            elsifetoile(tokens, tree, parent)
        else:
            error_printer("elsifetoile", tokens, tree, [28])
    else:
        error_printer("elsifetoile", tokens, tree, [8, 10, 9])
            