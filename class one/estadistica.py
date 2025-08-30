import pandas as pd

# Cargar el DataFrame de ventas
try:
    df_ventas = pd.read_csv('ventas.csv')
    print("DataFrame de ventas cargado:")
    print(df_ventas.head())
except FileNotFoundError:
    print("Error: 'ventas.csv' no encontrado. Asegúrate de que el archivo existe y está en la ubicación correcta.")
    # Salir o manejar el error si el archivo no se carga
    exit()
    

print("\n--- Estadísticas Descriptivas ---")

# 1. Resumen estadístico de columnas numéricas (count, mean, std, min, 25%, 50%, 75%, max)
print("\nResumen estadístico de 'Ventas' (df.describe()):")
print(df_ventas['Ventas'].describe())

# Resumen para todo el DataFrame (solo columnas numéricas)
print("\nResumen estadístico de todo el DataFrame (df.describe()):")
print(df_ventas.describe())

# 2. Conteo de valores únicos en una columna
print("\nConteo de productos por 'Categoria' (df['Categoria'].value_counts()):")
print(df_ventas['Categoria'].value_counts())

print("\nConteo de productos por 'Region':")
print(df_ventas['Region'].value_counts())

# 3. Mediana, Moda, Cuartiles
print("\nMediana de Ventas:", df_ventas['Ventas'].median())
print("Moda de la Región (el valor más frecuente):", df_ventas['Region'].mode()[0]) # mode() puede devolver múltiples valores
print("Cuartil 25% de Ventas:", df_ventas['Ventas'].quantile(0.25))
print("Cuartil 75% de Ventas:", df_ventas['Ventas'].quantile(0.75))


print("\n--- Detección y Manejo de Duplicados ---")

data_duplicados = {
    'ID': [1, 2, 3, 1, 4, 2],
    'Nombre': ['A', 'B', 'C', 'A', 'D', 'B'],
    'Valor': [100, 200, 300, 100, 400, 200]
}
df_duplicados = pd.DataFrame(data_duplicados)
print("\nDataFrame original con duplicados:")
print(df_duplicados)

# 1. Identificar filas duplicadas (devuelve una Serie booleana)
# `keep='first'` (por defecto): marca como True todos excepto la primera ocurrencia del duplicado
# `keep='last'`: marca como True todos excepto la última ocurrencia
# `keep=False`: marca como True todas las ocurrencias duplicadas
es_duplicado = df_duplicados.duplicated()
print("\n¿Es cada fila un duplicado? (keep='first'):")
print(es_duplicado)

# Mostrar las filas que son duplicados (excluyendo la primera aparición)
print("\nFilas duplicadas (excluyendo la primera aparición):")
print(df_duplicados[es_duplicado])

# 2. Eliminar filas duplicadas
df_sin_duplicados = df_duplicados.drop_duplicates()
print("\nDataFrame sin duplicados (keep='first' por defecto):")
print(df_sin_duplicados)

# Eliminar duplicados considerando solo un subconjunto de columnas
# Por ejemplo, eliminar si 'ID' Y 'Nombre' son duplicados, manteniendo el primero
df_duplicados_subconjunto = df_duplicados.drop_duplicates(subset=['ID', 'Nombre'])
print("\nDataFrame sin duplicados en 'ID' y 'Nombre':")
print(df_duplicados_subconjunto)