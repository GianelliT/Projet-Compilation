from tree import *
from instr import *
from ident import ident
from caractere import caractere
from entier import entier
from error_printer import error_printer

def op(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op1(tokens, tree, tree.add_node("OPE1", parent))
            op_prime(tokens, tree, tree.add_node("OP_PRIME", parent))
        else:
            error_printer("op", tokens, tree, [1,2,3])  
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29]:
        op1(tokens, tree, tree.add_node("OPE1", parent))
        op_prime(tokens, tree, tree.add_node("OP_PRIME", parent))
    elif tokens[0] == 19:
        tree.add_node("not", parent)
        tokens.pop(0)
        op(tokens, tree, tree.add_node("OP", parent))
    else:
        error_printer("op", tokens, tree, [1,2,3,39,47,7,18,20,11,29])

def op_prime(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [48,49,17,28,44,46]:
        pass
    elif tokens[0]==21:
        tree.add_node("or", parent)
        tokens.pop(0)
        else_op(tokens, tree, tree.add_node("ELSE", parent))
        op1(tokens, tree, tree.add_node("OPE1", parent))
        op_prime(tokens, tree, tree.add_node("OP_PRIME", parent))
    else:
        error_printer("op_prime", tokens, tree, [48,49,17,28,44,46,21])

def op1(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op2(tokens, tree, tree.add_node("OPE2", parent))
            op1_prime(tokens, tree, tree.add_node("OP1_PRIME", parent))
        else:
            error_printer("op1", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29,19]:
        op2(tokens, tree, tree.add_node("OPE2", parent))
        op1_prime(tokens, tree, tree.add_node("OP1_PRIME", parent))
    else:
       error_printer("op1", tokens, tree, [1,2,3,39,47,7,18,20,11,29])
    

def op1_prime(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [21,48,49,17,28,44,46]:
        pass
    elif tokens[0]==5:
        tree.add_node("and", parent)
        tokens.pop(0)
        then_op(tokens, tree, tree.add_node("THEN", parent))
        op2(tokens, tree, tree.add_node("OP2", parent))
        op1_prime(tokens, tree, tree.add_node("OP1_PRIME", parent))
    else:
        error_printer("op1_prime", tokens, tree, [21,48,49,17,28,44,46,5])

def op2(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op3(tokens, tree, tree.add_node("OPE3", parent))
            op2_prime(tokens, tree, tree.add_node("OP2_PRIME", parent))
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29,19]:
        op3(tokens, tree, tree.add_node("OPE3", parent))
        op2_prime(tokens, tree, tree.add_node("OP2_PRIME", parent))
    else:
        error_printer("op2", tokens, tree, [1,2,3,39,47,7,18,20,11,29])

def op2_prime(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [5,21,48,49,17,28,44,46]:
        pass
    elif tokens[0]==19:
        tree.add_node("not", parent)
        tokens.pop(0)
        op3(tokens, tree, tree.add_node("OP3", parent))
        op2_prime(tokens, tree, tree.add_node("OP2_PRIME", parent))
    else:
        error_printer("op2_prime", tokens, tree, [5,21,48,49,17,28,44,46,19])

def op3(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op4(tokens, tree, tree.add_node("OPE4", parent))
            op3_prime(tokens, tree, tree.add_node("OP3_PRIME", parent))
        else:
            error_printer("op3", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29,19]:
        op4(tokens, tree, tree.add_node("OPE4", parent))
        op3_prime(tokens, tree, tree.add_node("OP3_PRIME", parent))
    else:
        error_printer("op3", tokens, tree, [1,2,3,39,47,7,18,20,11,29])

def op3_prime(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [19,5,21,48,49,17,28,44,46]:
        pass
    elif tokens[0] in [34, 35]:
        comparateur(tokens, tree, tree.add_node("COMPARATEUR", parent))
        op4(tokens, tree, tree.add_node("OPE4", parent))
        op3_prime(tokens, tree, tree.add_node("OP3_PRIME", parent))
    else:
        error_printer("op3_prime", tokens, tree, [19,5,21,48,49,17,28,44,46,34,35])

def op4(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op5(tokens, tree, tree.add_node("OPE5", parent))
            op4_prime(tokens, tree, tree.add_node("OP4_PRIME", parent))
        else:
            error_printer("op4", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29,19]:
        op5(tokens, tree, tree.add_node("OPE5", parent))
        op4_prime(tokens, tree, tree.add_node("OP4_PRIME", parent))
    else:
        error_printer("op4", tokens, tree, [1,2,3,39,47,7,18,20,11,29])

def op4_prime(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [34,35,9,5,21,48,49,17,28,44,46]:
        pass
    elif tokens[0] in [36, 37]:
        ordre(tokens, tree, tree.add_node("ORDRE", parent))
        op5(tokens, tree, tree.add_node("OPE5", parent))
        op4_prime(tokens, tree, tree.add_node("OP4_PRIME", parent))
    else:
        error_printer("op4_prime", tokens, tree, [34,35,9,5,21,48,49,17,28,44,46,36,37])

def op5(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op6(tokens, tree, tree.add_node("OPE6", parent))
            op5_prime(tokens, tree, tree.add_node("OP5_PRIME", parent))
        else:
            error_printer("op5", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29,19]:
        op6(tokens, tree, tree.add_node("OPE6", parent))
        op5_prime(tokens, tree, tree.add_node("OP5_PRIME", parent))
    else:
        error_printer("op5", tokens, tree, [1,2,3,39,47,7,18,20,11,29])

def op5_prime(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [36,37,34,35,9,5,21,48,49,17,28,44,46]:
        pass
    elif tokens[0]==38:
        add_op(tokens, tree, tree.add_node("ADD", parent))
        op6(tokens, tree, tree.add_node("OPE6", parent))
        op5_prime(tokens, tree, tree.add_node("OP5_PRIME", parent))
    elif tokens[0]==39: # - unaire detecté comme un - binaire
        add_op(tokens, tree, tree.add_node("ADD", parent))
        op6(tokens, tree, tree.add_node("OPE6", parent))
        op5_prime(tokens, tree, tree.add_node("OP5_PRIME", parent))
    else:
        error_printer("op5_prime", tokens, tree, [36,37,34,35,9,5,21,48,49,17,28,44,46,38,39])


def op6(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op7(tokens, tree, tree.add_node("OPE7", parent))
            op6_prime(tokens, tree, tree.add_node("OP6_PRIME", parent))
        else:
            error_printer("op6", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29,19]:
        op7(tokens, tree, tree.add_node("OPE7", parent))
        op6_prime(tokens, tree, tree.add_node("OP6_PRIME", parent))
    else:
        error_printer("op6", tokens, tree, [1,2,3,39,47,7,18,20,11,29])

def op6_prime(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [38,39,36,37,34,35,9,5,21,48,49,17,28,44,46]:
        pass
    elif tokens[0] in [25, 41, 40]:
        mult_op(tokens, tree, tree.add_node("MULT", parent))
        op7(tokens, tree, tree.add_node("OPE7", parent))
        op6_prime(tokens, tree, tree.add_node("OP6_PRIME", parent))
    else:
        error_printer("op6_prime", tokens, tree, [38,39,36,37,34,35,9,5,21,48,49,17,28,44,46,25,41,40])

def op7(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op8(tokens, tree, tree.add_node("OPE8", parent))
        else:
            error_printer("op7", tokens, tree, [1,2,3])
    elif tokens[0] in [47, 7, 18, 20, 11, 29,19]:
        op8(tokens, tree, tree.add_node("OPE8", parent))
    elif tokens[0]==39:
        tree.add_node("-", parent)
        tokens.pop(0)
        op8(tokens, tree, tree.add_node("OPE8", parent))
    else:
        error_printer("op7", tokens, tree, [1,2,3,39,47,7,18,20,11,29])

def op8(tokens, tree, parent): # Verifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            #expr1(tokens, tree, tree.add_node("EXPR1", parent))
            expr1(tokens, tree, tree.add_node("EXP", parent))
        else:
            error_printer("op8", tokens, tree, [1,2,3])
    elif tokens[0] in [47, 7, 18, 20, 11, 29,19]:
        #expr1(tokens, tree, tree.add_node("EXPR1", parent))
        expr1(tokens, tree, tree.add_node("EXP", parent))
    else:
        error_printer("op8", tokens, tree, [1,2,3,47,7,18,20,11,29])

def else_op(tokens, tree, parent): # Verifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            pass
        else:
            error_printer("else_op", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29]:
        pass
    elif tokens[0]==8:
        tree.add_node("else", parent)
        tokens.pop(0)
    else:
        error_printer("else_op", tokens, tree, [1,2,3,39,47,7,18,20,11,29,8])

def then_op(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            pass
        else:
            error_printer("then_op", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29]:
        pass
    elif tokens[0]==28:
        tree.add_node("then", parent)
        tokens.pop(0)
    else:
        error_printer("then_op", tokens, tree, [1,2,3,39,47,7,18,20,11,29,28])

def comparateur(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0]==34:
        tree.add_node("=", parent)
        tokens.pop(0)
    elif tokens[0]==35:
        tree.add_node("/=", parent)
        tokens.pop(0)
    else:
        error_printer("comparateur", tokens, tree, [34,35])
        
def ordre(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0]==36:
        tree.add_node(">", parent)
        tokens.pop(0)
        egalite(tokens, tree, tree.add_node("EGALITE", parent))
    elif tokens[0]==37:
        tree.add_node("<", parent)
        tokens.pop(0)
        egalite(tokens, tree, tree.add_node("EGALITE", parent))
    else:
        error_printer("ordre", tokens, tree, [36,37])

def egalite(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1, 2, 3]:
            pass
        else:
            error_printer("egalite", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29]:
        pass
    elif tokens[0] == 34:
        tree.add_node("=", parent)
        tokens.pop(0)
    else:
        error_printer("egalite", tokens, tree, [1,2,3,39,47,7,18,20,11,29,34])

def add_op(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0]==38:
        tree.add_node("+", parent)
        tokens.pop(0)
    elif tokens[0]==39:
        tree.add_node("-", parent)
        tokens.pop(0)
    else:
        error_printer("add_op", tokens, tree, [38,39])

def mult_op(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0]==25:
        tree.add_node("rem", parent)
        tokens.pop(0)
    elif tokens[0]==41:
        tree.add_node("/", parent)
        tokens.pop(0)
    elif tokens[0]==40:
        tree.add_node("*", parent)
        tokens.pop(0)
    else:
        error_printer("mult_op", tokens, tree, [25,41,40])
        
def exp(tokens, tree, parent): # Vérifié au 21/12 
    if type(tokens[0]) == tuple:
        if tokens[0][0] in [1,2,3]:
            op(tokens, tree, tree.add_node("OP", parent))
            exacces(tokens, tree, tree.add_node("EXACCES", parent))
        else:
            error_printer("exp", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29]:
        op(tokens, tree, tree.add_node("OP", parent))
        exacces(tokens, tree, tree.add_node("EXACCES", parent))
    elif tokens[0] == 19:
        tree.add_node("not", parent)
        tokens.pop(0)
        exp(tokens, tree, tree.add_node("EXP", parent))
    else:
        error_printer("exp", tokens, tree, [1,2,3,39,47,7,18,20,11,29,19])


def exacces(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [28,46,17,49,48,45]:
        pass
    elif tokens[0] == 44:
        if type(tokens[1]) == tuple:
            if tokens[1][0] == 1:
                tree.add_node(".", parent)
                tokens.pop(0)
                ident(tokens, tree, tree.add_node("IDENT", parent))
                exacces(tokens, tree, tree.add_node("EXACCES", parent))
            else:
                error_printer("exacces", tokens[1], tree, [1])
        elif tokens[1] == 44:                      
            pass
        else:
            error_printer("exacces", tokens[1], tree, [1,44])
    else:
        error_printer("exacces", tokens, tree, [28,46,17,49,48,44])
        
def expr1(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 3:
            caractere(tokens, tree, tree.add_node("CARACTERE", parent))
        elif tokens[0][0] == 2:
            entier(tokens, tree, tree.add_node("ENTIER", parent))
        elif tokens[0][0] == 1:
            ident(tokens, tree, tree.add_node("IDENT", parent))
            #expr2(tokens, tree, tree.add_node("EXPR2", parent))
            expr2(tokens, tree, parent)
        else:
            error_printer("expr1", tokens, tree, [1,2,3])
    elif tokens[0] == 47:
        tree.add_node("(", parent)
        tokens.pop(0)
        exp(tokens, tree, tree.add_node("EXP", parent))
        if tokens[0] == 48:
            tree.add_node(")", parent)
            tokens.pop(0)
        else:
            error_printer("expr1", tokens, tree, [48])
    elif tokens[0] == 7:
        tree.add_node("Character'Val", parent)
        tokens.pop(0)
        if tokens[0] == 47:
            tree.add_node("(", parent)
            tokens.pop(0)
            exp(tokens, tree, tree.add_node("EXP", parent))
            if tokens[0] == 48:
                tree.add_node(")", parent)
                tokens.pop(0)
            else:
                error_printer("expr1", tokens, tree, [48])
        else:
            error_printer("expr1", tokens, tree, [47])
    elif tokens[0] == 18:
        tree.add_node("new", parent)
        tokens.pop(0)
        ident(tokens, tree, tree.add_node("IDENT", parent))
    elif tokens[0] == 20:
        tree.add_node("null", parent)
        tokens.pop(0)
    elif tokens[0] == 11:
        tree.add_node("false", parent)
        tokens.pop(0)
    elif tokens[0] == 29:
        tree.add_node("true", parent)
        tokens.pop(0)
    else:
        error_printer("expr1", tokens, tree, [1,2,3,47,7,18,20,11,29])
    

def expr2(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] in [34,28,25,41,40,39,38,36,37,35,19,5,21,46,17,44,49,48]:
        pass
    elif tokens[0] == 47:
        #exprplus(tokens, tree, tree.add_node("EXPRPLUS", parent))
        exprplus(tokens, tree, parent)
    else:
        error_printer("expr2", tokens, tree, [34,28,25,41,40,39,38,36,37,35,19,5,21,46,17,44,49,48,47])

        
def exprplus(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] == 47:
        tree.add_node("(", parent)
        tokens.pop(0)
        exp(tokens, tree, tree.add_node("EXP", parent))
        #exprplus2(tokens, tree, tree.add_node("EXPRPLUS2", parent))
        exprplus2(tokens, tree, parent)
        if tokens[0] == 48:
            tree.add_node(")", parent)
            tokens.pop(0)
        else:
            error_printer("exprplus", tokens, tree, [48])
    else:
        error_printer("exprplus", tokens, tree, [47])


def exprplus2(tokens, tree, parent): # Vérifié au 21/12
    if tokens[0] == 49:
        tree.add_node(",", parent)
        tokens.pop(0)
        exp(tokens, tree, tree.add_node("EXP", parent))
        #exprplus2(tokens, tree, tree.add_node("EXPRPLUS2", parent))
        exprplus2(tokens, tree, parent)
    elif tokens[0] == 48:
        pass
    else:
        error_printer("exprplus2", tokens, tree, [49,48])
    
def exprinter(tokens, tree, parent): # Vérifié au 21/12
    if type(tokens[0]) == tuple:
        if tokens[0][0] == 3 or tokens[0][0] == 2 or tokens[0][0] == 1:
            exp(tokens, tree, tree.add_node("EXP", parent))
        else:
            error_printer("exprinter", tokens, tree, [1,2,3])
    elif tokens[0] in [39, 47, 7, 18, 20, 11, 29]:
        exp(tokens, tree, tree.add_node("EXP", parent))
    elif tokens[0] == 46:
        pass
    else:
        error_printer("exprinter", tokens, tree, [1,2,3,39,47,7,18,20,11,29,46])