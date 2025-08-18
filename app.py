import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- Configuration de la page Streamlit ---
# Le thème sombre par défaut est activé via la configuration globale de Streamlit,
# mais vous pouvez aussi le forcer avec st.set_page_config en spécifiant le layout et le titre.
st.set_page_config(layout="wide", page_title="Tontine 3.0 - Dashboard", initial_sidebar_state="expanded")

# --- Injection de CSS pour un style personnalisé ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    .stMetric {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #30363d;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stMetric span {
        font-size: 1.2rem;
        font-weight: bold;
    }
    .st-emotion-cache-1r6r0z6 {
        background-color: #161b22;
    }
    .st-emotion-cache-13ln4j7 {
        background-color: #161b22;
    }
    .st-emotion-cache-12m1a0 {
        background-color: #161b22;
    }
    .st-emotion-cache-19623e1 {
        background-color: #161b22;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Titre et introduction ---
st.title("Tontine 3.0 : Un système de Fusions ✨")
st.markdown("""
<div style="text-align: center;">
    Bienvenue sur ce tableau de bord interactif pour explorer le système d'investissement Tontine 3.0.
    Utilisez la barre latérale pour naviguer entre les différentes fusions.
</div>
""", unsafe_allow_html=True)

# --- Données du système (Fusion 1 à 5) ---
data = {
    'Fusion': [1, 2, 3, 4, 5],
    'Gain Total ($)': [14000, 28000, 56000, 112000, 224000],
    'Investissement Crypto ($)': [2000, 4000, 8000, 16000, 32000],
    'Total Redistribué ($)': [12000, 24000, 48000, 96000, 192000],
    'Gain par Membre ($)': [400, 800, 1600, 3200, 6400],
    'Réinvestissement ($)': [4000, 8000, 16000, 32000, 64000],
    'Cumul Crypto ($)': [2000, 6000, 14000, 30000, 62000]
}
df = pd.DataFrame(data)

# --- Sélecteur de Fusion dans la barre latérale ---
st.sidebar.header("Naviguer entre les Fusions")
selected_fusion = st.sidebar.selectbox("Sélectionnez la génération de Fusion :", list(range(1, 6)), format_func=lambda x: f"Fusion {x}")
current_fusion_data = df.loc[df['Fusion'] == selected_fusion].squeeze()

# --- 1. Démarrage du système ---
st.markdown("---")
st.header("1. Démarrage du système : La Fusion 1")
st.markdown(
    """
    <div style="padding: 15px; border-radius: 10px; background-color: #1f2a36; border: 1px solid #30363d; margin-top: 10px; color: #c9d1d9;">
        💡 Le système est lancé par un groupe de <b>20 personnes</b>.
        Chacune investit <b>$100</b> pour former une cagnotte communautaire de <b>$2000</b>,
        qui permet d'entrer dans la <b>Tontine 3.0</b>.
    </div>
    """,
    unsafe_allow_html=True
)

# --- 2. Gains et Répartition ---
st.markdown("---")
st.header(f"2. Gains et Répartition : Fusion {selected_fusion}")

cols = st.columns(3)
with cols[0]:
    st.markdown(f'<div class="stMetric"><span>🏆 Gain Total</span><br><br><span style="color:#66cc00; font-size:1.8rem;">${current_fusion_data["Gain Total ($)"]:,}</span></div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown(f'<div class="stMetric"><span>💰 Investissement Crypto</span><br><br><span style="color:#5bc0de; font-size:1.8rem;">${current_fusion_data["Investissement Crypto ($)"]:,}</span></div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown(f'<div class="stMetric"><span>💸 Total Redistribué</span><br><br><span style="color:#f0ad4e; font-size:1.8rem;">${current_fusion_data["Total Redistribué ($)"]:,}</span></div>', unsafe_allow_html=True)

st.markdown("""
Le gain total généré par la Fusion 1 est de **$14,000**. Une partie est investie en crypto, et le reste est redistribué aux membres.
""")

# --- 3. Détails des gains par membre ---
st.markdown("---")
st.subheader("Détails des gains par membre")
st.info(f"À ce stade, chaque membre de la Fusion {selected_fusion} reçoit un gain de **${current_fusion_data['Gain par Membre ($)']:,}**.")
st.markdown('<div class="calculator-container"><p class="calculator-title">CALCULATEUR DE GAINS INDIVIDUELS</p>', unsafe_allow_html=True)
st.markdown(f"**Gain individuel par membre** : **${current_fusion_data['Gain par Membre ($)']}**")
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. Réinvestissement et cumul ---
st.markdown("---")
st.header("4. Le cycle de doublement")
st.subheader("Réinvestissement pour la prochaine fusion")

cols_reinvest = st.columns(2)
with cols_reinvest[0]:
    st.metric(label=f"Fonds pour la Fusion {selected_fusion+1}", value=f"${current_fusion_data['Réinvestissement ($)']:,}")
with cols_reinvest[1]:
    st.metric(label="Cumul Crypto Total", value=f"${current_fusion_data['Cumul Crypto ($)']:,}")

st.markdown(f"""
Un tiers des gains, soit **${current_fusion_data['Réinvestissement ($)']:,}**, est automatiquement réinvesti pour la Fusion {selected_fusion+1}.
Ce système garantit un doublement des gains et des investissements à chaque nouvelle génération de fusion.
""")

# --- Tableau détaillé ---
st.markdown("---")
st.header("Tableau de suivi détaillé des Fusions")
st.dataframe(df.set_index('Fusion').T)

# --- Graphiques de visualisation ---
st.markdown("---")
st.header("5. Points Forts à retenir")

st.markdown("""
<h3 style="color: #66cc00;">1. L'investissement unique</h3>
<p>Vous n'investissez que 100 $ une seule fois. Le système se finance ensuite lui-même.</p>
<h3 style="color: #66cc00;">2. Le double cumul</h3>
<p>Le système génère non seulement des gains en argent, mais aussi un investissement cumulatif en cryptomonnaie qui grandit à chaque fusion.</p>
""", unsafe_allow_html=True)

# Graphique de l'évolution des gains
fig_gains = px.line(
    df,
    x='Fusion',
    y=['Gain Total ($)', 'Total Redistribué ($)', 'Investissement Crypto ($)'],
    title="Croissance des Gains et des Investissements par Fusion",
    labels={'value': 'Montant ($)', 'variable': 'Catégorie'},
    color_discrete_map={
        'Gain Total ($)': 'rgb(102, 204, 0)',
        'Total Redistribué ($)': 'rgb(255, 153, 0)',
        'Investissement Crypto ($)': 'rgb(51, 153, 255)'
    }
)
fig_gains.update_traces(mode='lines+markers')
st.plotly_chart(fig_gains, use_container_width=True)

# Graphique de l'évolution des gains par membre
fig_member = px.line(
    df,
    x='Fusion',
    y='Gain par Membre ($)',
    title="Gains individuels par membre",
    labels={'Fusion': 'Génération de Fusion', 'Gain par Membre ($)': 'Gain individuel ($)'},
    color_discrete_sequence=['#ffcc00']
)
fig_member.update_traces(mode='lines+markers')
st.plotly_chart(fig_member, use_container_width=True)
