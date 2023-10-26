class ChatBot:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludo(self):
        return f"Hola, soy {self.nombre}. ¿Cómo puedo ayudarte hoy?"

    def despedida(self):
        return f"Fue un placer ayudarte. ¡Hasta la próxima!"


# Crear una instancia del ChatBot
bot = ChatBot("BotPython")

# El bot saluda
print(bot.saludo())

# El bot se despide
print(bot.despedida())
