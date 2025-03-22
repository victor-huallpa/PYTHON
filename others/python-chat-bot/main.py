import openai
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

openai.api_key = os.getenv("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")

# Inicialización de mensajes si no está definido
if "messages" not in st.session_state:
  st.session_state["messages"] = [{"role": "assistant", "content": "Hola, soy ChatGPT, ¿En qué puedo ayudarte?"}]

# Mostrar los mensajes existentes
for msg in st.session_state["messages"]:
  st.chat_message(msg["role"]).write(msg["content"])

# Entrada del usuario
if user_input := st.chat_input():
  st.session_state["messages"].append({"role": "user", "content": user_input})
  st.chat_message("user").write(user_input)
  
  # Obtener la respuesta del modelo ChatGPT
  response = client.completions.create(
   model="gpt-3.5-turbo-instruct",
   prompt="Write a tagline for an ice cream shop."
  )
  
  # Agregar la respuesta a los mensajes
  responseMessage = response['choices'][0]['text']
  st.session_state["messages"].append({"role": "assistant", "content": responseMessage})
  st.chat_message("assistant").write(responseMessage)
