from menu import get_whit_no_space,get_user_choice,accueil
from Classes.Professeur import Professeur
import datetime
from Classes.ChoixInvalide import ChoixInvalide

#Fonctions Menu PROFESSEURS
def menu_professeur():
    print(f"""\t******************************************************\n\n\t\t\tGESTION DES PROFESSEURS\n\n\t******************************************************\n
Menu :
    1: Ajouter un professeur\n
    2: Supprimer un professeur\n
    3: Modifier les informations du professeur\n
    4: Lister les professeurs\n
    5: Obtenir le dernier professeur ajouté\n
    6: Retour\n
    0: Accueil\n
""")
    try:
        choice = get_whit_no_space("Entrez votre choix:")
        if choice == "1":
            enregistrer_prof()
        elif choice == "2":
            delete_prof()
        elif choice == "3":
            edit_prof()
        elif choice == "4":
            Professeur.ObtenirProfesseur()
            menu_professeur()
        elif choice == "5":
            Professeur.dernier()
            menu_professeur()
        elif choice == "6" or choice == "0":
            accueil()
            
        # else:
        #         raise ChoixInvalide()
    except ChoixInvalide as e:
            print(e)
            menu_professeur()
        

def enregistrer_prof():
    try:
        print("Entrez les informations sur le professeur\n")
        id = int(get_whit_no_space("Id: "))
        while any(prof.get_id() == id for prof in Professeur.professeurs):
            print("Cet id existe déjà")
            id =  int(get_whit_no_space("Id: "))
        nom = input("Nom: ")
        prenom = input("Prenom: ")
        ville = input ("Ville: ")
        dateNaissance_str = get_whit_no_space("Date de Naissance (format JJ-MM-AAAA): ")
        dateNaissance = datetime.datetime.strptime(dateNaissance_str, "%d-%m-%Y").date()
        while True:
            vacant = input("Vacant :")
            if vacant in ["0","1"]:
                break
            else :print("Veuillez entrer une valeur entre 0 ou 1")
        matiere = input("Entrez la  matière: ")
        cours= input("Entrez le prochain cours: ")
        sujet= input("Entrez le sujet de réunion: ")

    except ValueError:
        print ("Vous vous êtes trompez sur le type de la Date ou de l'id veuillez réessayer")
        enregistrer_prof()

   
    prof = Professeur(id,dateNaissance,ville,prenom,nom,vacant,matiere,cours,sujet)
    Professeur.ajouter(prof)
    get_user_choice("1: Ajouter un nouveau prof\n2: Revenir au menu précendent\nEntrez votre choix:",enregistrer_prof,menu_professeur)

def delete_prof():
    Professeur.lister()
    if Professeur.professeurs:
        try:
            id= int(input("Entrez l'id du prof à supprimer:"))
        except ValueError:
            print("L'id doit être un entier")
            delete_prof()
        Professeur.supprimer(id)

    else: menu_professeur()
    if Professeur.professeurs:
        get_user_choice("1: Supprimer un autre prof\n2: Revenir au menu précendent\nEntrez votre choix:",delete_prof,menu_professeur)
    else: menu_professeur()
    

        
def edit_prof():
    if Professeur.professeurs:
        Professeur.lister()
        try:
            id = int(input("Entrez l'id du professeur à modifier: "))
        except:
            print("Le id doit être un entier")
            edit_prof()
        prof = next((prof for prof in Professeur.professeurs if prof.get_id() == id), None)
        print(prof)
        if prof:
            Professeur.modifier(prof)
        else:
            print("ID incorrect")
            edit_prof()
    else : 
        print("Aucun élève enregistré") 
        menu_professeur()
    
