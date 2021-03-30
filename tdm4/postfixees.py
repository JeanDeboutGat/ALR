from postfix_lexer import PostfixLexer
from sly.lex import LexError

class PostfixException(Exception) :
    pass

# analyseur lexical :
analyseur = PostfixLexer()


# memory (association ident ->  integer)
mem = dict()

def evaluate( expression, verbose = None ) :
    """
        Évalue une expression postfixée et renvoie le résultat
        
        arguments :
            expression : chaîne représentant l'expression à évaluer
            verbose : mode verbeux
            
    """

    tokens = analyseur.tokenize(expression)
    # pile d'évaluation :
    stack=[]
    #dictionnaire d'associer les entiers aux variables 
    dic  ={}
    
    try :
        for tok in tokens :
            if tok.type == 'ENTIER' :
                val = tok.value
                stack.append(val)
                print(len(stack))
            #elif tok.type == 'IDENT' :
                # ...
            #elif tok.type == 'SET' :
                # ...
            elif tok.type == 'OP2' :
                v2 = stack.pop()
                v1 = stack.pop()
                stack.append(tok.value(v1,v2))
            elif tok.type == 'OP1' :
                v = stack.pop()
                stack.append(tok.value(v))
                
            elif tok.type == 'POP' :
                v = stack.pop(len(stack)-1)
                
            elif tok.type == 'SET' :
                cle    = tok.value
                valeur = stack[len(stack)-1] 
                dic.update({cle:valeur})
                
            elif tok.type == 'IDENT' :
                key = tok.value
                stack.append (dic.get(key,0))
            
            else :
                raise PostfixException(tok, ' not implemented')
            if verbose :
                print(f'token -> {tok.type}, valeur: {tok.value}\n PILE : {stack}')
        print(len(stack))        
        res = stack.pop()
        
        if stack : # pile non vide ---> erreur
            raise PostfixException(f'Erreur, la pile devrait être vide et elle contient {stack}')

        return res
                
    except LexError as erreur :
        raise PostfixException("Erreur à l'anayse lexicale ", erreur)
    except IndexError as erreur :
        if erreur.args[0] == 'pop from empty list' :
            raise PostfixException("Erreur pile vide ", erreur)
        else :
            raise erreur