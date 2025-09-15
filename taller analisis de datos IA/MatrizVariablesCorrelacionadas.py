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

# ==============================
# 4. Matriz de Variables Correlacionadas
# ==============================
print("\n--- 4. Matriz de Variables Correlacionadas ---")

# Usar solo columnas numéricas para evitar errores
numeric_df = df.select_dtypes(include="number")

# Matriz de correlación (Pearson por defecto)
correlation_matrix = numeric_df.corr()
print("\nMatriz de Correlación (primeras filas):")
print(correlation_matrix.head())

# Heatmap de correlación (triángulo superior para mejor lectura)
plt.figure(figsize=(12, 10))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(
    correlation_matrix,
    mask=mask,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=.5,
    square=True
)
plt.title('Matriz de Correlación de Variables')
plt.tight_layout()
plt.show()
