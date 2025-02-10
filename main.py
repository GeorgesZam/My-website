import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Georges Zamfiroiu - Stage Ouvrier", layout="wide")

# Titre principal
st.title("Georges Zamfiroiu")
st.subheader("Étudiant en ingénierie informatique à CESI Nanterre")

# Section de présentation
st.markdown("""
Bienvenue sur ma page de présentation ! Je suis actuellement à la recherche d'un stage ouvrier d'une durée de 3 à 4 mois à partir d'avril 2025. Mes compétences dépassent largement mon niveau d'étude, et j'aimerais avoir la chance de vous les démontrer.

**Compétences clés :** 
- Intelligence Artificielle & Data Science
- Développement Python (Machine Learning, NLP)
- Arduino & Tinkercad
- Gestion de projets techniques complexes

[Consultez mon CV](https://www.linkedin.com/in/georges-zam-6aa2b3332/)
""")

# Section des projets
st.header("Projets réalisés")
st.markdown("Vous pouvez découvrir mes projets sur :")
st.markdown("- [Mon GitHub](https://github.com/GeorgesZam)")
st.markdown("- [Mon LinkedIn](https://www.linkedin.com/in/georges-zam-6aa2b3332/)")

# Section de contact
st.header("Contact")
st.markdown("Vous pouvez me contacter par email à **georges.zamfiroiu@example.com** ou via LinkedIn.")

# Footer
st.markdown("---")
st.markdown("© 2025 Georges Zamfiroiu")
