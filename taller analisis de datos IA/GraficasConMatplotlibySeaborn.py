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

# Preprocesamiento mínimo (igual que en limpieza de datos)
df = df.drop('Cabin', axis=1)  # eliminar Cabin
df['Age'] = df['Age'].fillna(df['Age'].median())  # imputar Age
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # imputar Embarked
df = df.drop(['PassengerId', 'Name'], axis=1)  # eliminar columnas irrelevantes
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1}).astype(int)  # convertir Sex a numérico
df = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked', drop_first=True)  # one-hot encoding


# ==============================
# 5. Gráficas con Matplotlib y Seaborn
# ==============================
print("\n--- 5. Gráficas con Matplotlib y Seaborn ---")

# 5.1 Distribución de la edad (Histograma + KDE)
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], kde=True, bins=30)
plt.title('Distribución de la Edad de los Pasajeros')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()

# 5.2 Tasa de Supervivencia por género
plt.figure(figsize=(7, 5))
sns.barplot(x='Sex', y='Survived', data=df, errorbar=None)  # 0=female, 1=male
plt.title('Tasa de Supervivencia por Género')
plt.xlabel('Género (0: Femenino, 1: Masculino)')
plt.ylabel('Tasa de Supervivencia')
plt.xticks(ticks=[0, 1], labels=['Femenino', 'Masculino'])
plt.tight_layout()
plt.show()

# 5.3 Tasa de Supervivencia por clase de pasajero (Pclass)
plt.figure(figsize=(7, 5))
sns.barplot(x='Pclass', y='Survived', data=df, errorbar=None)
plt.title('Tasa de Supervivencia por Clase de Pasajero')
plt.xlabel('Clase de Pasajero')
plt.ylabel('Tasa de Supervivencia')
plt.tight_layout()
plt.show()

# 5.4 Tasa de Supervivencia por puerto de embarque (usando one-hot)
if {'Embarked_Q', 'Embarked_S'}.issubset(df.columns):
    # C = no Q y no S
    mask_C = (df['Embarked_Q'] == 0) & (df['Embarked_S'] == 0)
    mask_Q = df['Embarked_Q'] == 1
    mask_S = df['Embarked_S'] == 1

    embarked_survival = pd.DataFrame({
        'Port': ['C', 'Q', 'S'],
        'Survived_Rate': [
            df.loc[mask_C, 'Survived'].mean(),
            df.loc[mask_Q, 'Survived'].mean(),
            df.loc[mask_S, 'Survived'].mean()
        ]
    })

    plt.figure(figsize=(7, 5))
    sns.barplot(x='Port', y='Survived_Rate', data=embarked_survival, errorbar=None)
    plt.title('Tasa de Supervivencia por Puerto de Embarque')
    plt.xlabel('Puerto de Embarque')
    plt.ylabel('Tasa de Supervivencia')
    plt.tight_layout()
    plt.show()
else:
    print("\n[Aviso] No se encontraron columnas 'Embarked_Q' y 'Embarked_S'. "
          "Revisa el one-hot encoding del paso de limpieza.")

# 5.5 Dispersión Age vs Fare (color por Survived)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, alpha=0.7)
plt.title('Relación entre Edad, Tarifa y Supervivencia')
plt.xlabel('Edad')
plt.ylabel('Tarifa')
plt.legend(title='Supervivencia')
plt.tight_layout()
plt.show()

# 5.6 Box plot de la tarifa por clase de pasajero
plt.figure(figsize=(10, 6))
sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('Distribución de la Tarifa por Clase de Pasajero')
plt.xlabel('Clase de Pasajero')
plt.ylabel('Tarifa')
plt.tight_layout()
plt.show()
