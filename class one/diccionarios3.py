def mostrar_informacion_estudiante(estudiante):
    """
    Función para mostrar toda la información de un estudiante
    de manera organizada
    """
    print("=== INFORMACIÓN DEL ESTUDIANTE ===")
    for seccion, datos in estudiante.items():
        print(f"\n{seccion.upper().replace('_', ' ')}:")
        if isinstance(datos, dict):
            for clave, valor in datos.items():
                if isinstance(valor, dict):
                    print(f"  {clave}:")
                    for sub_clave, sub_valor in valor.items():
                        print(f"    {sub_clave}: {sub_valor}")
                elif isinstance(valor, list):
                    print(f"  {clave}: {', '.join(map(str, valor))}")
                else:
                    print(f"  {clave}: {valor}")
        else:
            print(f"  {datos}")

# Ejemplo de diccionario estudiante_completo
estudiante_completo = {
    "datos_personales": {
        "nombre": "Luis Pérez",
        "edad": 21,
        "direccion": "Calle  123"
    },
    "academico": {
        "carrera": "Ingeniería de Sistemas",
        "semestre": 5,
        "materias": ["Matemáticas", "Programación", "Física"]
    },
    "contacto": {
        "email": "luis.perez@example.com",
        "telefono": "555-1234"
    }
}

# Usar la función con el diccionario definido
mostrar_informacion_estudiante(estudiante_completo)
