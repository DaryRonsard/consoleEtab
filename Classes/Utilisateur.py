import mysql.connector
from mysql.connector import Error
from datetime import datetime
#Classe Utilisateur
class Utilisateur:
    utilisateurs=[]
    next_id = 2
    def __init__(self,pseudo,motDePasse,dateCreation):
        self.__id = Utilisateur.next_id
        self.__pseudo = pseudo
        self.__motDePasse = motDePasse
        self.__dateCreation = dateCreation
        Utilisateur.utilisateurs.append(self)
        Utilisateur.next_id += 1

    def __str__(self) -> str:
        return f"[Identifiant:{self.get_pseudo()} | Mot de passe:{self.get_motDePasse()}]"
    #Getters
    def get_id(self):
        return self.__id
        
    def get_pseudo(self):
        return self.__pseudo
    
    def get_motDePasse(self):
        return self.__motDePasse
    
    def get_dateCreation(self):
        return self.__dateCreation
    
    #Setters
    def set_id(self,id):
        self.__id = id
    
    def set_pseudo(self,pseudo):
        self.__pseudo = pseudo
    
    def set_motDePasse(self, motDePasse):
        self.__motDePasse = motDePasse

    def set_dateCreation(self,dateCreation):
        self.__dateCreation = dateCreation

    #Methodes
    #Méthode authentification
    @staticmethod
    def authentification(identifiant, motDePasse):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='walter',
                password='Hr010120018'
            )
            
            if connection.is_connected():
                cursor = connection.cursor()
                query = "SELECT pseudo, mot_de_passe FROM utilisateurs"
                cursor.execute(query)
                utilisateurs = cursor.fetchall()
                
                for user in utilisateurs:
                    pseudo, mot_de_passe = user
                    if identifiant == pseudo and motDePasse == mot_de_passe:
                        return True
                        
                return False

        except Error as e:
            print(f"Error: {e}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        
    # Méthode ajouter
    @staticmethod
    def ajouterCompte(identifiant, motDePasse, date):
        from menu import get_user_choice
        
        from Services.Gestions_Utilisateurs import enregistrer_user
        for user in Utilisateur.utilisateurs:
            if user.get_pseudo() == identifiant:
                print("Identifiant déjà utilisé.")
                enregistrer_user()
                return

        Utilisateur(identifiant, motDePasse, date)
        print(f"Utilisateur {identifiant} ajouté avec succès.")

    
    # Méthode modifier
    @staticmethod
    def modifierMotDePasse(identifiant, motDePasse):
        for user in Utilisateur.utilisateurs:
            if user.get_pseudo() == identifiant:
                user.set_motDePasse(motDePasse)
                print("Mot de passe modifié avec succès.")
                return
        print("Utilisateur non trouvé.")

    #Méthode supprimer
    @staticmethod
    def supprimerCompte(identifiant, motDePasse):
        for user in Utilisateur.utilisateurs:
            if user.get_pseudo() == identifiant and user.get_motDePasse() == motDePasse:
                Utilisateur.utilisateurs.remove(user)
                print(f"Utilisateur {identifiant} supprimé avec succès.")
                return
        
        print("Identifiant ou mot de passe incorrect.")

    #Méthode lister
    @staticmethod
    def listerUtilisateur():
        if not Utilisateur.utilisateurs:
            print("Aucun utilisateur enregistré.")
        else:
            print("Utilisateurs:\n")
            for user in Utilisateur.utilisateurs:
                print(user)

    #Méthode afficherdernier
    @staticmethod
    def dernier():
        if not Utilisateur.utilisateurs:
            print("Aucun utilisateur enregistré.")
        else:
            last_user = Utilisateur.utilisateurs[-1]  
            print("Dernier utilisateur enregistré: ",last_user)

    #Méthode creation d'un user par defaut
    @staticmethod
    def initialize_default_user():
        default_username = "admin"
        default_password = "admin"
        default_dateCreation= datetime.now()
        Utilisateur(default_username, default_password,default_dateCreation)
        print("Utilisateur par défaut créé.")


    @staticmethod
    def initialize_default_user_sql():
        default_username = "admin"
        default_password = "admin"
        default_dateCreation= datetime.now()

        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='etab_db',
                user='walter',
                password='Hr010120018'
            )
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM utilisateurs WHERE pseudo= %s",(default_username,))
                if cursor.fetchone is None:
                    cursor.execute("INSERT INTO utilisateurs (pseudo,mot_de_passe,date_creation) VALUES (%s, %s, %s)",
                                (default_username, default_password, default_dateCreation))
                    connection.commit()
                    print("Utilisateur par défaut créé.")
                else:
                    print("Utilisateur par défaut existe déja.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()