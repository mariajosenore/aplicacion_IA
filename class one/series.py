import pandas as pd
import numpy as np # Necesario para crear una Serie desde un array NumPy

print("--- Creación de Series ---")
print("--- Serie desde lista ---")

# 1. Desde una lista de Python
data_lista = [10, 20, 30, 40, 50]
serie_a = pd.Series(data_lista)
print("\nSerie desde lista:")
print(serie_a)
# Observa el índice numérico por defecto (0, 1, 2, ...)


# # 2. Desde un array de NumPy
# print("--- Serie desde array NumPy ---")

# data_numpy = np.array([1.5, 2.8, 3.1, 4.0])
# serie_b = pd.Series(data_numpy)
# print("\nSerie desde array NumPy:")
# print(serie_b)


# # 3. Desde un diccionario de Python (las claves se convierten en índices)
# print("--- Serie desde diccionario ---")

# data_diccionario = {'a': 100, 'b': 200, 'c': 300}
# serie_c = pd.Series(data_diccionario)
# print("\nSerie desde diccionario:")
# print(serie_c)


# # 4. Creando una Serie con un índice personalizado
# ingredientes = ['harina', 'azúcar', 'huevos', 'leche']
# cantidades = [500, 250, 4, 150] # en gramos/ml
# serie_receta = pd.Series(cantidades, index=ingredientes)
# print("\nSerie con índice personalizado (receta):")
# print(serie_receta)

# print("\n--- Acceso a Elementos de una Serie ---")

# # Usaremos la serie_receta creada anteriormente
# print("Serie de la receta:")
# print(serie_receta)

# # Acceso por índice numérico (como una lista)
# print("\nPrimer ingrediente (índice 0):", serie_receta[0])

# # Acceso por etiqueta de índice
# print("Cantidad de azúcar:", serie_receta['azúcar'])

# # Acceso a múltiples elementos por etiquetas
# print("\nHarina y Huevos:")
# print(serie_receta[['harina', 'huevos']])

# # Acceso a múltiples elementos por índices numéricos
# print("\nLos primeros dos ingredientes (índices 0 y 1):")
# print(serie_receta[0:2]) # Slicing igual que en listas

print("\n===== Operaciones con Series ====")

# Serie de precios
precios = pd.Series([10, 20, 30], index=['Manzana', 'Pera', 'Naranja'])
print("\nPrecios originales:")
print(precios)

# # Multiplicar todos los elementos por un escalar
# precios_dobles = precios * 2
# print("\nPrecios duplicados:")
# print(precios_dobles)

# # Sumar dos Series (alineación por índice)
# impuestos = pd.Series([1, 2, 3], index=['Manzana', 'Pera', 'Naranja'])
# precios_con_impuestos = precios + impuestos
# print("\nPrecios con impuestos:")
# print(precios_con_impuestos)

# # Sumar dos Series con índices no coincidentes (genera NaN)
# descuentos = pd.Series([0.5, 1.0], index=['Manzana', 'Banana'])
# precios_con_descuento = precios - descuentos
# print("\nPrecios con descuentos (observar NaN por falta de alineación):")
# print(precios_con_descuento)
# # ¡Importante! Pandas alinea las operaciones por los índices. Si no coinciden, devuelve NaN (Not a Number).