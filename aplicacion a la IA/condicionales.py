def verificar_mayoria_edad():
    """
    Función que solicita la edad al usuario y determina su categoría etaria
    """
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0:
            print("Error: La edad no puede ser negativa.")
        elif edad == 0:
            print("¡Acabas de nacer! Bienvenido al mundo.")
        elif edad < 13:
            print(f"Tienes {edad} años. Eres un niño/niña.")
        elif edad < 18:
            print(f"Tienes {edad} años. Eres un adolescente.")
            años_faltantes = 18 - edad
            print(f"Te faltan {años_faltantes} años para ser mayor de edad.")
        elif edad < 65:
            print(f"Tienes {edad} años. Eres mayor de edad y estás en edad productiva.")
        else:
            print(f"Tienes {edad} años. Eres un adulto mayor.")
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")

# Ejecutar la función
verificar_mayoria_edad()
