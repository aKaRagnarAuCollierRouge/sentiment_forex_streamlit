import threading

import pandas as pd

from mise_à_jour import run_schedule
from récupération_données import *
import streamlit as st

def main():
    st.title("Sentiment Forex datas")

    # Récupérer la liste des paires de devises uniques
    currency_pairs = get_unique_currency_pairs()

    # Utiliser un menu déroulant (selectbox) pour sélectionner la paire de devises
    selected_pair = st.selectbox("Sélectionnez une paire de devises :", currency_pairs)

    # Récupérer les données pour la paire de devises sélectionnée
    data = get_data_for_currency_pair(selected_pair)

    #création DF pour controler entêtes
    df=pd.DataFrame(data,columns=['Date prélévé','Heure prélevé','Date réél','Heure réél(-3H)','Long(%)','Short(%)','Lots short','Lots long'])

    # Afficher un tableau pour les données de la paire de devises sélectionnée
    st.write(f"Table des données pour la paire de devises {selected_pair} :")
    st.dataframe(df)




if __name__ == "__main__":
    # Créer un thread pour exécuter la fonction d'ajout de données
    update_thread = threading.Thread(target=run_schedule)
    # Démarrer le thread
    update_thread.start()
    # Utiliser le décorateur st.cache pour optimiser la récupération des données lors du rafraîchissement de l'application
    main()


