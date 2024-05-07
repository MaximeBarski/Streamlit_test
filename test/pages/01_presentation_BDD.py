# Importation des bibliothèques

import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement de la database voitures
st.title("Présentation de la base de données : ")

# Affichage de la database
link = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'
df = pd.read_csv(link)
df

# Création du dictionnaire des variables

st.markdown("__Description des variables__ :  \n  - ___mpg___ (miles per gallon) : la consommation d'essence d'une voiture. \n - ___cylinders___ : le nombre de cylindres du moteur.  \n - ___cubicinches___ (cylindrée): le volume interne du moteur à combustion (souvent en cm3).  \n - ___hp___ (horsepower) : la puissance du moteur en chevaux.  \n - ___weightlbs___ : le poids de la voiture.  \n - ___time-to-60___ (accélération) : la durée en seconde pour passer de l'arrêt (0 km/h) à 60 mph (environ 97 km/h).  \n - ___year___ : l'année de production du modèle.  \n - ___continent___ : origine des constructeurs.")
