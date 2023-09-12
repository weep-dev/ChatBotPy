import speech_recognition as sr

# Função para reconhecimento de voz
def ouvir_microfone():
    # Cria um objeto de reconhecimento de voz
    r = sr.Recognizer()
    
    # Usa o microfone como fonte de áudio
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = r.listen(source)
    
    try:
        # Reconhece o discurso usando o Google Speech Recognition
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
        return texto
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio")
    except sr.RequestError as e:
        print("Erro ao solicitar resultados do serviço de reconhecimento de fala; {0}".format(e))

fala = ouvir_microfone()

print(fala)
