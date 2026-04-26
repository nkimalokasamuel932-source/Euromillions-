import streamlit as st
import pandas as pd
import random

# Configuration de la page
st.set_page_config(page_title="Loto et Euromillions Master Pro", page_icon="🎯")

st.title("🎯 Loto Master : Euromillions")
st.write("Analyse hybride des probabilités pour le prochain tirage.")

# Chargement des données
@st.cache_data
def load_data():
    # Lit le fichier CSV que tu modifies sur GitHub
    df = pd.read_csv('synthese_hybride_euromillions.csv')
    # Trie par score le plus élevé
    df = df.sort_values(by='Score_Hybride', ascending=False)
    return df

try:
    data = load_data()

    # Affichage du Top 5 des numéros
    st.subheader("🔥 Top 5 des numéros suggérés")
    top_5 = data.head(5)
    
    # Création de colonnes pour un affichage propre sur mobile
    cols = st.columns(5)
    for i, (index, row) in enumerate(top_5.iterrows()):
        cols[i].metric(label=f"N°", value=int(row['Numero']))
        st.write(f"Score: **{row['Score_Hybride']}**")

    st.divider()

    # Section Générateur de Ticket
    st.subheader("🎰 Générateur de Ticket Flash")
    if st.button("Générer mon ticket pour Mardi"):
        # On prend 5 numéros parmi les 10 meilleurs scores
        pool_numeros = data['Numero'].head(10).tolist()
        ticket_nums = random.sample(pool_numeros, 5)
        ticket_nums.sort()
        
        # On génère 2 étoiles au hasard (Euromillions : 1 à 12)
        etoiles = random.sample(range(1, 13), 2)
        etoiles.sort()
        
        st.success(f"Numéros : {ticket_nums}")
        st.warning(f"Étoiles : {etoiles}")
        st.balloons()

    # Affichage du tableau complet pour les curieux
    with st.expander("Voir l'analyse complète"):
        st.dataframe(data)

except Exception as e:
    st.error(f"Erreur lors de la lecture du fichier CSV : {e}")
    st.info("Vérifie que ton fichier 'synthese_hybride_euromillions.csv' est bien présent sur GitHub.")
