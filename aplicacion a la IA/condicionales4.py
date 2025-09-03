"""
Ejercicio 2: Clasificador de Triángulos
Objetivo: Determinar el tipo de triángulo basado en las longitudes de sus lados
"""

print("=== CLASIFICADOR DE TRIÁNGULOS ===")

# Función para validar entrada numérica positiva
def obtener_lado(numero):
    while True:
        try:
            lado = float(input(f"Ingrese la longitud del lado {numero}: "))
            if lado > 0:
                return lado
            else:
                print("La longitud debe ser un número positivo")
        except ValueError:
            print("Debe ingresar un número válido")

# Obtener las longitudes de los lados
print("Ingrese las longitudes de los tres lados del triángulo:")
lado_a = obtener_lado(1)
lado_b = obtener_lado(2)
lado_c = obtener_lado(3)

print(f"\nLados ingresados: {lado_a}, {lado_b}, {lado_c}")

# Verificar si forman un triángulo válido (desigualdad triangular)
if (lado_a + lado_b > lado_c) and (lado_a + lado_c > lado_b) and (lado_b + lado_c > lado_a):
    print("✓ Las longitudes forman un triángulo válido")

    # Clasificar por lados (equilátero, isósceles, escaleno)
    if lado_a == lado_b == lado_c:
        tipo_lados = "Equilátero"
        descripcion_lados = "Todos los lados son iguales"
    elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        tipo_lados = "Isósceles"
        descripcion_lados = "Dos lados son iguales"
    else:
        tipo_lados = "Escaleno"
        descripcion_lados = "Todos los lados son diferentes"

    # Clasificar por ángulos (usando teorema de Pitágoras)
    # Ordenar los lados para facilitar el cálculo
    lados = sorted([lado_a, lado_b, lado_c])
    lado_menor, lado_medio, lado_mayor = lados

    # Calcular el cuadrado de los lados
    cuadrado_menor = lado_menor ** 2
    cuadrado_medio = lado_medio ** 2
    cuadrado_mayor = lado_mayor ** 2

    # Clasificar por ángulos
    if abs(cuadrado_menor + cuadrado_medio - cuadrado_mayor) < 0.0001:  # margen de error flotante
        tipo_angulos = "Rectángulo"
        descripcion_angulos = "Tiene un ángulo de 90 grados"
    elif cuadrado_menor + cuadrado_medio > cuadrado_mayor:
        tipo_angulos = "Acutángulo"
        descripcion_angulos = "Todos los ángulos son menores a 90 grados"
    else:
        tipo_angulos = "Obtusángulo"
        descripcion_angulos = "Tiene un ángulo mayor a 90 grados"

    # Calcular perímetro y área (fórmula de Herón)
    perimetro = lado_a + lado_b + lado_c
    s = perimetro / 2  # Semi-perímetro
    area = (s * (s - lado_a) * (s - lado_b) * (s - lado_c)) ** 0.5

    # Mostrar resultados
    print(f"\n=== CLASIFICACIÓN DEL TRIÁNGULO ===")
    print(f"Por lados: {tipo_lados}")
    print(f" → {descripcion_lados}")
    print(f"Por ángulos: {tipo_angulos}")
    print(f" → {descripcion_angulos}")

    print(f"\n=== PROPIEDADES ===")
    print(f"Perímetro: {perimetro:.2f} unidades")
    print(f"Área: {area:.2f} unidades cuadradas")

    # Información adicional según el tipo
    if tipo_lados == "Equilátero":
        print(f"\n📐 Información adicional:")
        print(f" • Todos los ángulos miden 60°")
        print(f" • Es también un triángulo acutángulo")
        print(f" • Altura: {(lado_a * (3**0.5)) / 2:.2f} unidades")

    elif tipo_angulos == "Rectángulo":
        print(f"\n📐 Información adicional:")
        print(f" • La hipotenusa mide {lado_mayor:.2f} unidades")
        print(f" • Los catetos miden {lado_menor:.2f} y {lado_medio:.2f} unidades")
        print(f" • Área también = (cateto1 × cateto2) / 2 = {(lado_menor * lado_medio) / 2:.2f}")

else:
    print("❌ Las longitudes NO forman un triángulo válido")
    print("Recuerda: La suma de dos lados debe ser mayor que el tercer lado")

    # Mostrar qué condición falla
    if lado_a + lado_b <= lado_c:
        print(f" • {lado_a} + {lado_b} = {lado_a + lado_b} ≤ {lado_c}")
    if lado_a + lado_c <= lado_b:
        print(f" • {lado_a} + {lado_c} = {lado_a + lado_c} ≤ {lado_b}")
    if lado_b + lado_c <= lado_a:
        print(f" • {lado_b} + {lado_c} = {lado_b + lado_c} ≤ {lado_a}")
