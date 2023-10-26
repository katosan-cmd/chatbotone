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

# Este código crea una clase ChatBot con métodos para saludar y despedirse.
# Luego crea una instancia de ChatBot llamada BotPython y utiliza sus métodos
# para saludar y despedirse.
# Por favor, ten en cuenta que este es un ejemplo muy básico. Un bot de chat real
#  requeriría mucho más código y funcionalidad, como la capacidad de procesar
#  y responder a las entradas del usuario.
