"""
user : Jean TROUSSIER
date : jeudi 19 septembre
objectif : fonction de la gestion d'impot
ToDo : interface, fonction de traitement du montant a payer, des tranches)
"""
liste_de_tranche = [[0,10225],[10226,26070],[26071,74545],[75546,160336]]
liste_des_cote = [0,11,30,41,45]

def montant_a_payer(int_salaire):
    """
    fonction qui a pour entrée un int contenant le salaire de salarié et qui retourne sa cote, en int
    """
