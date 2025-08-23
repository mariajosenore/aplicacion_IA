# Base de datos de estudiantes con sus calificaciones
estudiantes_db = {
    1001: {
        "nombre": "Carlos Mendoza",
        "materias": {
            "Matemáticas": [4.5, 3.8, 4.2],
            "Física": [4.0, 4.3, 3.9],
            "Programación": [4.8, 4.5, 4.7]
        }
    },
    1002: {
        "nombre": "Lucía Herrera",
        "materias": {
            "Matemáticas": [4.2, 4.0, 4.1],
            "Física": [3.8, 4.2, 4.0],
            "Programación": [4.6, 4.4, 4.8]
        }
    },
    1003: {
        "nombre": "Pedro Ramírez",
        "materias": {
            "Matemáticas": [3.5, 3.8, 3.6],
            "Física": [3.9, 3.7, 4.0],
            "Programación": [4.1, 3.9, 4.3]
        }
    }
}

def calcular_promedio_materia(notas):
    """Calcula el promedio de una lista de notas"""
    return sum(notas) / len(notas) if notas else 0

def calcular_promedio_general(materias):
    """Calcula el promedio general de todas las materias"""
    promedios = []
    for notas in materias.values():
        promedio_materia = calcular_promedio_materia(notas)
        promedios.append(promedio_materia)
    return sum(promedios) / len(promedios) if promedios else 0

def mostrar_reporte_estudiante(codigo_estudiante):
    """Muestra un reporte completo de un estudiante"""
    if codigo_estudiante not in estudiantes_db:
        print(f"Error: No se encontró el estudiante con código {codigo_estudiante}")
        return

    estudiante = estudiantes_db[codigo_estudiante]
    nombre = estudiante["nombre"]
    materias = estudiante["materias"]

    print(f"\n=== REPORTE ACADÉMICO ===")
    print(f"Estudiante: {nombre}")
    print(f"Código: {codigo_estudiante}")
    print(f"{'='*40}")

# Ejemplo de llamada a la función
mostrar_reporte_estudiante(1001)
