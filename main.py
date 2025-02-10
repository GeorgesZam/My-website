import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Georges Zam - CV Interactif",
    page_icon="📄",
    layout="wide"
)

# CSS personnalisé pour un design moderne
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;500&family=Inter:wght@400;600&display=swap');

    .main {
        background-color: #F8FAFC;
        color: #0F172A;
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        color: #1E3A8A;
        font-family: 'Roboto Mono', monospace;
    }

    .card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid #E2E8F0;
    }

    .card:hover {
        transform: translateY(-5px);
        transition: transform 0.3s ease;
    }

    .skill-badge {
        display: inline-block;
        background: #1E3A8A;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin: 0.25rem;
        font-size: 0.9rem;
    }

    .link-button {
        display: inline-block;
        background: #1E3A8A;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-decoration: none;
        margin: 0.5rem 0;
    }

    .link-button:hover {
        background: #0F172A;
    }
</style>
""", unsafe_allow_html=True)

# Header avec photo et titre
col1, col2 = st.columns([1, 3], gap="medium")
with col1:
    st.image("https://media.licdn.com/dms/image/v2/D4E03AQEd8bYIj96nvA/profile-displayphoto-shrink_400_400/B4EZSYkmgHHAAk-/0/1737726519746?e=1744848000&v=beta&t=xmK-gWog2EqFwPy6wQU9o6h9lai9_HG8rxaT8gZgJCY", width=150)  # Remplacez par votre photo

with col2:
    st.markdown("# Georges Zam")
    st.markdown("**Ingénieur Informatique | Data, IA et Développement Logiciel**")
    st.markdown("📅 Recherche un stage de 3-4 mois à partir d'avril 2025")
    st.markdown("📍 CESI Nanterre, France")

# Section Objectif
st.markdown("## 🎯 Objectif")
with st.container():
    st.markdown("""
    <div class="card">
        Je recherche un stage dans les domaines de l'informatique, de la data science, de l'intelligence artificielle, et du développement logiciel. 
        Je suis ouvert à des missions techniques variées et à des responsabilités liées au développement de systèmes informatiques. 
        À l'issue de ce stage, je suis également intéressé par une opportunité d'alternance.
    </div>
    """, unsafe_allow_html=True)

# Section Formation
st.markdown("## 🎓 Formation")
with st.container():
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class="card">
            <h3>CESI Nanterre, France</h3>
            <p><strong>2023 – Présent</strong></p>
            <ul>
                <li>2ème année (Informatique) : Microcontrôleurs, POO, réseaux, développement web</li>
                <li>1ère année (Généraliste) : Traitement du signal, mécanique, BTP, électronique</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
        <div class="card">
            <h3>Lycée Alain, Le Vésinet</h3>
            <p><strong>2016 – 2023</strong></p>
            <ul>
                <li>Baccalauréat scientifique, spécialité mathématiques (expert)</li>
                <li>Physique, chimie, et informatique</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Section Expérience Professionnelle
st.markdown("## 💼 Expérience Professionnelle")
with st.container():
    st.markdown("""
    <div class="card">
        <h3>Médaille d'argent au WorldSkills 2025 IDF</h3>
        <p><strong>2024 – Présent</strong></p>
        <ul>
            <li>Solutions logicielles pour entreprise</li>
            <li>Vice-Président du CESI AERO Club</li>
            <li>Conception et lancement d'une fusée</li>
            <li>Compétitions d'hovercrafts (1ère place)</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Section Compétences
st.markdown("## 🛠️ Compétences Techniques")
with st.container():
    st.markdown("""
    <div class="card">
        <h3>Langages de programmation</h3>
        <span class="skill-badge">Python</span>
        <span class="skill-badge">C/C++</span>
        <span class="skill-badge">Java</span>
        <span class="skill-badge">Bash</span>
        <span class="skill-badge">SQL</span>
        <span class="skill-badge">HTML/CSS/JS</span>
    </div>
    <div class="card">
        <h3>AI & Data Science</h3>
        <span class="skill-badge">PyTorch</span>
        <span class="skill-badge">Scikit-learn</span>
        <span class="skill-badge">Hugging Face</span>
        <span class="skill-badge">Kaggle</span>
    </div>
    """, unsafe_allow_html=True)

# Section Liens
st.markdown("## 🔗 Liens")
with st.container():
    st.markdown("""
    <div class="card">
        <a href="https://github.com/GeorgesZam" class="link-button">GitHub</a>
        <a href="https://www.linkedin.com/in/georges-zam-6aa2b3332/" class="link-button">LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("© 2025 - Georges Zam | CV Interactif")
