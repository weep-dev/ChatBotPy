import openai
import pyttsx3

openai.api_key = 'sua key aqui'

def responder_pergunta(pergunta):
    resposta = openai.Completion.create(
        engine='text-curie-001',
        prompt=pergunta,
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.7
    )
    return resposta.choices[0].text.strip()

# Função de falar
def falar_texto(texto):
    # Cria um objeto de fala
    engine = pyttsx3.init()
    
    # Define a voz a ser usada (opcional)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Altere o índice para selecionar outra voz
    
    # Fala o texto
    engine.say(texto)
    engine.runAndWait()

# Exemplo de uso
pergunta = input("Faça uma pergunta: ")
resposta = responder_pergunta(pergunta)
print(resposta)
falar_texto(resposta)
