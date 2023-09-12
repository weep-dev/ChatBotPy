import pyttsx3

# Função para falar o texto
def falar_texto(texto):
    # Cria um objeto de fala
    engine = pyttsx3.init()
    
    # Define a voz a ser usada (opcional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # Altere o índice para selecionar outra voz
    
    # Fala o texto
    engine.say(texto)
    engine.runAndWait()

# Solicita o input do usuário
entrada = input("Digite algo: ")

# Reproduz o texto digitado
falar_texto(entrada)
