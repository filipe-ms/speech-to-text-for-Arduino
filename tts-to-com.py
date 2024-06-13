import serial # PIP install pyserial...
import speech_recognition # PIP install speechrecognition...

arduino = serial.Serial('COM5', 9600) # Defina corretamente a porta COM do arduino!!
voice = speech_recognition.Recognizer()

def text_to_speech():
    try:
        with speech_recognition.Microphone() as audio_source: # Utilizando o microfone como fonte de audio.
            voice.adjust_for_ambient_noise(audio_source, duration = 0.2) # Por quanto tempo o programa ajusta a escuta para o barulho do ambiente.
            speech = voice.listen(audio_source, None, 2) # Timeout = None e tempo limite de frase = 2 segundos. Pare o mouse em cima de Listen para mais informações.
            speech_to_text = voice.recognize_google(speech, language="pt-BR") # Use o Google para fazer a tradução.

            return speech_to_text

    except speech_recognition.RequestError as e:
        print("Could not request results; {0}".format(e))

    except speech_recognition.UnknownValueError:
        print("unknown error occurred")


def parse_tts(mensagem_transcrita): # Não esqueça de adequar essa função às suas necessidades!!
    return mensagem_transcrita

while True:
    arduino.write(f'{parse_tts(text_to_speech())}\r'.encode()) # Envia a mensagem para o arduino.
