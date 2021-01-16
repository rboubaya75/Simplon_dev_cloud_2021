# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:18:14 2021

@author: rboub
"""


from random import choice
from unidecode import unidecode

def word():
    f = open('mot.txt', 'r' )
    contenu = f.readlines()
    return unidecode(choice(contenu)).upper().replace('\n','')


def underscore(mot , L = []):
    r = ''
    for i in mot:
        if i in L:
            r += i + ' '
        else:
            r += '_ '
            
    return r[:-1]


def Input():
    letter = input('Please enter a letter : ')
    if letter =="" or len( letter ) > 1 or ord(letter) < 65 or ord(letter) > 122:
        return Input()

    else:
        return letter.upper()
    
    

#si la lettre est trouvée

def hangman(chance):
    
    Steps = [  
        
                   """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """
    ,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      | |
       |
    ==============
    """,
    """
    GAME OVER !
    """
    ]
    
    return Steps[chance]
    


Already_used_letters = []
word_to_find =word()
display = underscore(word_to_find  )

nb_erreurs = 0


while '_' in display and nb_erreurs < 6:
    letter = Input()
    
    if letter in word_to_find :
        word_to_find  += [ letter ]
        
    elif letter not in word_to_find :
        nb_erreurs +=1
        print(hangman(nb_erreurs ))

        
    if letter in Already_used_letters:
         Already_used_letters += [ letter ]
         print("word allready used, please try again")
        
    display = underscore(word_to_find , Already_used_letters  )
    print( '\n Word to be guessed : ' , display , ' '*6 , 'Nombre d\'erreurs maximum :' , 11-nb_erreurs )



 