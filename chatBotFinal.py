import speech_recognition as sr
import openai
import pyttsx3

openai.api_key = 'sua key aqui'

def responder_pergunta(pergunta):
    resposta = openai.Completion.create(
        engine='text-curie-001',
        prompt=pergunta,
        max_tokens=300,
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
    engine.setProperty('voice', voices[0].id)  # Altere o índice para selecionar outra voz
    
    # Fala o texto
    engine.say(texto)
    engine.runAndWait()

#Converte a fala do microfone em texto
def converterVoz():
    print("Diga")
    r = sr.Recognizer(language='pt-Br')
    with sr.Microphone() as source:
        print("Pode falar")
        audio = r.listen(source)
        print("Capturou o audio")
        try:
            text = r.recognize(audio)
            return text
        except sr.UnknownValueError:
            print()
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))


print("Faça uma pergunta: ")
#Chama a função que converte a voz em texto e armazena essa mensagem
pergunta = converterVoz()
#Usa a mensagem armazenada e utiliza como pergunta passada na função
resposta = responder_pergunta(pergunta)
#Mostra a resposta da pergunta e fala ela usando a função de falar
print(resposta)
falar_texto(resposta)