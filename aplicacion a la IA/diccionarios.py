# Ejemplo: Información de una persona
persona = {
    "nombre": "Ana García",
    "edad": 26,
    "profesion": "Ingeniera de Sistemas",
    "ciudad": "Bogotá",
    "activo": True
}

print(persona)

# Usando el diccionario persona definido anteriormente
print(persona["nombre"]) # Ana García
print(persona["edad"]) # 26
print(persona["profesion"]) # Ingeniera de Sistemas

print(f"Nueva edad: {persona['edad']}") # Nueva edad: 26

# Agregar nuevos elementos
persona["telefono"] = "+57 300 123 4567"
persona["email"] = "ana.garcia@email.com"
print(persona)

# Método 1: pop() - elimina y retorna el valor
telefono_eliminado = persona.pop("telefono")
print(f"Teléfono eliminado: {telefono_eliminado}")

# Método 1: Iteración directa (por defecto itera sobre claves)
print("Claves del diccionario:")
for clave in persona:
    print(f" - {clave}")
    
# Método 2: Usando keys() explícitamente
print("\nUsando keys():")
for clave in persona.keys():
    print(f" - {clave}")
    
print("Valores del diccionario:")
for i in persona.values():
    print(f" - {i}")

print("Pares clave-valor:")
for clave, valor in persona.items():
    print(f" {clave}: {valor}")
