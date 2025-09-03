"""
EJERCICIO INTEGRADOR 1: SISTEMA DE GESTIÓN DE BIBLIOTECA
Objetivo: Crear un sistema completo que demuestre el uso de todos los conceptos
aprendidos:
- Tipos de datos (listas, diccionarios, cadenas, números)
- Entrada y salida de datos
- Estructuras condicionales
- Validación de entrada
- Formateo de salida
"""

print("=" * 60)
print(" SISTEMA DE GESTIÓN DE BIBLIOTECA UNIVERSITARIA")
print("=" * 60)

# Base de datos de libros (lista de diccionarios)
biblioteca = [
    {
        "id": 1,
        "titulo": "Introducción a Python",
        "autor": "Guido van Rossum",
        "año": 2020,
        "categoria": "Programación",
        "disponible": True,
        "prestamos": 15
    },
    {
        "id": 2,
        "titulo": "Algoritmos y Estructuras de Datos",
        "autor": "Thomas Cormen",
        "año": 2018,
        "categoria": "Ciencias de la Computación",
        "disponible": True,
        "prestamos": 23
    },
    {
        "id": 3,
        "titulo": "Inteligencia Artificial Moderna",
        "autor": "Stuart Russell",
        "año": 2019,
        "categoria": "Inteligencia Artificial",
        "disponible": False,
        "prestamos": 31
    },
    {
        "id": 4,
        "titulo": "Bases de Datos Relacionales",
        "autor": "Ramez Elmasri",
        "año": 2017,
        "categoria": "Bases de Datos",
        "disponible": True,
        "prestamos": 18
    }
]

# Lista de usuarios registrados
usuarios_registrados = ["juan.perez", "ana.garcia", "carlos.lopez", "maria.rodriguez"]


def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    print("\n" + "=" * 40)
    print(" MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. Consultar catálogo de libros")
    print("2. Buscar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Registrar nuevo libro")
    print("6. Estadísticas de la biblioteca")
    print("7. Salir")
    print("-" * 40)


def validar_opcion_menu(min_opcion, max_opcion):
    """Valida que la opción del menú esté en el rango correcto"""
    while True:
        try:
            opcion = int(input(f"Seleccione una opción ({min_opcion}-{max_opcion}): "))
            if min_opcion <= opcion <= max_opcion:
                return opcion
            else:
                print(f"Error: Debe seleccionar una opción entre {min_opcion} y {max_opcion}")
        except ValueError:
            print("Error: Debe ingresar un número entero válido")


def mostrar_catalogo():
    """Muestra todos los libros en el catálogo"""
    print("\n" + "=" * 80)
    print(" CATÁLOGO DE LIBROS")
    print("=" * 80)

    if not biblioteca:
        print("No hay libros en la biblioteca.")
        return

    # Encabezado de la tabla
    print(f"{'ID':<3} {'Título':<30} {'Autor':<20} {'Año':<6} {'Estado':<12} {'Préstamos':<10}")
    print("-" * 80)

    # Mostrar cada libro
    for libro in biblioteca:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"{libro['id']:<3} {libro['titulo']:<30} {libro['autor']:<20} "
              f"{libro['año']:<6} {estado:<12} {libro['prestamos']:<10}")

    print("-" * 80)
    print(f"Total de libros: {len(biblioteca)}")

    # Estadísticas rápidas
    disponibles = sum(1 for libro in biblioteca if libro["disponible"])
    prestados = len(biblioteca) - disponibles
    print(f"Disponibles: {disponibles} | Prestados: {prestados}")


# (El resto del código sigue igual, solo con buena indentación)
