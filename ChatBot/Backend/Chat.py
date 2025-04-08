def get_bot_reply(user_msg):
    user_msg = user_msg.lower()

    respuestas = {
        "saludos": ["hola", "buenos días", "buenas tardes", "qué tal"],
        "despedidas": ["adiós", "hasta luego", "nos vemos", "chao"],
        "agradecimientos": ["gracias", "muchas gracias", "te lo agradezco"],
        "ayuda": ["ayuda", "necesito ayuda", "qué puedes hacer"],
        "nombre": ["cómo te llamas", "quién eres"]
    }

    respuestas_bot = {
        "saludos": "¡Hola! ¿Cómo estás?",
        "despedidas": "¡Hasta luego! Que tengas un buen día.",
        "agradecimientos": "¡De nada! Siempre estoy aquí para ayudarte.",
        "ayuda": "Puedo responder preguntas básicas o ayudarte con información general.",
        "nombre": "Soy tu asistente virtual personalizado 😊"
    }

    for categoria, frases in respuestas.items():
        if any(frase in user_msg for frase in frases):
            return respuestas_bot[categoria]

    return "Lo siento, no entendí eso. ¿Podrías reformular tu mensaje?"
