
import sqlite3

import requests
import schedule
import time
from bs4 import BeautifulSoup as bs

# Fonction pour récupérer la liste des paires de devises uniques depuis la base de données
def get_unique_currency_pairs():
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT paire FROM row_data")
    pairs = cursor.fetchall()
    conn.close()
    return [pair[0] for pair in pairs]

# Fonction pour récupérer les données pour une paire de devises spécifique depuis la base de données
def get_data_for_currency_pair(currency_pair):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Date,Heure,Date_réél,Heure_réél,Pourcentage_long,Pourcentage_short,Lot_long,Lot_short FROM row_data WHERE paire = ?", (currency_pair,))
    data = cursor.fetchall()
    conn.close()
    return data

#fonction pour récupérer les données de myfxbook
def récupération_données():
    url_fx_books = requests.get("https://www.myfxbook.com/fr/community/outlook")
    soup = bs(url_fx_books.text, 'html.parser')
    trs = soup.find_all('tr', class_='outlook-symbol-row')
    liste_données=[]
    for tr in trs:
        tbody=tr.find('tbody')
        tds=tbody.find_all('td')
        symbole=tds[0].text
        short=tds[2].text.rstrip('%')
        lot_short=tds[3].text.rstrip(" lots")
        long=tds[6].text.rstrip("%")
        lot_long=tds[7].text.rstrip(" lots")
        liste_données.append([symbole,long,short,lot_long,lot_short])
    return liste_données





