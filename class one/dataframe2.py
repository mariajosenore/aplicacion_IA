import pandas as pd

# URL del conjunto de datos del Titanic
titanic_url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

# Reemplaza el dataframe con el de Titanic
df = pd.read_csv(titanic_url)

# Imprime las primeras 5 filas para verificar
print("Dataframe de Titanic cargado:")
print(df.head())