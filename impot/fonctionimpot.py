"""
user : Jean TROUSSIER
date : jeudi 19 septembre
objectif : fonction de la gestion d'impot
ToDo : interface, fonction de traitement du montant a payer, des tranches)
"""
liste_de_tranche = [[0,10225],[10226,26070],[26071,74545],[75546,160336]]
liste_des_cote = [0,11,30,41,45]



def verif_input(input):
    """
    fonction qui prend comme paramèter une float et qui renvoie true si c une float ou false si ce n'est pas le cas
    """
    try:
        float(input)
    except:
        return False
    return True

def tranche(float_salaire):
    """
    fonction qui a pour entrée une float contenant le salaire de salarié et qui retourne sa cote, en int
    """
    cat = 0
    for i in liste_de_tranche:
        if float_salaire > i[1]:
            cat +=1
        else:
            return cat
    return cat

def impot_a_calc(int_salaire):
    """
    fonction qui prend en entrée une floatante , le salaire et qui renvoie sous forme de floatante, l'impot a payer
    """
    if verif_input(int_salaire) == False:
        return -1
    int_salaire = float(int_salaire)
    cat = tranche(int_salaire) 
    print(cat)
    if int_salaire <= liste_de_tranche[0][1]:
        return 0
    else:
        return (int_salaire - liste_de_tranche[cat - 1][1] + 1) *  liste_des_cote[cat] / 100