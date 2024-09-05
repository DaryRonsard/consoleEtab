from menu import get_whit_no_space,get_user_choice,accueil
from Classes.Eleve import Eleve
import datetime
from Classes.ChoixInvalide import ChoixInvalide

#Fonctions Menu ELEVES
def menu_eleve():
     print(f"""\t******************************************************\n\n\t\t\tGESTION DES ELEVES\n\n\t******************************************************\n
Menu :
    1: Ajouter un élève\n
    2: Supprimer un élève\n
    3: Modifier les informations de l'élève\n
    4: Lister les élèves\n
    5: Obtenir le dernier élève ajouté\n
    6: Retour\n
    0: Accueil\n
""")
     try:
            choice = get_whit_no_space("Entrez votre choix:")
            if choice == "1":
                enregistrer_eleve()
            elif choice == "2":
                delete_student()
            elif choice == "3":
                edit_eleve()
            elif choice == "4":
                Eleve.ObtenirEleve()
                menu_eleve()
                
            elif choice == "5":
                Eleve.dernier()
                menu_eleve()
                
            elif choice == "6" or choice == "0":
                accueil()
                
            else:
                raise ChoixInvalide()
     except ChoixInvalide as e:
            print(e)
            menu_eleve()
            

def enregistrer_eleve():
    try:
        print("Entrez les informations sur l'élève\n")
        id = int(get_whit_no_space("Id: "))
        while any(eleve.get_id() == id for eleve in Eleve.eleves):
            print("Cet id existe déjà")
            id =  int(get_whit_no_space("Id: "))
        nom = input("Nom: ")
        prenom = input("Prenom: ")
        ville = input ("Ville: ")
        dateNaissance_str = get_whit_no_space("Date de Naissance (format JJ-MM-AAAA): ")
        dateNaissance = datetime.datetime.strptime(dateNaissance_str, "%d-%m-%Y").date()
        classe = input("Classe :")
        matricule = input("Matricule :")
    except ValueError:
        print ("Vous vous êtes trompez sur le type de la Date ou de l'id veuillez réessayer")
        enregistrer_eleve()

   
    eleve = Eleve(id,dateNaissance,ville,prenom,nom,classe,matricule)
    Eleve.ajouter(eleve)
    get_user_choice("1: Ajouter un nouveau élève\n2: Revenir au menu précendent\nEntrez votre choix:",enregistrer_eleve,menu_eleve)

def delete_student():
    Eleve.lister()
    if Eleve.eleves:
        try:
            id= int(input("Entrez l'id de lélève à supprimer:"))
        except ValueError:
            print("L'id doit être un entier")
            delete_student()
        Eleve.supprimer(id)

    else: menu_eleve()
    if Eleve.eleves:
        get_user_choice("1: Supprimer un autre élève\n2: Revenir au menu précendent\nEntrez votre choix:",delete_student,menu_eleve)
    else: menu_eleve()
    

        
def edit_eleve():
    if Eleve.eleves:
        Eleve.lister()
        try:
            id = int(input("Entrez l'id de l'élève à modifier: "))
        except:
            print("Le id doit être un entier")
            edit_eleve()
        eleve = next((eleve for eleve in Eleve.eleves if eleve.get_id() == id), None)
        print(eleve)
        if eleve:
            Eleve.modifier(eleve)
        else:
            print("ID incorrect")
            edit_eleve()
    else : 
        print("Aucun élève enregistré") 
        menu_eleve()
    
