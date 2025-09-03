import pandas as pd

# print("--- Creación de DataFrames ---")

# # 1. Desde un diccionario de listas (cada clave es el nombre de una columna)
# data_alumnos = {
#     'Nombre': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Edad': [20, 22, 21, 23],
#     'Carrera': ['Ing. Sistemas', 'Ing. Electrónica', 'Ing. Sistemas', 'Ing. Civil']
# }
# df_alumnos = pd.DataFrame(data_alumnos)
# print("\nDataFrame de alumnos desde diccionario de listas:")
# print(df_alumnos)

# # 2. Desde un diccionario de Series
# edades = pd.Series([25, 30, 35], index=['Juan', 'Maria', 'Pedro'])
# ciudades = pd.Series(['Madrid', 'Barcelona', 'Valencia'], index=['Juan', 'Maria', 'Pedro'])
# data_empleados = {'Edad': edades, 'Ciudad': ciudades}
# df_empleados = pd.DataFrame(data_empleados)
# print("\nDataFrame de empleados desde diccionario de Series:")
# print(df_empleados)

print("\n--- Lectura de Archivos ---")

# Lectura de un archivo CSV
# Asegúrate de que 'ventas.csv' esté en la misma carpeta que tu script Python
try:
    df_ventas = pd.read_csv('ventas.csv')
    print("\nDataFrame de ventas cargado desde 'ventas.csv':")
    print(df_ventas)
except FileNotFoundError:
    print("\nError: 'ventas.csv' no encontrado. Asegúrate de que el archivo existe y está en la ubicación correcta.")
    
 
print("\n--- Exploración Básica del DataFrame de Ventas ---")

# Mostrar las primeras 5 filas (útil para una vista rápida)
print("\nPrimeras 5 filas (df.head()):")
print(df_ventas.head())

# Mostrar las últimas 3 filas
print("\nÚltimas 3 filas (df.tail(3)):")
print(df_ventas.tail(3))

# Información general del DataFrame (tipos de datos, valores no nulos)
print("\nInformación del DataFrame (df.info()):")
df_ventas.info()

# Información general del DataFrame (tipos de datos, valores no nulos)
print("\nInformación del DataFrame (df.describe()):")
print(df_ventas.describe())

# Dimensiones del DataFrame (filas, columnas)
print("\nDimensiones del DataFrame (df.shape):", df_ventas.shape)

# Nombres de las columnas
print("Nombres de las columnas (df.columns):", df_ventas.columns)

# # Índice de las filas
# print("Índice de las filas (df.index):", df_ventas.index)    

# print("\n--- Selección de Columnas ---")

# Seleccionar una sola columna (devuelve una Serie)
productos = df_ventas['Producto']
print("\nColumna 'Producto':")
print(productos.head())
print(type(productos)) # Es una Serie

# Seleccionar múltiples columnas (devuelve un DataFrame)
productos_y_ventas = df_ventas[['Producto', 'Ventas']]
print("\nColumnas 'Producto' y 'Ventas':")
print(productos_y_ventas.head())
print(type(productos_y_ventas)) # Es un DataFrame

print("\n--- Selección de Filas con .iloc[] ---")

# Seleccionar una fila por su índice numérico
fila_0 = df_ventas.iloc[0]
print("\nPrimera fila (iloc[0]):")
print(fila_0)
print(type(fila_0)) # Es una Serie (la fila completa)

# Seleccionar las primeras 3 filas
primeras_3_filas = df_ventas.iloc[0:3] # Similar al slicing de listas
print("\nLas primeras 3 filas (iloc[0:3]):")
print(primeras_3_filas)

# Seleccionar filas y columnas por posición
# Ejemplo: Las columnas 'Producto' (0) y 'Ventas' (3) de las filas 1 y 2
filas_columnas_iloc = df_ventas.iloc[[1, 2], [0, 3]]
print("\nFilas 1 y 2, columnas 'Producto' y 'Ventas' (iloc[[1,2], [0,3]]):")
print(filas_columnas_iloc)

# print("\n--- Selección Condicional (Filtrado) ---")

# # 1. Filas donde 'Ventas' es mayor que 100
# ventas_altas = df_ventas[df_ventas['Ventas'] > 100]
# print("\nVentas mayores a 100:")
# print(ventas_altas)

# # 2. Filas de la 'Categoria' 'Electronica'
# electronica = df_ventas[df_ventas['Categoria'] == 'Electronica']
# print("\nProductos de categoría 'Electronica':")
# print(electronica)

# # 3. Múltiples condiciones (usando & para 'AND', | para 'OR', ~ para 'NOT')
# # Productos de 'Electronica' con ventas mayores a 100
# electronica_ventas_altas = df_ventas[(df_ventas['Categoria'] == 'Electronica') & (df_ventas['Ventas'] > 100)]
# print("\nElectrónica con ventas > 100:")
# print(electronica_ventas_altas)

# # Productos de la región 'Norte' o 'Sur'
# norte_o_sur = df_ventas[(df_ventas['Region'] == 'Norte') | (df_ventas['Region'] == 'Sur')]
# print("\nProductos de la región 'Norte' o 'Sur':")
# print(norte_o_sur)

# # 4. Usando .isin() para múltiples valores en una columna
# # Productos de las categorías 'Electronica' o 'Muebles'
# categorias_especificas = df_ventas[df_ventas['Categoria'].isin(['Electronica', 'Muebles'])]
# print("\nProductos de categorías 'Electronica' o 'Muebles' (todas):")
# print(categorias_especificas) # En este caso, serán todas las filas del DataFrame.


# print("\n--- Añadir y Modificar Columnas ---")
# # Añadir una nueva columna con un valor constante
# df_ventas['Moneda'] = 'USD'
# print("\nDataFrame con columna 'Moneda' añadida:")
# print(df_ventas.head())

# # Añadir una nueva columna basada en operaciones con columnas existentes
# # Suponemos un impuesto del 5%
# df_ventas['Ventas_con_Impuesto'] = df_ventas['Ventas'] * 1.05
# print("\nDataFrame con 'Ventas_con_Impuesto':")
# print(df_ventas.head())

# # Modificar una columna existente (por ejemplo, cambiar la categoría de un producto específico)
# # Primero, identificar el índice de la fila a modificar (ej: el mouse)
# # Si sabes que el Mouse está en el índice 2:
# df_ventas.loc[2, 'Categoria'] = 'Oficina' # Usamos .loc para modificar por etiqueta de fila y columna
# print("\nDataFrame con 'Mouse' en 'Oficina':")
# print(df_ventas.head())

# #descargar nuevo csv
# df_ventas.to_csv('ventas_modificado.csv', index=False)  