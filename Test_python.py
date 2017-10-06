#! /usr/bin/python3

import os
import pickle
from random import choice

nb_coups = 8

liste_mots = [
    "prout",
    "jonathan",
    "remi",
    "axanne",
    ]

def recup_lettre():
    lettre = input("Tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return recup_lettre()
    else:
        return lettre
    
def choisir_mot():
    
    return choice(liste_mots)

def recup_mot_masque(mot_complet, lettres_trouvees):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees :
            mot_masque +=lettre
        else:
            mot_masque += "*"
    return mot_masque

continuer_partie = 'o'

while continuer_partie != 'n':
    mot_a_trouver = choisir_mot()
    lettres_trouvees = []
    mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
    nb_chances = nb_coups
    while mot_a_trouver != mot_trouve and nb_chances > 0:
        print("Mot a trouver {0} (encore {1} chances)".format(mot_trouve, nb_chances))
        lettre = recup_lettre()
        if lettre in lettres_trouvees :
            print("Vous avez deja choisi cette lettre.")
        elif lettre in mot_a_trouver:
            lettres_trouvees.append(lettre)
            print("Bien joue !")
        else:
            nb_chances -= 1
            print("non, cette lettre ne se trouve pas dans le mot.")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
        
    if mot_a_trouver == mot_trouve:
        print("Felicitation ! Vous avez gagne !")
    else:
        print("PENDU ! Vous avez perdu !")
            
    continuer_partie = input("Shouhaitez vous continuer la partie (O/N) ?")
    continuer_partie = continuer_partie.lower()