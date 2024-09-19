"""
user : Jean TROUSSIER
date : jeudi 19 septembre
objectif : fonction principale de la gestion d'impot
ToDo : interface, fonction de traitement du montant a payer, des tranches)
"""
import fonctionimpot as fi
print("please input your salary")
reponse = input("repones utilisateur :")
argent_perdu = fi.impot_a_calc(reponse)
if argent_perdu == -1:
    print("veuiller entrée une donnée valide")
else :
    print("vous devez : ", argent_perdu," d'euro")