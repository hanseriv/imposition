"""
user : Jean TROUSSIER
date : jeudi 19 septembre
objectif : fonction de la gestion d'impot
ToDo : interface, fonction de traitement du montant a payer, des tranches)
"""
liste_de_tranche = [[0,10225],[10226,26070],[26071,74545],[75546,160336]]
liste_des_cote = [0,11,30,41,45]

def verif_input(input):
    try:
        float(input)
    except:
        return False
    return True

def tranche(float_salaire):
    """
    fonction qui a pour entrée un int contenant le salaire de salarié et qui retourne sa cote, en int
    """
    cat = 0
    for i in liste_de_tranche:
        if int_salaire > i[1]:
            cat +=1
        else:
            return cat
    return cat

def impot_a_calc(int_salaire):
    if verif_input(int_salaire) == False:
        return -1
    cat = tranche(int_salaire) 
    if cat <= liste_de_tranche[0][1]:
        return 0
    else:
        return (int_salaire - liste_de_tranche[cat - 1] + 1) *  liste_des_cote[cat] / 100