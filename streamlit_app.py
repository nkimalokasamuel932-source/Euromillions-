import streamlit as st
import pandas as pd
import random

# Configuration
st.set_page_config(page_title="Loto-Euro Fusion Pro", page_icon="🧬")

st.title("🧬 Intelligence Croisée : Loto & Euro")
st.write("Analyse des tendances du **26 Avril 2026**")

# --- DONNÉES ---
loto_chauds = [16, 22, 23, 2, 33, 30, 9, 10, 14, 29, 49, 13, 17]
euro_chauds = [44, 42, 23, 19, 29, 37, 50, 25, 13, 17, 10, 49]

# Calcul de convergence automatique
communs = list(set(loto_chauds) & set(euro_chauds))

# Création sécurisée du tableau
data_fusion = []
for n in communs:
    data_fusion.append({
        "Numero": n,
        "Force": random.randint(85, 99),
        "Etat": "🔥 Brûlant" if n in [13, 23, 49] else "✅ Stable"
    })

df_convergence = pd.DataFrame(data_fusion)
if not df_convergence.empty:
    df_convergence = df_convergence.sort_values(by="Force", ascending=False)

# --- INTERFACE ---
tab1, tab2, tab3 = st.tabs(["🚀 CONVERGENCE", "🎯 LOTO MIROIR", "🇪🇺 EURO MIROIR"])

with tab1:
    st.subheader("📊 Les Élus de la Convergence")
    if not df_convergence.empty:
        st.table(df_convergence)
        if st.button("Générer Ticket Fusion"):
            piliers = df_convergence['Numero'].tolist()
            base = random.sample(piliers, min(len(piliers), 3))
            reste = random.sample([n for n in range(1, 51) if n not in base], 5 - len(base))
            ticket = sorted(base + reste)
            st.success(f"Ticket : {ticket}")
            st.balloons()
    else:
        st.write("Calcul de convergence en cours...")

with tab2:
    st.subheader("🎯 Jouer au Loto")
    if st.button("Générer Loto (Influence Euro)"):
        piliers = [n for n in euro_chauds if n <= 49]
        t = sorted(random.sample(piliers, 3) + random.sample(range(1, 50), 2))
        st.success(f"Ticket : {t} | Chance : {random.randint(1,10)}")

with tab3:
    st.subheader("🇪🇺 Jouer à l'Euro")
    if st.button("Générer Euro (Influence Loto)"):
        t = sorted(random.sample(loto_chauds, 3) + random.sample(range(1, 51), 2))
        st.warning(f"Ticket : {t[:5]} | Étoiles : {sorted(random.sample(range(1,13), 2))}")

st.divider()
st.metric(label="Numéro Pivot Global", value="23")
