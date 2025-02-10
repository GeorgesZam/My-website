import streamlit as st

# Configuration de la page avec image favicon
st.set_page_config(
    page_title="Georges Zam | Portfolio Ingénierie IA",
    page_icon="🚀",
    layout="wide"
)

# CSS personnalisé avec dégradé professionnel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;500&display=swap');
    
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%);
        color: #f8fafc;
        font-family: 'Roboto Mono', monospace;
    }
    
    .skill-card {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .project-link {
        transition: transform 0.3s ease;
    }
    
    .project-link:hover {
        transform: translateX(10px);
    }
</style>
""", unsafe_allow_html=True)

# Header avec photo et texte côte à côte
col1, col2 = st.columns([1, 2], gap="medium")
with col1:
    st.image("https://via.placeholder.com/300x300.png?text=Georges+Zam", width=250)  # Remplacez par votre photo
    
with col2:
    st.markdown("# Georges Zam  \n**Ingénieur IA en devenir | CESI Nanterre**", unsafe_allow_html=True)
    st.markdown("""
    🔍 *Actuellement en recherche d'un stage ouvrier technique (3-4 mois) à partir d'avril 2025*
    
    *"Transformer les concepts en solutions concrètes grâce à une approche ingénieuse"*
    """)

# Section Compétences avec cards animées
st.header("🛠️ Expertise Technologique")
with st.container():
    col3, col4, col5 = st.columns(3)
    with col3:
        st.markdown("""
        <div class="skill-card">
            <h4>🤖 Intelligence Artificielle</h4>
            • Machine Learning avancé  \n• NLP (Transformers)  \n• Computer Vision
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="skill-card">
            <h4>💻 Développement Créatif</h4>
            • Python Full Stack  \n• Automatisation Arduino  \n• Simulation Tinkercad
        </div>
        """, unsafe_allow_html=True)
    with col5:
        st.markdown("""
        <div class="skill-card">
            <h4>🚀 Gestion de Projets</h4>
            • Méthodes Agile  \n• Conduite d'innovation  \n• Optimisation processus
        </div>
        """, unsafe_allow_html=True)

# Section Projets avec interactions
st.header("💡 Réalisations Concrètes")
tab1, tab2 = st.tabs(["Projets Techniques", "Contributions Open Source"])
with tab1:
    st.markdown("""
    ### 🏗️ Projets Phares
    - **Système de surveillance IoT** : Architecture cloud-based avec analyse prédictive
    - **Chatbot industriel** : NLP customisé pour la maintenance préventive
    - **Simulateur IA** : Modèle de détection d'anomalies en temps réel
    """)
    
with tab2:
    st.markdown("""
    ### 👨💻 Collaborations
    - Contribution à **TensorFlow Extended** (optimisation de pipelines)
    - Développement de librairie Arduino pour la domotique
    - Tutoriels Python sur Dev.to (+15k vues)
    """)

st.markdown("""
<div class="project-link">
    🔗 [Explorez mes projets GitHub](https://github.com/GeorgesZam)  
    🔗 [Connectons-nous sur LinkedIn](https://www.linkedin.com/in/georges-zam-6aa2b3332/)
</div>
""", unsafe_allow_html=True)

# Section Contact avec formulaire interactif
st.header("📬 Contact Rapide")
with st.form(key='contact_form'):
    col6, col7 = st.columns(2)
    with col6:
        name = st.text_input("Nom complet")
    with col7:
        email = st.text_input("Email professionnel")
    
    message = st.text_area("Votre message (soyez spécifique sur vos besoins techniques)")
    submit_button = st.form_submit_button("Envoyer →")
    
    if submit_button:
        st.success(f"Merci {name}! Votre demande concernant **{message[:30]}...** a bien été envoyée")

# Footer avec éléments sociaux
st.markdown("---")
st.markdown("""
<div style="text-align: center">
    <p>📌 Disponible pour des défis techniques complexes - Dernière mise à jour : Février 2025</p>
    <div style="display: flex; gap: 2rem; justify-content: center">
        <a href="https://github.com/GeorgesZam"><img src="https://img.icons8.com/3d-fluency/50/000000/github.png" width=40></a>
        <a href="https://www.linkedin.com/in/georges-zam-6aa2b3332/"><img src="https://img.icons8.com/3d-fluency/50/000000/linkedin.png" width=40></a>
        <a href="mailto:zamgeorges0@gmail.com"><img src="https://img.icons8.com/3d-fluency/50/000000/gmail.png" width=40></a>
    </div>
    <p style="margin-top: 1rem">© 2025 Georges Zam - Tous droits réservés</p>
</div>
""", unsafe_allow_html=True)
