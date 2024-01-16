import os
from google.auth import load_credentials_from_file
from firebase_admin import initialize_app
from google.cloud import firestore

# Charger les informations d'identification depuis le fichier JSON
credentials, _ = load_credentials_from_file('C:/Users/carlo/AppData/Roaming/gcloud/application_default_credentials.json')

# Définir la variable d'environnement GOOGLE_APPLICATION_CREDENTIALS
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/carlo/AppData/Roaming/gcloud/application_default_credentials.json'

# Spécifier le projet (remplacez "votre-projet-id" par l'ID de votre projet)
os.environ['GOOGLE_CLOUD_PROJECT'] = 'formulaire-e2086'

# Initialiser l'application Firebase
initialize_app()

# Initialiser la connexion Firestore
db = firestore.Client()

class Formulaire:
    def __init__(self):
        self.intention_quitter_pays = None
        self.tranche_age = None
        self.niveau_etudes = None
        self.pays_vise = None
        self.raison_depart = None
        self.objectif_depart = None
        self.duree_prevue = None
        self.intention_retour_pays_origine = None

    def enregistrer_dans_firestore(self):
        # Créer une référence à la collection "formulaires"
        formulaires_ref = db.collection('formulaires')

        # Ajouter les données du formulaire à la collection
        formulaires_ref.add({
            'intention_quitter_pays': self.intention_quitter_pays,
            'tranche_age': self.tranche_age,
            'niveau_etudes': self.niveau_etudes,
            'pays_vise': self.pays_vise,
            'raison_depart': self.raison_depart,
            'objectif_depart': self.objectif_depart,
            'duree_prevue': self.duree_prevue,
            'intention_retour_pays_origine': self.intention_retour_pays_origine
        })

    def question_intention_quitter_pays(self):
        self.intention_quitter_pays = input("Avez-vous l'intention de quitter le pays après avoir terminé vos études universitaires?\n1. Oui\n2. Non\n3. Incertain\n")

    def question_tranche_age(self):
        print("Quel est votre âge actuel?")
        print("1. Moins de 20 ans")
        print("2. 20-24 ans")
        print("3. 25-29 ans")
        print("4. 30-34 ans")
        print("5. 35 ans et plus")
        choice = input()
        age_ranges = ["Moins de 20 ans", "20-24 ans", "25-29 ans", "30-34 ans", "35 ans et plus"]
        self.tranche_age = age_ranges[int(choice) - 1]

    def question_niveau_etudes(self):
        print("À quel niveau d'études êtes-vous actuellement?")
        print("1. Licence 1")
        print("2. Licence 2")
        print("3. Licence 3")
        print("4. Licence 4")
        print("5. DUT 1")
        print("6. DUT 2")
        choice = input()
        study_levels = ["Licence 1", "Licence 2", "Licence 3", "Licence 4", "DUT 1", "DUT 2"]
        self.niveau_etudes = study_levels[int(choice) - 1]

    def question_pays_vise(self):
        print("Vers quel(s) pays envisagez-vous de vous rendre? (Sélectionnez tous ceux qui s'appliquent)")
        print("1. États-Unis")
        print("2. Canada")
        print("3. Royaume-Uni")
        print("4. Australie")
        print("5. France")
        print("6. Autre (précisez)")
        choice = input()
        if choice == "6":
            self.pays_vise = input("Précisez le(s) pays : ")
        else:
            countries = ["États-Unis", "Canada", "Royaume-Uni", "Australie", "France"]
            self.pays_vise = [countries[int(c) - 1] for c in choice.split(',')]

    def question_raison_depart(self):
        print("Pourquoi envisagez-vous de quitter le pays? (Sélectionnez toutes celles qui s'appliquent)")
        print("1. Opportunités professionnelles")
        print("2. Recherche académique")
        print("3. Qualité de vie")
        print("4. Autre (précisez)")
        choice = input()
        if choice == "4":
            self.raison_depart = input("Précisez la raison : ")
        else:
            reasons = ["Opportunités professionnelles", "Recherche académique", "Qualité de vie"]
            self.raison_depart = [reasons[int(r) - 1] for r in choice.split(',')]

    def question_objectif_depart(self):
        print("Envisagez-vous de quitter le pays pour des études supplémentaires ou d'autres raisons? (Sélectionnez tous ceux qui s'appliquent)")
        print("1. Études supplémentaires")
        print("2. Raisons professionnelles")
        print("3. Raisons personnelles")
        choice = input()
        objectives = ["Études supplémentaires", "Raisons professionnelles", "Raisons personnelles"]
        self.objectif_depart = [objectives[int(o) - 1] for o in choice.split(',')]

    def question_duree_prevue(self):
        print("Si vous envisagez un départ temporaire, quelle est la durée prévue de votre séjour?")
        print("1. Moins d'un an")
        print("2. 1-2 ans")
        print("3. 3-5 ans")
        print("4. Plus de 5 ans")
        choice = input()
        durations = ["Moins d'un an", "1-2 ans", "3-5 ans", "Plus de 5 ans"]
        self.duree_prevue = durations[int(choice) - 1]

    def question_intention_retour_pays_origine(self):
        print("Avez-vous l'intention de retourner dans votre pays d'origine après votre séjour à l'étranger?")
        print("1. Oui")
        print("2. Non")
        print("3. Incertain")
        choice = input()
        intentions = ["Oui", "Non", "Incertain"]
        self.intention_retour_pays_origine = intentions[int(choice) - 1]

# Exemple d'utilisation du formulaire
formulaire = Formulaire()
formulaire.question_intention_quitter_pays()
formulaire.question_tranche_age()
formulaire.question_niveau_etudes
formulaire.question_pays_vise
formulaire.question_raison_depart
formulaire.question_objectif_depart
formulaire.question_duree_prevue
formulaire.question_intention_retour_pays_origine

# Enregistrer le formulaire dans Firestore
formulaire.enregistrer_dans_firestore()
