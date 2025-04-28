# -*- coding: utf-8 -*-
# Mini Compiler - Lexical Analyzer
# Author: Mouad Erraji
# Created: 2013
# School: Ecole Mohammadia d'Ingénieurs (EMI) - Morocco
# Description: A simple lexical analyzer to tokenize expressions into identifiers, operators, and keywords.

####################################################################################################################################
####################################################################################################################################

#Matrice creuse de l'Automate

A = [1, 2, 3, 7, 7, 7, 7, 7, 7, 8, 11, 13, 15, 15, 15, 0, 0, 0, 1, 1, 2, 4, 5, 5, 4, 5, 5, 5, 6, 5, 0, 6, 9, 10, 12, 14, 0, 0]
AI = [18, 20, 21, 22, 26, 30, 32, 32, 33, 34, 34, 35, 35, 36, 36, 36]
AJ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 0, 1, 1, 3, 0, 1, 3, 15, 0, 1, 3, 15, 2, 3, 8, 10, 8, 8]

#Fonction pour voir notre matrice
def afficherMatrice():
        for i in range(16):
                for j in range(18):
                        print rechercher(i,j),'\t',
                print
                
#Structure Léxéme
'''lex = [mot, ul]'''
lex = [None, None]

#Structure Table de Symbole
'''
tableSymbole = [[lex1, lex2], [lex]]
lex1 et lex2 ont le meme hashCode
>>>Initialisation:
'''
tableSymbole = [[[None, None]]]
for i in range(39):
        tableSymbole.append([lex,])

#############################################################################################################

#Fonction de recherche dans la Matrice
def rechercher(ligne, colonne):
    trouve = 0
    if ligne == 0: 
        up = 0
        down = AI[ligne] - 1
    else:
        up = AI[ligne - 1]
        down = AI[ligne] - 1
    for x in range(up, down +1):
        if AJ[x] == colonne:
            valeur = x
            trouve = 1
    if trouve == 0:
        return -1
    else:
        return A[valeur]

##############################################################################################################

#Fonction return numero de colonne de chaque caractere
def caractereAcolonne(caractere):
    '''
    a un caractere donné, retourne la colonne correspondante
    '''
    #lettre
    if ord(caractere) in range(65, 91) or ord(caractere) in range(97, 123):
        return 0
    #chiffre
    elif ord(caractere) in range(49, 58):
        return 1
    #/
    elif ord(caractere) == 47:
        return 2
    #*
    elif ord(caractere) == 42:
        return 3
    #+
    elif ord(caractere) == 43:
        return 4
    #-
    elif ord(caractere) == 45:
        return 5
    #(
    elif ord(caractere) == 40:
        return 6
    #)
    elif ord(caractere) == 41:
        return 7
    #=
    elif ord(caractere) == 61:
        return 8
    #<
    elif ord(caractere) == 60:
        return 9
    #>
    elif ord(caractere) == 62:
        return 10
    #:
    elif ord(caractere) == 58:
        return 11
    #.
    elif ord(caractere) == 46:
        return 12
    #,
    elif ord(caractere) == 44:
        return 13
    #;
    elif ord(caractere) == 59:
        return 14
    #espace
    elif ord(caractere) == 32:
        return 15
    #\t
    elif ord(caractere) == 9:
        return 16
    #\n
    elif ord(caractere) == 10:
        return 17
    #Caractere non reconnue
    else :
        return -1
        
##############################################################################################################

#Fonction return Etat Suivant
def etatSuivant(etat, caractere):
    ligne = etat
    colonne = caractereAcolonne(caractere)
    return rechercher(ligne, colonne)

##############################################################################################################

#Fonction is Etat Final
def estFinale(etat):
    '''
    return boolean : si l'etat est final ou pas
    '''
    final = False
    if etat == 1 or etat == 2 or etat == 3 or etat == 7 or etat == 8 or etat == 9 or etat == 10 or etat == 11 or etat == 12 or etat == 14 or etat == 15:
        final = True
    return final

##############################################################################################################

#Fonction return UL
def uniteLexicale(etatFinale):
    '''
    retourn l'unite lexical selon l'etat final
    sa depend d'ou on est sortit dans l'automate
    '''
    ul = -1
    if etatFinale == 1:
        ul = 'Identificateur'
    if etatFinale == 2:
        ul = 'Nombre'
    if etatFinale == 8 or etatFinale == 9 or etatFinale == 10 or etatFinale == 11 or etatFinale == 12:
        ul = 'Operateur Logique'
    if etatFinale == 3 or etatFinale == 7:
        ul = 'Operateur Arithmetique'
    if etatFinale == 14:
        ul = 'Operateur Arithmetique'
    if etatFinale == 15:
        ul = 'Ponctuation'
    return ul

##############################################################################################################        

#Fonction Hashage du léxéme
def hashCode(mot):
    somme = 0
    i = 1
    for lettre in mot:
        somme += i * ord(lettre)
        i += 1
    h = somme % 40
    return h

##############################################################################################################

#Fonction Remplire Table des Symbole
def ajouterTableSymbole(lexeme):
    mot = lexeme[0]
    ul = lexeme[1]
    h = hashCode(mot)
    if lexeme not in tableSymbole[h] and (ul == 'Identificateur' or ul == 'Mot Clé'):
        tableSymbole[h].append(lexeme)
        if tableSymbole[h][0] == [None, None]:
            tableSymbole[h].pop(0)

#Mot Clé
motCle = ['si', 'finsi', 'fin', 'alors', 'sinon', 'debut', 'tantque', 'et', 'ou']
for mot in motCle:
        lex = [mot, 'Mot Clé']
        ajouterTableSymbole(lex)

##############################################################################################################
            
#Fonction Afficher Table des Symboles
def afficher(table):
        print
        print '_________________________________'
        print 'mot','\t','\t','unite lexicale'
        print '_____', '\t','\t','____________'
        print
        for h in table:
                for lex in h:
                        if lex[0] != None and lex[1] != None:
                                print lex[0],'\t','\t',lex[1]


##############################################################################################################
                                
#Fonction Pricipale
def main():

    expression = raw_input('Entrez votre expression = ')
    expression += ' '
    etat = 0
    mot = ''
    i = 0
    print
    while i < len(expression) :

        etatPrecedent = etat
        etat = etatSuivant(etat, expression[i])
        mot += expression[i]

        if etat == 0:
                mot = ''

        if estFinale(etatPrecedent) and (etat == -1 or expression[i] == expression[-1]):

            mot = mot[:-1]
            if mot in motCle:
                ul = 'Mot Clé'
            else :
                ul = uniteLexicale(etatPrecedent)
            
            lexeme = [mot, ul]
            ajouterTableSymbole(lexeme)
            print mot + '\t','(' + ul + ') '
            mot = ''
            etat = 0
            i -= 1
        if not estFinale(etatPrecedent) and etat == -1:
            mot = mot[:-1]
            ul = 'Mot Non Reconnu'
            print mot + '\t','(' + ul + ') '
            mot = ''
            etat = 0
            if caractereAcolonne(expression[i]) != -1:
                    i -= 1
        i += 1
    afficher(tableSymbole)
    
    
