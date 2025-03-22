import random
import pyttsx3

# Diccionario de respuestas
respuestas_saludos = [
    "Hola, soy EcoTe, asistente de ventas de EcotTec, empresa encargada en venta de laptops en diferentes marcas y modelos. ¿En qué puedo ayudarte hoy?",
    "¡Hola! Soy EcoTe, asistente de ventas de EcotTec. ¿En qué puedo asistirte?",
    "Hola, bienvenido. Soy EcoTe, asistente de ventas de EcotTec. ¿Cómo puedo ayudarte?",
    "Hola, soy EcoTe, asistente de ventas de EcotTec. ¿En qué puedo asistirte hoy?",
    "¡Buenos días! Soy EcoTe, asistente de ventas de EcotTec. ¿Cómo puedo ayudarte?",
    "¡Hola! Soy EcoTe, asistente de ventas de EcotTec. ¿En qué puedo ayudarte hoy?",
    "Hola, soy EcoTe, asistente de ventas de EcotTec. ¿Cómo puedo asistirte?",
    "Hola, bienvenido. Soy EcoTe, asistente de ventas de EcotTec. ¿En qué puedo ayudarte?",
    "¡Hola! Soy EcoTe, asistente de ventas de EcotTec. ¿En qué puedo asistirte hoy?",
    "Hola, soy EcoTe, asistente de ventas de EcotTec. ¿En qué puedo ayudarte?",
]
respuestas_despedida = [
    "¡Adiós! Si necesitas algo más, no dudes en volver. Estoy aquí para ayudarte.",
    "Hasta luego. Si tienes más consultas, no dudes en regresar.",
    "Nos vemos. Recuerda que siempre puedes contar conmigo para cualquier ayuda que necesites.",
    "¡Hasta luego! Que tengas un buen día.",
    "Adiós, que tengas un día maravilloso.",
    "Hasta pronto. Siempre estaré aquí para ayudarte.",
    "Nos vemos luego. Siempre estoy disponible si necesitas ayuda adicional.",
    "Que tengas un buen día. Hasta la próxima.",
    "¡Adiós! Siempre es un placer ayudarte.",
    "Hasta pronto. No dudes en volver si tienes más preguntas.",
]
modelos_por_marca = {
    "hp": {
        "pavilion",
        "omen",
        "spectre",
    },
    "dell": {
        "inspiron",
        "alienware",
        "latitude",
        "xps",
    },
    "lenovo": {
        "thinkpad",
        "ideapad",
        "legion",
        "yoga",
    }
}
hp = {
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
}
dell = {
    "inspiron": {
        "precio": "$700 - $1500",
        "ram": "8 GB - 16 GB",
        "procesador": "Intel Core i3 - i7",
        "tarjeta_grafica": "Intel UHD Graphics o Nvidia GeForce MX130",
        "pantalla": "13.3 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Ideal para tareas diarias y multitarea."
    },
    "alienware": {
        "precio": "$1500 - $4000",
        "ram": "16 GB - 64 GB",
        "procesador": "Intel Core i7 - i9",
        "tarjeta_grafica": "Nvidia GeForce RTX o AMD Radeon RX",
        "pantalla": "15.6 pulgadas - 17.3 pulgadas",
        "caracteristicas": "La mejor opción para jugadores entusiastas y profesionales creativos."
    },
    "latitude": {
        "precio": "$800 - $2000",
        "ram": "8 GB - 32 GB",
        "procesador": "Intel Core i5 - i7",
        "tarjeta_grafica": "Intel UHD Graphics o AMD Radeon",
        "pantalla": "14 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Ideal para profesionales en movimiento y negocios."
    },
    "xps": {
        "precio": "$1000 - $3000",
        "ram": "16 GB - 64 GB",
        "procesador": "Intel Core i7 - i9",
        "tarjeta_grafica": "Nvidia GeForce GTX o RTX",
        "pantalla": "13.3 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Diseñada para usuarios exigentes y creativos."
    },
}
lenovo = {
    "thinkpad": {
        "precio": "$900 - $2000",
        "ram": "8 GB - 32 GB",
        "procesador": "Intel Core i5 - i7",
        "tarjeta_grafica": "Intel UHD Graphics o Nvidia GeForce MX",
        "pantalla": "14 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Diseñada para uso empresarial y productividad."
    },
    "ideapad": {
        "precio": "$500 - $1200",
        "ram": "4 GB - 16 GB",
        "procesador": "Intel Core i3 - i5",
        "tarjeta_grafica": "Intel UHD Graphics o AMD Radeon",
        "pantalla": "13.3 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Ideal para uso doméstico y estudiantil."
    },
    "legion": {
        "precio": "$1000 - $2500",
        "ram": "8 GB - 32 GB",
        "procesador": "Intel Core i5 - i7",
        "tarjeta_grafica": "Nvidia GeForce GTX o RTX",
        "pantalla": "15.6 pulgadas - 17.3 pulgadas",
        "caracteristicas": "Diseñada para juegos y rendimiento de alta gama."
    },
    "yoga": {
        "precio": "$800 - $1500",
        "ram": "8 GB - 16 GB",
        "procesador": "Intel Core i5 - i7",
        "tarjeta_grafica": "Intel UHD Graphics o Nvidia GeForce MX",
        "pantalla": "13.3 pulgadas - 15.6 pulgadas",
        "caracteristicas": "Convertible y versátil, perfecta para usuarios móviles y creativos."
    },
}


# Función para obtener información de la laptop
def obtener_info_laptop(marca, modelo):
    if marca.lower() == "hp" and modelo.lower() in hp:
        info = hp[modelo.lower()]
        return f"Modelo: {modelo.capitalize()}\nPrecio: {info['precio']}\nRAM: {info['ram']}\nProcesador: {info['procesador']}\nTarjeta Gráfica: {info['tarjeta_grafica']}\nPantalla: {info['pantalla']}\nCaracterísticas: {info['caracteristicas']}"
    elif marca.lower() == "dell" and modelo.lower() in dell:
        info = dell[modelo.lower()]
        return f"Modelo: {modelo.capitalize()}\nPrecio: {info['precio']}\nRAM: {info['ram']}\nProcesador: {info['procesador']}\nTarjeta Gráfica: {info['tarjeta_grafica']}\nPantalla: {info['pantalla']}\nCaracterísticas: {info['caracteristicas']}"
    elif marca.lower() == "lenovo" and modelo.lower() in lenovo:
        info = lenovo[modelo.lower()]
        return f"Modelo: {modelo.capitalize()}\nPrecio: {info['precio']}\nRAM: {info['ram']}\nProcesador: {info['procesador']}\nTarjeta Gráfica: {info['tarjeta_grafica']}\nPantalla: {info['pantalla']}\nCaracterísticas: {info['caracteristicas']}"
    else:
        return f"Lo siento, no tenemos información sobre el modelo {modelo} de laptop."

def sonido_print(imprimir):
    engine = pyttsx3.init()
    print(imprimir)
    engine.say(imprimir)
    engine.runAndWait()
    engine.stop()


while True:
    saludo_elegido = random.choice(respuestas_saludos)
    sonido_print(saludo_elegido)
    # Solicitar al usuario ingresar la marca y el modelo de la laptop
    marca_laptop = input("Ingrese la marca de la laptop que desea consultar (HP/Dell/lenovo): ")

    if marca_laptop in modelos_por_marca:
        modelos = modelos_por_marca[marca_laptop]
        respuesta = f"Modelos de {marca_laptop.capitalize()}:"
        sonido_print(respuesta)
        for i, modelo in enumerate(modelos, start=1):
            respuesta1 = f"{i}. {modelo.capitalize()}"
            sonido_print(respuesta1)
        modelo_laptop = input("Ingrese el modelo de la laptop que desea consultar: ")
            # Obtener y mostrar la información de la laptop
        info_laptop = obtener_info_laptop(marca_laptop, modelo_laptop)
        sonido_print(info_laptop)

        despedida_elegida = random.choice(respuestas_despedida)
        sonido_print(despedida_elegida)
    else:
        respuesta2 = f"Lo siento, no tenemos información sobre la marca {marca_laptop} de laptop."
        sonido_print(respuesta2)