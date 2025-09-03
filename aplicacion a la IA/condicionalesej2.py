def evaluar_calificacion():
    """
    Función que evalúa una nota numérica y proporciona la calificación
    correspondiente
    """
    try:
        nota = float(input("Introduce tu nota (0-5): "))
        if nota < 0 or nota > 5:
            print("Error: La nota debe estar entre 0 y 5.")
            return
        if nota >= 4.5:
            calificacion = "SOBRESALIENTE"
            descripcion = "Excelente desempeño académico"
            color_emoji = "🟢"
        elif nota >= 4.0:
            calificacion = "NOTABLE"
            descripcion = "Muy buen desempeño académico"
            color_emoji = "🔵"
        elif nota >= 3.5:
            calificacion = "BUENO"
            descripcion = "Buen desempeño académico"
            color_emoji = "🟡"
        elif nota >= 3.0:
            calificacion = "APROBADO"
            descripcion = "Desempeño académico satisfactorio"
            color_emoji = "🟠"
        else:
            calificacion = "REPROBADO"
            descripcion = "Desempeño académico insuficiente"
            color_emoji = "🔴"

        print(f"\n{color_emoji} RESULTADO DE LA EVALUACIÓN {color_emoji}")
        print(f"Nota numérica: {nota:.2f}")
        print(f"Calificación: {calificacion}")
        print(f"Descripción: {descripcion}")

        # Recomendaciones adicionales
        if nota >= 4.0:
            print("¡Felicitaciones! Mantén este excelente nivel.")
        elif nota >= 3.0:
            print("Buen trabajo. Puedes mejorar con un poco más de esfuerzo.")
        else:
            print("Es necesario reforzar los conocimientos. ¡No te desanimes!")

    except ValueError:
        print("Error: Por favor, introduce un número válido.")

# Ejecutar la función
evaluar_calificacion()
