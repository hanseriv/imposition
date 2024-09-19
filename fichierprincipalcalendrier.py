# -*- coding: utf-8 -*-
"""
user : Jean TROUSSIER
date : jeudi 19 septembre
objectif : calendrier
ToDo : gestion 
"""
import fonctioncalendrier as fc

recu_texte = input("votre date ?")
liste_de_date = fc.readingdate(recu_texte)
while liste_de_date == []:
    print("veuillez respectez la mise en forme suivante : \'xx/xx/xxxx\'")
    recu_texte = input("votre date ?")
    liste_de_date = fc.readingdate(recu_texte)
is_ur_date_correct = fc.is_your_date_possible(liste_de_date[:])
if is_ur_date_correct == True:
    print("vous avez rentrée une date valide")
else:
    print("la date rentrée est incorrecte..")
#heelo bande de con