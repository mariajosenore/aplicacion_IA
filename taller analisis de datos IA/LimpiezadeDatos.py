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


print("\n--- 2. Limpieza de Datos ---")

# Identificar valores perdidos
print("\nCantidad de valores perdidos por columna:")
print(df.isnull().sum())

# Visualizar la distribución de valores perdidos
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Mapa de Calor de Valores Perdidos')
plt.show()

# Manejo de valores perdidos

# 1. Columna 'Cabin': demasiados valores perdidos → eliminar
print("\nEliminando la columna 'Cabin' debido a la alta cantidad de valores perdidos...")
df = df.drop('Cabin', axis=1)

# 2. Columna 'Age': imputar con la mediana
print("Imputando los valores perdidos en 'Age' con la mediana...")
df['Age'] = df['Age'].fillna(df['Age'].median())

# 3. Columna 'Embarked': imputar con la moda
print("Imputando los valores perdidos en 'Embarked' con la moda...")
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Verificar nuevamente los valores perdidos
print("\nCantidad de valores perdidos después de la limpieza:")
print(df.isnull().sum())

# Eliminar columnas irrelevantes
print("Eliminando la columna 'PassengerId'...")
df = df.drop('PassengerId', axis=1)

print("Eliminando la columna 'Name'...")
df = df.drop('Name', axis=1)

# Convertir 'Sex' a valores numéricos
print("Convirtiendo la columna 'Sex' a valores numéricos (0: female, 1: male)...")
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1}).astype(int)

# Codificar 'Embarked' con One-Hot Encoding
print("Codificando la columna 'Embarked' usando One-Hot Encoding...")
df = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked', drop_first=True)

# Ver las primeras filas del DataFrame limpio
print("\nDataFrame después de la limpieza y preprocesamiento de 'Sex' y 'Embarked':")
print(df.head())
