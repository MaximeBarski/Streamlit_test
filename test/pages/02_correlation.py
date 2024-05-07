# Importation des bibliothèques

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement de la database voitures
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df = pd.read_csv(link)

st.title("Analyse de corrélation :")

# Sélectionnez la colonne 'continent'
selected_continent = st.selectbox("Sélectionnez un continent :", df['continent'].unique())

# Filtrer le DataFrame en fonction du continent sélectionné
df_filtered = df[df['continent'] == selected_continent]


# Création de l'analyse de corrélation
st.header("Matrice de corrélation", divider = "blue")


plt.figure(figsize=(10, 6))
viz_correlation  = sns.heatmap(df_filtered.corr(numeric_only=True),
            cmap = 'coolwarm',
            annot=True,
            square=True, 
            linewidths=.5)
st.pyplot(viz_correlation.figure)

st.subheader("Remarques :")
st.write("Forte corrélation positive : entre les variables cylinder, cubicinches, hp et weightlbs.")
st.write("Forte corrélation négative : mpg avec cylinder, weightlbs, cubicinches et hp.")
st.write("__Attention, ces corrélations varient selon les continents.__")