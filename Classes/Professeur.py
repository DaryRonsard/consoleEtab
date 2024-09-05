from Interfaces.ICRUDProfesseur import ICRUDProfesseur
from Interfaces.IEducation import IEducation
from Classes.Personne import Personne
from datetime import datetime
#Classe Professeur
class Professeur(IEducation,ICRUDProfesseur,Personne):
    professeurs=[]
    def __init__(self, id, dateNaissance, ville, prenom, nom,vacant,matiereEnseignee, prochainCours, sujetProchaineReunion):
        super().__init__(id, dateNaissance, ville, prenom, nom)
        self.__vacant = vacant
        self.__matiereEnseignee = matiereEnseignee
        self.__prochainCours = prochainCours
        self.__sujetProchaineReunion = sujetProchaineReunion
    
    def __str__(self):
        return f"""[ID: {self.get_id()}, NOM: {self.get_nom()}, PRENOMS: {self.get_prenom()}, DATE DE NAISSANCE: {self.get_dateNaissance()}, VILLE: {self.get_ville()}\nMatiere Enseignee: {self.get_matiereEnseignee()}, Prochain Cours: {self.get_prochainCours()}, Sujet Prochaine Réunion: {self.get_sujetProchaineReunion()}]
        """


    # Getter et Setter pour la classe
    
    def get_vacant(self):
        return self.__vacant
    
    def get_matiereEnseignee(self):
        return self.__matiereEnseignee
    
    def get_prochainCours(self):
        return self.__prochainCours
    
    def get_sujetProchaineReunion(self):
        return self.__sujetProchaineReunion
    
    def set_vacant(self, vacant):
        self.__vacant = vacant

    def set_matiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
    
    def set__prochainCours(self, prochainCours):
        self.__prochainCours = prochainCours

    def set_sujetProchaineReunion(self, sujetProchaineReunion):
        self.__sujetProchaineReunion = sujetProchaineReunion


    # Méthodes 
    #Méthode ajouter
    @staticmethod
    def ajouter(professeur):
        Professeur.professeurs.append(professeur)
        print(f"Professeur {professeur.get_nom()} {professeur.get_prenom()} ajouté avec succès.")

    @staticmethod
    #Méthode modifier
    def modifier(professeur):
        from Services.Gestions_professeurs import menu_professeur

        for profs in Professeur.professeurs:
            if profs.get_id() == professeur.get_id():
                while True:
                    choix = input("""Que voulez-vous mettre à jour?\n1. Modifier le nom\n2. Modifier le prénom\n3. Modifier la date de naissance\n4. Modifier la ville\n5. Modifier la classe\n6. Modifier la matière\n6. Modifier le prochain cours\n6. Modifier le sujet de la réunion\n9. Retour\nEntrez votre choix: """)

                    if choix == "1":
                        nouveau_nom = input("Entrez le nouveau nom: ")
                        profs.set_nom(nouveau_nom)
                        print(f"Nom mis à jour en {nouveau_nom}.")
                        
                    elif choix == "2":
                        nouveau_prenom = input("Entrez le nouveau prénom: ")
                        profs.set_prenom(nouveau_prenom)
                        print(f"Prénom mis à jour en {nouveau_prenom}.")

                    elif choix == "3":
                        while True:
                            nouvelle_date = input("Entrez la nouvelle date de naissance (DD-MM-YYYY): ")
                            try:
                                date_naissance = datetime.strptime(nouvelle_date, "%d-%m-%Y").date()
                                profs.set_dateNaissance(date_naissance)
                                print(f"Date de naissance mise à jour en {date_naissance}.")
                                break  
                            except ValueError:
                                print("Format de date invalide. Veuillez entrer la date au format YYYY-MM-DD.")
                            
                    elif choix == "4":
                        nouvelle_ville = input("Entrez la nouvelle ville: ")
                        profs.set_ville(nouvelle_ville)
                        print(f"Ville mise à jour en {nouvelle_ville}.")
                        
                    elif choix == "5":
                        while True:
                            vacant = input("Entrez la nouvelle classe: (0 pour non ou 1 pour oui)")
                            try:
                                profs.set_vacant(vacant)
                                print(f"Vacant mise à jour en {vacant}.")
                                break  
                            except ValueError:
                                print("Format invalide. Veuillez entrer 0 ou 1")

                    elif choix == "6":
                        nouvelle_matiere = input("Entrez la nouvelle matière: ")
                        profs.set_matiereEnseignee(nouvelle_matiere)
                        print(f"Matière mise à jour en {nouvelle_matiere}.")    
                    
                    elif choix == "7":
                        nouveau_cours= input("Entrez le nouveau prochain cours: ")
                        profs.set__prochainCours(nouveau_cours)
                        print(f"Prochain cours mis à jour en {nouveau_cours}.")   

                    elif choix == "8":
                        nouveau_sujet= input("Entrez le nouveau sujet de réunion: ")
                        profs.set_sujetProchaineReunion(nouveau_sujet)
                        print(f"Sujet de réunion mis à jour en {nouveau_sujet}.")   

                    elif choix == "9":
                        menu_professeur()
                        return  
                        
                        
                    else:
                        print("Choix invalide. Veuillez réessayer.")
                    break  # Sortir de la boucle après une mise à jour
    
    #Méthode lister
    @staticmethod
    def ObtenirProfesseur():
        if not Professeur.professeurs:
            print("Aucun professeur enregistré.")
        else:
            print("Professeurs:\n")
            for prof in Professeur.professeurs:
                print(prof)

    #Méthode supprimer
    @staticmethod
    def supprimer(id):
        for prof in Professeur.professeurs:
                if prof.get_id() == id:
                    Professeur.professeurs.remove(prof)
                    print(f"Professeur avec ID {id} supprimée avec succès.")
    
    #Méthode obtenir
    @staticmethod
    def obtenir(identifiant):
        return 
    
    #Méthode afficher dernier
    @staticmethod
    def dernier():
        if not Professeur.professeurs:
            print("Aucun professeur enregistré.")
        else:
            last_prof = Professeur.professeurs[-1]  
            print("Dernier professeur enregistré: ",last_prof)
    
    #Méthode enseigner
    @staticmethod
    def enseigner(self, matiere):
        return f"Enseigne la matière {matiere}"
    
    #Méthode preparerCours
    @staticmethod
    def preparerCours(self, prochainCours):
        return f"Prépare le contenu d'un cours sur le sujet {prochainCours}"
    
    #Méthode assisterReunion
    @staticmethod
    def assisterReunion(self, sujetProchaineReunion):
        return f"Doit assister à une reunion sur {sujetProchaineReunion}"