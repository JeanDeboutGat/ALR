
# Auteur: Jean Debout Gatari
----------------------------

# REPONSES  TDM1
--------------



 Question1: Mots composés de lettres (ASCII, donc non accentuées) majuscules ou minuscule, et commençant nécessairement par une majuscule
------------------------------------------------------------------------------------------------------------------------------------------

### Expression: [A-Z][A-Za-z]*
    Aee2	    ko
    Aé	        ko
    Aabcddfeee	ko
    Aaaaaaaaaa  ko
    Aa	        ok
    HELLo       ok  
    aaaaaaa	    ko
    a	        ko
    (eps        ko

Question2: Les numéros de téléphone en France, au format international
----------------------------------------------------------------------

### Expression: [+][3]{2}[1-9][0-9]{8}

    +33214363278	ok
    +33664363278	ok
    +33664363274	ok
    +33064363274	ko
    +23664363274	ko
    +33664363274	ko

Question3: les identifiants de départementfrançais.
---------------------------------------------------

### Expression: [0][1-9]|[1][0-9]|[2][1-9]|[3-8][0-9]|[9][0-5]|[9][7][1-6]|[2][AB]

    2c	ko
    2C	ko
    2AB	ko
    2	ko
    2A	ok
    977	ko
    976	ok
    100	ko
    1	ko
    96	ko
    95	ok
    21	ok
    20	ko
    19	ok
    01	ok
    00	ko
    e	ko
    0	ko
Question4 les identificateurscommençant par une lettre, et pouvant comporter lettres, chiffres et underscore
------------------------------------------------------------------------------------------------------------

### Expression: [A-Za-z]([A-Za-z]|[0-9])*(_?)([A-Za-z]|[0-9])+

    h       	ko
    heLLo_14	ok
    heLLo__o	ko
    _heLLo	    ko
    heLL_o	    ok


Question 5: les nombres entiers en Java
-----------------------------------------
### Expression: 0(x([0-9A-F]*_?[0-9A-F]+)*|o([0-7]*_?[0-7]+)*)|([0-9]*_?[0-9]+)*

Mot                     Résultat

0o012345678             ko
0o01234567              ok
0o0123456789ABCDEF      ko
0x0123456789ABCDEF__F   ko
0x0123456789ABCDEF      ok




Question 6: les listes d’identificateurs séparés par une virgule
------------------------------------------------------------------
### Expression: `*(( *[A-Za-z](([A-Za-z]|[0-9])*(_?)([A-Za-z]|[0-9])+)* *)(,( *[A-Za-z](([A-Za-z]|[0-9])*(_?)([A-Za-z]|[0-9])+)* *))?)*`

 Mot           Résultat 
------------------------
,Test , ament  ko       
Test , ament,  ko       
Test , ament   ok       
Test,ament     ok       
Test,	        ko       
Test_	        ko       
T__est	        ko       
T_est	        ok       
Test	        ok       

Question 7: les littéraux chaînes de caractères (version 1)
------------------------------------------------------------
### Expression : `"([^"]*)"`


 Mot    Résultat 
-----------------
""""a	 ko       
"""a"	 ok       
""a""	 ko       
"a"""	 ok       
""""	 ok       
"ab""c"  ok       

Question 8: les littéraux chaînes de caractères (version 2)
------------------------------------------------------------
### Expression : `("([^"]*)")*`

 Mot       Résultat 
--------------------
""""a	    ko       
"""a"	    ok       
""a""	    ko       
"a"""	    ok       
""""        ok       
"ab""c"     ok       



Question 9: les littéraux chaînes de caractères (version 3)
------------------------------------------------------------
### Expression : `("(([^"\\]*(\\(\\|"))?[^"\\]*)*)")*`


 Mot       Résultat 
--------------------
"\\\"	    ko       
"a\"	    ko       
"a\c"	    ko       
"a"b"	    ko       
"a\\b\"c"  ok       
"\\\""	    ok       

-Question 10: Noms XML
-----------------------
### Expression : `[A-Za-z:_][A-Za-z:\-_0-9\.]*`


 Mot        Résultat 
---------------------
_test.:-_"  ko       
_test.:-_   ok       
_	        ok       
:	        ok       
a	        ok       

-Question 11: Réferences d’entité XML
--------------------------------------
### Expression : `&[A-Za-z:_]?[A-Za-z:\-_0-9\.]*;`


 Mot           Résultat 
------------------------
&_test;&grtg;   ko       
_test;	        ko       
&_test;         ok       
&_test	        ko       
_test	        ko       

-Question 12: Valeurs d’attribut en XML
---------------------------------------
### Expression : `"&?[^<&"]*"`


 Mot     Résultat 
------------------
"test>"  ok       
"test<"  ko       
"test""  ko       
"test&"  ko       
"test"	  ok       
"&test"  ok       
""	  ok       


Question 13: Balises ouvrantes XML
------------------------------------
### Expression : `<([A-Za-z:_][A-Za-z:\-_0-9\.]*)( +[a-z]* *= *"&?[^<&"]*")* *>`


 Mot                                                 Résultat 
--------------------------------------------------------------
`<balise attribut="valeur" attributdeux = "valeur2">` 	 ok      
`<balise attribut="valeur" attributdeux="valeur2" >`  	 ok      
`< balise attribut="valeur" attributdeux="valeur2">`  	 ko      
`<balise attribut="valeur" attributdeux="valeur2">`   	 ok      
`<balise attribut="v&aleur">`			                 ko      
`<balise attribut="&valeur">`			                 ok      
`<balise attribut="valeur">`			                 ok      
`<balise attribut=valeur>`			                     ko      
`<balise attribut=>`				                     ko      
`<balise attribut>`				                         ko      
`<balise>`					                             ok   
