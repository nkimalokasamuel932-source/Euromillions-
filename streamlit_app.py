import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Loto Master Pro", layout="wide")

st.title("🎯 Loto Master : Prédictions Mardi")

# Chargement des données
try:
    df = pd.read_csv('synthese_hybride_euromillions.csv', sep=';')
except:
    st.error("Fichier de données non trouvé. Vérifiez le fichier CSV.")
    st.stop()

tab1, tab2 = st.tabs(["📊 Analyse & Prédictions", "🎲 Générateur de Ticket"])

with tab1:
    st.header("Top 10 des numéros prioritaires")
    # On trie par score pour afficher les prédictions en haut
    df_sorted = df.sort_values(by="Score_Hybride", ascending=False)
    st.table(df_sorted.head(10))
    
    st.info("💡 Conseil : Le numéro en haut du tableau est votre base la plus solide.")

with tab2:
    st.header("Générateur Flash Optimisé")
    if st.button("🚀 Générer mon Ticket Rang 4"):
        # On prend les 3 meilleurs numéros + 2 au hasard dans le top 10
        top_3 = df_sorted['Numéro'].head(3).tolist()
        autres_top = df_sorted['Numéro'].iloc[3:10].tolist()
        ticket = top_3 + random.sample(autres_top, 2)
        ticket.sort()
        
        etoiles = random.sample(range(1, 13), 2)
        etoiles.sort()
        
        st.success(f"**Votre grille pour Mardi :**")
        st.subheader(f" {ticket[0]} - {ticket[1]} - {ticket[2]} - {ticket[3]} - {ticket[4]}")
        st.subheader(f"⭐ Étoiles : {etoiles[0]} et {etoiles[1]}")
