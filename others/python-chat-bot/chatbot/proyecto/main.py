import openai
import pyttsx3
import os
# Configuración de la clave de la API de ChatGPT
API_KEY = os.getenv("OPENAI_API_KEY")


# Función para enviar la solicitud a la API de ChatGPT
def enviar_solicitud(texto):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=texto,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Función para convertir texto a voz
def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

# Saludo inicial del chatbot
texto_a_voz("¡Hola! Soy un chatbot de EcoTec. ¿En qué puedo ayudarte?")

# Loop principal del chatbot
while True:
    entrada_usuario = input('Tú: ')
    
    # Envía la solicitud al modelo de ChatGPT y obtiene la respuesta
    respuesta_chatbot = enviar_solicitud(entrada_usuario)
    
    # Muestra la respuesta del chatbot y conviértela a voz
    print('Chatbot:', respuesta_chatbot)
    texto_a_voz(respuesta_chatbot)
