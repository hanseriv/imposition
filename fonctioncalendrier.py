#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 08:25:23 2024
@author: jean.troussier
obj : fonction necessaire au bon fonctionnement du programme de calendrier
"""
liste_valeur_possible_pour_calendrier = ['1','2','3','4','5','6','7','8','9','/','0']


def readingdate(string_to_read):
    """
    reçois string_to_read , une variable contenant l'input de l'utilisateur et renvoie une liste contenant
    chaque élément de la date comme suit [année,mois,jour] 
    il vérifie si ce dernier suis la régle de composition suivante XX/XX/XXXX 
    si ce n'est pas le cas il renvoie une liste vide
    """
    liste_de_la_date = []
    if len(string_to_read) < 10:
        return liste_de_la_date
    else :
        if '/' not in string_to_read :
            return liste_de_la_date
        if string_to_read[2] != string_to_read[5] != '/':
            return liste_de_la_date[:]
        compteur_puissance = 0
        valeur_buffer = 0
        numero_de_la_position_du_chiffre_de_la_date = -1
        while numero_de_la_position_du_chiffre_de_la_date != -len(string_to_read)-1:
            i = string_to_read[numero_de_la_position_du_chiffre_de_la_date]
            if i != '/' and i in liste_valeur_possible_pour_calendrier:
                valeur_buffer += int(i) * 10 ** compteur_puissance
                compteur_puissance += 1
            elif i not in liste_valeur_possible_pour_calendrier:
                return []
            else:
                liste_de_la_date.append(valeur_buffer)
                compteur_puissance = 0
                valeur_buffer = 0
            numero_de_la_position_du_chiffre_de_la_date -= 1
        liste_de_la_date.append(valeur_buffer)
        print(liste_de_la_date)
        return liste_de_la_date[:]
    
    
    
def number_of_day_per_months(int_mois):
    """
    reçois un int contenant le chiffre du mois (int_mois) et retourne une int contenant le nombre de jour possible (hors année bisextile)
    """
    if int_mois == 2 :
        return 28
    elif int_mois in [1,3,5,7,8,10,12] :
        return 31
    else:
        return 30
    
    
    
def is_your_year_bisextil(int_year):
    """
    reçois un int contenant l'année (int_year) et renvoie true si l'année est bisextil ou false si c le contraire
    """
    if int_year / 4 == int(int_year / 4) and int_year / 100 != int(int_year/100):
        return True
    return False
    
def is_your_date_possible(liste_de_date):
    """
    recois une liste de 3 int contenant l'année, le mois et le jour et vérifie si la date est 
    valide en retournant true si sa l'ai ou false dans le cas contraire 
    """
    if liste_de_date[1] > 12:
        return False
    number_of_day_possible = number_of_day_per_months(liste_de_date[1])
    if liste_de_date[1] == 2:
        votre_année_est_elle_bisextile = is_your_year_bisextil(liste_de_date[0])
        if votre_année_est_elle_bisextile == True:
            number_of_day_possible +=1
    if liste_de_date[2] > number_of_day_possible:
        return False
    return True
    
    
    
    
    
    