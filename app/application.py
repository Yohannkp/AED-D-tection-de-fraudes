import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Charger les données
@st.cache_data
def load_data():
    file_path = "../creditcard.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Titre de l'application
st.title("📊 Analyse Exploratoire des Données - Fraude Bancaire")

# Afficher un aperçu des données
st.subheader("🔍 Aperçu des données")
st.write(df.head())

# Afficher les dimensions des données
st.write(f"**Nombre de lignes:** {df.shape[0]} | **Nombre de colonnes:** {df.shape[1]}")

# Sélection d'un type d'analyse
option = st.sidebar.selectbox("Sélectionner une analyse", 
                              ["Distribution des classes", "Histogramme des montants", "Boxplot des montants", "Matrice de corrélation"])

if option == "Distribution des classes":
    st.subheader("📌 Répartition des transactions (fraude vs normale)")
    fig, ax = plt.subplots()
    sns.countplot(x=df["Class"], palette="coolwarm", ax=ax)
    ax.set_title("Répartition des transactions normales vs frauduleuses")
    st.pyplot(fig)

elif option == "Histogramme des montants":
    st.subheader("📊 Distribution des montants des transactions")
    fig, ax = plt.subplots()
    sns.histplot(df["Amount"], bins=50, kde=True, color="blue", ax=ax)
    ax.set_title("Distribution des montants des transactions")
    ax.set_xlabel("Montant")
    ax.set_ylabel("Fréquence")
    st.pyplot(fig)

elif option == "Boxplot des montants":
    st.subheader("📌 Boxplot des montants des transactions")
    fig, ax = plt.subplots()
    sns.boxplot(x=df["Amount"], ax=ax)
    ax.set_title("Boxplot du montant des transactions")
    st.pyplot(fig)

elif option == "Matrice de corrélation":
    st.subheader("📊 Matrice de corrélation")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(df.corr(), cmap="coolwarm", annot=False, linewidths=0.5, ax=ax)
    ax.set_title("Matrice de corrélation des variables")
    st.pyplot(fig)

st.sidebar.write("📌 Sélectionnez une analyse dans le menu déroulant pour afficher les graphiques.")
