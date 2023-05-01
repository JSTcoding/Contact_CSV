#coding:utf-8

import os
import re
import csv

os.system("clear") # import du module OS - execute la fonction shell [clear] qui efface le terminal

print()
print("Ce programme permet d'enregistrer des contacts à la chaîne \net d'enregistrer les données dans un fichier txt ou csv.")
print()
#info_str = ("")
#ifile = ("")  # Initialisation de la variable ifile à une chaîne vide

############# CREATION NOUVEAU FICHIER ########################################
def new():
     global ifile  # Déclaration de ifile comme variable globale pour pouvoir la modifier dans la fonction
     ifile = input("Entrer le nom de fichier à créer avec son extension (exemple: 'contact_pro.csv'): ")
     colon= ("Nom , Prénom , Entreprise , Adresse mail , Téléphone\n") # Crée la première ligne du fichier avec les en-têtes de colonnes
     with open( ifile , "a") as f:    ## "a" = append = ajouter à la suite / "w" = whrite = créer un nouveau fichier
        f.write(colon)

############# MODIFICATION FICHIER EXISTANT ###################################
def exist():
     global ifile  # Déclaration de ifile comme variable globale pour pouvoir la modifier dans la fonction
     ifile = input("Entrer le nom de fichier à compléter avec son extension (exemple: 'contact_pro.csv'): ")
     empty = (" \n")
     with open( ifile , "a") as f:
         f.write(empty) 
                  

# Fonction qui demande à l'utilisateur de saisir ses informations personnelles
def saisie():
    print("\n Saisir le contact \n" )
    nom = input("Nom du contact : ")
    while not re.match(r'^[A-Za-zéèêëïîôöùüç\-\s]+$', nom):
        print("Le nom ne doit contenir que des lettres, des tirets, des espaces et les caractères é,è,ê,ë,ï,î,ô,ö,ù,ü,ç.")
        nom = input("Nom du contact : ")

    prenom = input("Prénom du contact : ")
    while not re.match(r'^[A-Za-zéèêëïîôöùüç\-\s]+$', prenom):
        print("Le prénom ne doit contenir que des lettres, des tirets, des espaces et les caractères é,è,ê,ë,ï,î,ô,ö,ù,ü,ç.")
        prenom = input("Prénom du contact : ")

    entreprise = input("Nom de l'entreprise : ")
    while not re.match(r'^[A-Za-zéèêëïîôöùüç\-\s]+$', entreprise):
        print("Le nom de l'entreprise ne doit contenir que des lettres, des tirets, des espaces et les caractères é,è,ê,ë,ï,î,ô,ö,ù,ü,ç.")
        entreprise = input("Nom de l'entreprise : ")
    
    email = input("Entrez votre adresse e-mail : ")
    while not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', email):
        print("L'adresse e-mail n'est pas valide.")
        email = input("Entrez votre adresse e-mail : ")
    
    tel = input("Numéro de téléphone du contact : ")
    while not re.match(r'^\d{10}$', tel):
        print("Le numéro de téléphone doit contenir 10 chiffres.")
        tel = input("Numéro de téléphone du contact : ")
    
    num_tel = '(+33) ' + tel 
    # Crée une chaîne de caractères formatée avec les informations personnelles
    info_str = f"{nom} , {prenom} , {entreprise} , {email} , {num_tel}\n"
 
# Enregistre la chaîne de caractères dans un fichier texte
    with open( ifile , "a") as f:    ## "a" = append = ajouter à la suite / "w" = whrite = créer un nouveau fichier
        f.write(info_str)

####### DEBUT DU PROGRAMME ########################################

choix = 0
while choix not in [1, 2]:
    choix = input("Pour créer un nouveau fichier tapez 1 \nPour compléter un fichier existant tapez 2 :")
    try:
        choix = int(choix)
    except ValueError:
        print("Veuillez entrer le nombre 1 ou 2 ! ")
        continue

if choix == 1:
    new()
else:
    exist()       

while True:
    saisie()

    quitter = input("Tapez 'Quitter' pour sortir ou appuyez sur la touche Entrée pour continuer : ")
    if quitter.lower() == "quitter":
        print("Au revoir !")
        break

