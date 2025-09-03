def contar_frecuencias(elementos):
    """
    Cuenta la frecuencia de aparición de cada elemento en una lista
    Args:
        elementos (list): Lista de elementos a contar
    Returns:
        dict: Diccionario con elementos como claves y frecuencias como valores
    """
    frecuencias = {}
    for elemento in elementos:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    return frecuencias

def mostrar_estadisticas_frecuencia(frecuencias, titulo="ANÁLISIS DE FRECUENCIAS"):
    """
    Muestra las estadísticas de frecuencia de manera organizada
    """
    print(f"\n{titulo}")
    print("="*50)
    # Ordenar por frecuencia (descendente)
    elementos_ordenados = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    total_elementos = sum(frecuencias.values())
    print(f"Total de elementos: {total_elementos}")
    print(f"Elementos únicos: {len(frecuencias)}")
    print("\nDistribución de frecuencias:")
    print(f"{'Elemento':<15} {'Frecuencia':<12} {'Porcentaje':<10}")
    print("-"*40)
    for elemento, frecuencia in elementos_ordenados:
        porcentaje = (frecuencia / total_elementos) * 100
        print(f"{elemento:<15} {frecuencia:<12} {porcentaje:.1f}%")

# Ejemplo 1: Análisis de frutas
frutas = ['manzana', 'pera', 'naranja', 'manzana', 'uva', 'pera', 'manzana',
          'banana', 'naranja', 'manzana', 'pera', 'uva']
frecuencias_frutas = contar_frecuencias(frutas)
mostrar_estadisticas_frecuencia(frecuencias_frutas, "ANÁLISIS DE FRUTAS")

# Ejemplo 2: Análisis de calificaciones
calificaciones = [4, 5, 3, 4, 5, 2, 4, 3, 5, 4, 3, 4, 5, 3, 4]
frecuencias_notas = contar_frecuencias(calificaciones)
mostrar_estadisticas_frecuencia(frecuencias_notas, "DISTRIBUCIÓN DE CALIFICACIONES")
