#creacion de listas 
frutas = ["manzana", "banana", "naranja"]
print(frutas)
print(frutas[0])  # manzana

print(frutas[0])  # manzana
print(frutas[-1])  # naranja (índice negativo)

frutas[1] = "pera"
print(frutas)  # ['manzana', 'pera', 'naranja']

frutas.append("sandía")
print(frutas)  # ['manzana', 'pera', 'naranja', 'sandía']

frutas.remove("pera")
print(frutas)  # ['manzana', 'naranja', 'sandía']

frutas.pop()  # Elimina el último
print(frutas)  # ['manzana', 'naranja']

for fruta in frutas:
    print(fruta)

numeros = [5, 2, 9, 1]

numeros.sort()       # Ordena la lista
print(numeros)       # [1, 2, 5, 9]

numeros.reverse()    # Invierte el orden
print(numeros)       # [9, 5, 2, 1]

print(len(numeros))  # 4 (cantidad de elementos)


