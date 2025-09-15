# ==============================
# 1. Importar librerías
# ==============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# 2. Cargar el dataset Titanic
# ==============================
titanic_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(titanic_url)

# Mostrar confirmación
print("--- Dataset Titanic cargado ---")
print(df.head())


print("\n--- 3. Estadísticas Relevantes ---")

# Estadísticas descriptivas del DataFrame limpio
print("\nEstadísticas descriptivas del DataFrame limpio:")
print(df.describe())

# Distribución de la variable objetivo 'Survived'
print("\nDistribución de la variable 'Survived' (0: No Sobrevive, 1: Sobrevive):")
print(df['Survived'].value_counts())
print("\nProporción de la variable 'Survived':")
print(df['Survived'].value_counts(normalize=True))  # proporción

# Estadísticas de supervivencia por género
print("\nEstadísticas de supervivencia por género (0: Femenino, 1: Masculino):")
print(df.groupby('Sex')['Survived'].mean())

# Estadísticas de supervivencia por clase de pasajero (Pclass)
print("\nEstadísticas de supervivencia por clase de pasajero:")
print(df.groupby('Pclass')['Survived'].mean())

# Estadísticas de supervivencia por puerto de embarque
embarked_cols = [col for col in df.columns if 'Embarked_' in col]
if embarked_cols:
    print("\nEstadísticas de supervivencia por puerto de embarque:")
    print("Se generarán visualizaciones en la siguiente sección.")
else:
    print("\nLas columnas de Embarked no se encontraron para el análisis. "
          "Revisa el paso de one-hot encoding en la limpieza.")

# Distribución de la edad de los pasajeros
print("\nDistribución de la edad de los pasajeros:")
print(df['Age'].describe())
