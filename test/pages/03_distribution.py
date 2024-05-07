# Importation des bibliothèques

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Chargement de la database voitures
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df = pd.read_csv(link)

st.title("Analyse de distribution :")

# Sélectionnez la colonne 'continent'
selected_continent = st.selectbox("Sélectionnez un continent :", df['continent'].unique())

# Filtrer le DataFrame en fonction du continent sélectionné
df_filtered = df[df['continent'] == selected_continent]

# Création des graphiques de distribution des différentes variables

# MPG
st.header("Distribution de la variable mpg : ", divider = "blue")
plt.figure(figsize=(10, 6))
viz_distribution_mpg = sns.displot(df_filtered['mpg'],
                                   kde=True)
st.pyplot(viz_distribution_mpg.figure)
st.write("La distribution de la consommation d'essence varie selon le continent. Elle est plus élevée aux US comparé à l'Europe et au Japon.")


# cylinders
st.header("Distribution de la variable cylinders : ", divider = "blue")
plt.figure(figsize=(10, 6))
plt.pie(df_filtered["cylinders"].value_counts(), autopct='%1.1f%%')
plt.legend(df_filtered["cylinders"].unique())
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(plt)
st.write("On constate que la répartition de la cylindrée est principalement de valeur 4 en Europe et au Japon.")


# Afficher le titre
st.header("Violin Plot pour les variables sélectionnées : ", divider = "blue")

# Créer un violin plot avec Seaborn pour les variables sélectionnées
selected_variables = ["mpg", "hp"]
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_filtered[selected_variables], inner="quartile")
plt.xlabel("Variables")
plt.ylabel("Valeurs")
st.pyplot(plt)