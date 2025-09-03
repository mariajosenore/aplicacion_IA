def chatbot():
    print("¡Hola! Soy tu chatbot. Escribe 'salir' para terminar.")
    while True:
        user_input = input("Tú: ").lower()

        if user_input == "salir":
            print("Chatbot: ¡Hasta luego!")
            break
        elif "hola" in user_input:
            print("Chatbot: ¡Hola! ¿Cómo estás?")
        elif "cómo estás" in user_input or "como estas" in user_input:
            print("Chatbot: Estoy bien, gracias por preguntar.")
        elif "qué haces" in user_input or "que haces" in user_input:
            print("Chatbot: Estoy aquí para ayudarte.")
        else:
            print("Chatbot: Lo siento, no entiendo eso.")

if __name__ == "__main__":
    chatbot()
