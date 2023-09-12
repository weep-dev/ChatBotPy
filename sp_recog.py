import speech_recognition as sr

def converterVoz():
    print("Diga")
    r = sr.Recognizer(language='pt-Br')
    with sr.Microphone() as source:
        print("Pode falar")
        audio = r.listen(source)
        print("Capturou o audio")
        try:
            text = r.recognize(audio)
            print(text)
        except sr.UnknownValueError:
            print()
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    
converterVoz()