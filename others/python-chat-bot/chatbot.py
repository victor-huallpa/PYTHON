import pyttsx3
import random

# Inicialización del motor de texto a voz
engine = pyttsx3.init()

# Configuración de la voz
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Cambia el índice según la voz que prefieras

# Respuestas del chatbot
respuestas_saludo = [
    "¡Hola! Soy EcoTe, el asistente virtual de EcoTec. ¿En qué puedo ayudarte hoy?",
    "¡Bienvenido! Soy EcoTe, el asistente virtual de EcoTec. ¿Cómo puedo ayudarte?",
    "Hola, soy EcoTe, el asistente virtual de EcoTec. ¿En qué puedo asistirte?"
]

respuestas_despedida = [
    "¡Adiós! Si necesitas algo más, no dudes en volver. Estoy aquí para ayudarte.",
    "Hasta luego. Si tienes más consultas, no dudes en regresar.",
    "Nos vemos. Recuerda que siempre puedes contar conmigo para cualquier ayuda que necesites."
]

respuestas_generales = [
    "Lo siento, no entendí. ¿Puedes repetirlo?",
    "No comprendo. ¿Puedes formular la pregunta de otra manera?",
    "Esa es una buena pregunta. Permíteme buscar la respuesta."
]

respuestas_hp = {
    "pavilion": {
        "precio": "$800 - $1200",
        "ram": "8 GB - 16 GB",
        "procesador": "Intel Core i5 - i7",
        "tarjeta_grafica": "Intel HD Graphics o Nvidia GeForce MX250",
        "pantalla": "14 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Perfecta para uso doméstico y multimedia."
    },
    "omen": {
        "precio": "$1200 - $2500",
        "ram": "16 GB - 32 GB",
        "procesador": "Intel Core i7 - i9",
        "tarjeta_grafica": "Nvidia GeForce GTX o RTX",
        "pantalla": "15.6 pulgadas - 17.3 pulgadas",
        "caracteristicas": "Diseñada para juegos de alto rendimiento y tareas exigentes."
    },
    "spectre": {
        "precio": "$1500 - $3000",
        "ram": "16 GB - 64 GB",
        "procesador": "Intel Core i7 - i9",
        "tarjeta_grafica": "Nvidia GeForce GTX o RTX",
        "pantalla": "13.3 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Elegante y potente, ideal para usuarios profesionales y creativos."
    }
    # Puedes seguir agregando más modelos aquí...
}


# Función para obtener la respuesta del chatbot y mostrarla en voz
def obtener_respuesta_y_mostrar_voz(respuesta):
    print("EcoTe:", respuesta)
    engine.say(respuesta)
    engine.runAndWait()

# Función para responder a las preguntas del usuario
def responder_pregunta(texto):
    if "hola" in texto.lower():
        respuesta = random.choice(respuestas_saludo)
    elif "adiós" in texto.lower() or "hasta luego" in texto.lower():
        respuesta = random.choice(respuestas_despedida)
    elif "hp" in texto.lower():
        respuesta = "Tenemos varios modelos de HP disponibles, incluyendo Pavilion, Omen y Spectre. ¿Sobre cuál modelo te gustaría obtener más información?"
    else:
        respuesta = random.choice(respuestas_generales)
    return respuesta

# Saludo inicial del chatbot
obtener_respuesta_y_mostrar_voz(random.choice(respuestas_saludo))

# Bucle principal del chatbot
while True:
    # Obtener la entrada del usuario
    entrada_usuario = input("Tú: ")
    
    # Obtener y mostrar la respuesta del chatbot
    respuesta = responder_pregunta(entrada_usuario)
    obtener_respuesta_y_mostrar_voz(respuesta)

    # Comprobar si el usuario desea salir del chatbot
    if "adiós" in entrada_usuario.lower() or "hasta luego" in entrada_usuario.lower():
        break
