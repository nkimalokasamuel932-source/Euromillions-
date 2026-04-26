import streamlit as st
import pandas as pd
import random

# Configuration de la page
st.set_page_config(page_title="Loto & Euro Fusion", page_icon="🔮")

st.title("🔮 Fusion Statistique : Loto & Euromillions")
st.write("Analyse croisée des tendances du Samedi 25 Avril 2026")

# Chargement des données
@st.cache_data
def load_data():
    return pd.read_csv('synthese_hybride_euromillions.csv')

try:
    df = load_data()

    # Affichage du tableau de bord
    st.subheader("📊 Top 10 des numéros en convergence")
    st.dataframe(df.head(10), use_container_width=True)

    # Générateur de ticket optimisé
    st.divider()
    st.subheader("🎯 Générateur de Ticket Stratégique")
    
    if st.button("Générer ma combinaison pour Mardi"):
        # STRATÉGIE : 3 numéros dans le Top 10 + 2 numéros dans le reste
        top_piliers = df['Numero'].head(10).tolist()
        autres_nums = [n for n in range(1, 51) if n not in top_piliers]
        
        selection_piliers = random.sample(top_piliers, 3)
        selection_surprise = random.sample(autres_nums, 2)
        
        ticket_final = sorted(selection_piliers + selection_surprise)
        etoiles = sorted(random.sample(range(1, 13), 2))
        
        # Affichage du résultat
        st.success(f"**Numéros :** {', '.join(map(str, ticket_final))}")
        st.warning(f"**Étoiles :** {etoiles[0]} — {etoiles[1]}")
        
        st.info("💡 Cette combinaison mixe tes meilleures stats Loto/Euro et une part de hasard contrôlé.")
        st.balloons()

except Exception as e:
    st.error(f"Erreur de chargement : {e}")
    st.info("Vérifie que ton fichier CSV est bien sur GitHub.")

st.sidebar.write("Dernière mise à jour : 26 Avril 2026")
