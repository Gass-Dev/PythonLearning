import streamlit as st
import pandas

df = pandas.read_csv("data.csv")


# Configuration de la page
st.set_page_config(
    page_title="Dashboard Marketing Gwen",
    page_icon="🚀",
    layout="wide"
)


# # Sélectionner les lignes dont l'âge est supérieur à 50 et les Hommes
# st.write(df[(df.Age > 50) & (df.Gender == 'Male')])


st.title("Votre Dashboard interactif avec Streamlit 🎨")

st.subheader("Bienvenue sur votre Dashboard")
st.text("Bienvenue sur notre plateforme interactive qui vous permettra d'explorer et d'analyser des données de manière intuitive. Ce Dashboard a été spécialement conçu pour vous aider à mieux comprendre les concepts clés de la data science et à acquérir une expérience pratique en utilisant Streamlit.")

st.subheader("Comment utiliser Streamlit ?")
st.text("Voici les quelques commandes de base pour utiliser Streamlit :")

st.subheader("Titre et texte")
st.markdown("st.title('Title') : pour afficher un titre")
st.markdown("st.markdown('Some text') : pour afficher du texte")
st.markdown("st.write(data) ou st.dataframe(df) : pour afficher des données")

st.subheader("Widgets")
st.markdown("st.checkbox('Show raw data') : pour afficher des données brutes")
st.markdown("st.selectbox('Choose a city',('London','New York','San Francisco')) : pour afficher une liste déroulante")
st.markdown("st.button('Submit') : pour afficher un bouton de soumission")


st.subheader("Afficher des graphiques")
st.markdown("st.line_chart(data) : pour afficher un graphique linéaire")
st.markdown("st.bar_chart(data) : pour afficher un graphique à barres")
st.markdown("st.pyplot(fig) : pour afficher un graphique matplotlib")
st.markdown("st.map(data) : pour afficher une carte")

st.subheader("Affichage des donnees brutes")
# Checkbox
if st.checkbox("Afficher les données brutes"):
    st.write(df)


st.subheader("Affichage dynamique des donnees")
# Columns 
col1, col2= st.columns(2)
with col1:
    st.title("1️⃣ Example de widget")
    # Selectbox 1
    number = st.selectbox("Sélectionnez la Profession", ['Artist', 'Doctor', 'Engineer', 'Entertainment', 'Executive', 'Healthcare'])
    st.write("Vous avez choisi le nombre", number)
    # Selectbox 2
    number = st.selectbox("Sélectionnez un critère", ['Age', 'Work_Experience', 'Family_Size', 'Entertainment', 'Executive', 'Healthcare'])
    st.write("Vous avez choisi le nombre", number)

with col2:
    st.title("Exemple de widget formulaire")
    form = st.form(key="my_form")
    number = form.selectbox("Sélectionnez un critère", ['Ever_Married', 'Graduated'])
    number = form.selectbox("Sélectionnez une valeur", ['Yes', 'No'])
    number = form.selectbox("Sélectionnez l'âge minimum", ['18', '23', '28', '33', '38', '43'])
    number = form.selectbox("Sélectionnez la taille minimum du foyer", ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    bouton = form.form_submit_button(label="Soumettre")

# with col2:
#     st.title("Example de widget form")
#     # Input user
#     user_input = st.text_input("Entrez votre nom")
#     st.write("Vous avez entré", user_input)

#     # Slider
#     age = st.slider("Entrez votre âge", 1, 100)
#     st.write("Vous avez", age, "ans")


# with col3:
#     st.title("Col 3")
#     form = st.form(key="my_form")

#     with form:
#         st.title("My Form")
#         bouton = st.form_submit_button(label="Submit")

#         if bouton:
#             st.write('Moyenne des âges :', df.Age.mean())