#authored by Jean Debout GATARI

from sly import Lexer
from sly.lex import LexError
import operator

class PostfixLexer(Lexer):
    
    # token types :
    tokens = {IDENT, OP2, ENTIER,OP1,OP2,POP,SET}
    # token specifications :
    _entier_base_10='[1-9][0-9]*'
    _entier_base_8='0[Oo]([0-7]*_?[0-7]+)*' 
    _entier_base_16='0[xX]([0-9A-F]*_?[0-9A-F]+)*' 
    ENTIER =rf'{_entier_base_8}|{_entier_base_10}|{_entier_base_16}'
    
    #identificateur d'affectation du valeur au variable
    SET   =  '(->)([A-Za-z][A-Za-z0-9]*)'
    #un opérateur à un seul argument
    OP1 ='(opp)|(OPP)'
    #un opérateur à deux arguments
    OP2 = '(add)|(sub)|(mul)|(div)|(ADD)|(SUB)|(MUL)|(DIV)|[+-/*/]'
    #accepte les chaînespopetPOP
    POP = '(POP)|(pop)'
    #idenftifacateurs des mots [A-Za-z][A-Za-z0-9]*
    IDENT =  '[A-Za-z][A-Za-z0-9]*'
    
    
    
    #Autorisation de la présence de commentaires
    ignore_dieses_commentaires=r'(^#)(.)*'
    ignore_accolades_commentaires=r'[{][^{|^}]+[}]'
    ignore_html_tags_commentaires=r'(<!-)[^(<!-)|^(->)]+(->)'
    ignore_spaces=r'\s+'
    

    def ENTIER(self,t) :
        if (t.value.startswith("0o")or t.value.startswith("0O")):
             t.value = int(t.value,8)
        elif (t.value.startswith("0x")or t.value.startswith("0X")):
            t.value = int(t.value,16)
        else:
            t.value = int(t.value)    
        return t
    
    def OP2(self,t) :
        if   t.value == "+" or t.value == "add"  or t.value == "ADD":
             t.value=operator.add
        elif t.value == "-" or t.value == "sub"or t.value == "SUB":
             t.value=operator.sub      
        elif t.value == "*" or t.value == "mul"or t.value == "MUL":
             t.value=operator.mul
        elif t.value == "/" or t.value == "sub"or t.value == "SUB":
             t.value=operator.floordiv
        
        return t
    
    def OP1(self,t):  
        t.value = lambda x:-x;
        return t

    def SET (self,t):
        t.value = t.value[2:len(t.value)]
        return t
        
     

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
 

if __name__ == '__main__':
    
    analyseur = PostfixLexer()
    #source = 'alpha+321*x5'
    print('entrez un texte à analyser');
    source = input()
    tokenIterator = analyseur.tokenize(source)
    try :
        for tok in tokenIterator :
            print(f'token -> type: {tok.type}, valeur: {tok.value} ({type(tok.value)}), ligne : {tok.lineno}')
    except LexError as erreur :
        print("Erreur à l'anayse lexicale ", erreur)
     

