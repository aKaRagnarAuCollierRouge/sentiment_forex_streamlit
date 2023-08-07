import sqlite3
import schedule
import time
import locale
import locale
from récupération_données import *
import datetime
# Définir le local sur 'fr_FR.UTF-8' pour la France
#locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')


# Fonction pour ajouter les nouvelles données dans la base de données
def ajouter_donnees():
    # Vérifier si l'heure actuelle est entre vendredi 23:00 et dimanche 23:00
    date_heure_now = datetime.datetime.now()

    # Vérifier si l'heure actuelle est entre vendredi 23:00 et dimanche 23:00
    if date_heure_now.weekday() == 4 and date_heure_now.hour >= 23:
        print("Pas d'ajout de données entre vendredi 23:00 et dimanche 23:00")
        return
    elif date_heure_now.weekday() == 5:
        print("Pas d'ajout de données entre vendredi 23:00 et dimanche 23:00")
        return
    elif date_heure_now.weekday() == 6 and date_heure_now.hour < 23:
        print("Pas d'ajout de données entre vendredi 23:00 et dimanche 23:00")
        return

    liste_données=récupération_données()

    date=date_heure_now.strftime('%d/%m/%Y')
    heure=date_heure_now.strftime('%H:%M')
    # Ajoute ici le code pour récupérer les nouvelles données à ajouter à la base de données
    # Par exemple, tu peux les récupérer depuis une source externe (API, fichier CSV, etc.)

    # Calculer la date et l'heure avec un décalage de -3 heures
    decalage_heures = datetime.timedelta(hours=-3)
    date_decalee = (date_heure_now + decalage_heures).strftime('%d/%m/%Y')
    heure_decalee = (date_heure_now + decalage_heures).strftime('%H:%M')

    # Ensuite, insère les nouvelles données dans la base de données
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    for donnée in liste_données:
        donnée.append(date)
        donnée.append(heure)
        donnée.append(date_decalee)
        donnée.append(heure_decalee)
    # Exemple d'insertion de données (remplace par tes propres données)
        cursor.execute("INSERT INTO row_data (Paire,Pourcentage_long, Pourcentage_short,Lot_short, Lot_long,Date,Heure,Date_réél,Heure_réél) VALUES (?, ?, ?, ?, ?, ?,?,?,?)",donnée)
    conn.commit()
    conn.close()


def run_schedule():
    # Planifie l'exécution de la fonction toutes les heures rondes
    schedule.every().hour.at(':00').do(ajouter_donnees)
    while True:

        schedule.run_pending()
        time.sleep(1)
