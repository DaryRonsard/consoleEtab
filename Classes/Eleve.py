from Classes.Personne import Personne

from Interfaces.ICRUDElve import ICRudeleve
from datetime import datetime

class Eleve(Personne,ICRudeleve):
    eleves=[]
    def __init__(self, id, dateNaissance, ville, prenom, nom, classe,matricule):
        super().__init__(id, dateNaissance, ville, prenom, nom)
        self.__classe = classe
        self.__matricule = matricule

    def __str__(self):
        return f"[ID: {self.get_id()},MATRICULE: {self.get_matricule()} NOM: {self.get_nom()}, PRENOMS: {self.get_prenom()}, DATE DE NAISSANCE: {self.get_dateNaissance()}, VILLE: {self.get_ville()}, CLASSE: {self.get_classe()}]"

    # Getter et Setter pour la classe
    
    def get_classe(self):
        return self.__classe
    
    def set_classe(self, classe):
        self.__classe = classe

    def get_matricule(self):
        return self.__matricule
    
    def set_matricule(self, matricule):
        self.__matricule = matricule

    # Méthodes 
    #Methode ajouter
    @staticmethod
    def ajouter(eleve):
        Eleve.eleves.append(eleve)
        print(f"Élève {eleve.get_nom()} {eleve.get_prenom()} ajouté avec succès.")

    #Methode modifier
    @staticmethod
    def modifier(eleve):
        from Services.Gestions_eleves import menu_eleve

        for student in Eleve.eleves:
            if student.get_id() == eleve.get_id():
                while True:
                    choix = input("Que voulez-vous mettre à jour?\n1. Modifier le nom\n2. Modifier le prénom\n3. Modifier la date de naissance\n4. Modifier la ville\n5. Modifier la classe\n6. Modifier le matricule\n7. Retour\nEntrez votre choix: ")

                    if choix == "1":
                        nouveau_nom = input("Entrez le nouveau nom: ")
                        student.set_nom(nouveau_nom)
                        print(f"Nom mis à jour en {nouveau_nom}.")
                        
                    elif choix == "2":
                        nouveau_prenom = input("Entrez le nouveau prénom: ")
                        student.set_prenom(nouveau_prenom)
                        print(f"Prénom mis à jour en {nouveau_prenom}.")

                    elif choix == "3":
                        while True:
                            nouvelle_date = input("Entrez la nouvelle date de naissance (DD-MM-YYYY): ")
                            try:
                                date_naissance = datetime.strptime(nouvelle_date, "%d-%m-%Y").date()
                                student.set_dateNaissance(date_naissance)
                                print(f"Date de naissance mise à jour en {date_naissance}.")
                                break  
                            except ValueError:
                                print("Format de date invalide. Veuillez entrer la date au format YYYY-MM-DD.")
                            
                    elif choix == "4":
                        nouvelle_ville = input("Entrez la nouvelle ville: ")
                        student.set_ville(nouvelle_ville)
                        print(f"Ville mise à jour en {nouvelle_ville}.")
                        
                    elif choix == "5":
                        nouvelle_classe = input("Entrez la nouvelle classe: ")
                        student.set_classe(nouvelle_classe)
                        print(f"Classe mise à jour en {nouvelle_classe}.")
                    
                    elif choix == "6":
                        nouveau_matricule = input("Entrez le nouveau matricule: ")
                        student.set_matricle(nouveau_matricule)
                        print(f"Matricule mise à jour en {nouveau_matricule}.")
                        
                    elif choix == "7":
                        menu_eleve()
                        return  
                        
                        
                    else:
                        print("Choix invalide. Veuillez réessayer.")

    #Methode lister
    @staticmethod
    def ObtenirEleve():
        if not Eleve.eleves:
            print("Aucun élève enregistré.")
        else:
            print("Elèves:\n")
            for eleve in Eleve.eleves:
                print(eleve)
    
    #Methode supprimer
    @staticmethod
    def supprimer(id):
        for eleve in Eleve.eleves:
                if eleve.get_id() == id:
                    Eleve.eleves.remove(eleve)
                    print(f"Elève avec ID {id} supprimée avec succès.")

    #Methode afficher dernier
    @staticmethod
    def dernier():
        if not Eleve.eleves:
            print("Aucun élève enregistré.")
        else:
            last_eleve = Eleve.eleves[-1]  
            print("Dernier élève enregistré: ",last_eleve)
            
    #Methode obtenir
    @staticmethod
    def obtenir(identifiant):
        return