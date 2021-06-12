import speech_recognition as sr
import serial
import time

r = sr.Recognizer()
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#ser.flush()

with sr.Microphone() as source:
    while (1):
        print('Speak Anything : ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        '''
        with open('speech.wav','wb') as f:
            f.write(audio.get_wav_data())
        '''

        try:
            text = r.recognize_google(audio, language='es-MX')
            print('You said: {}'.format(text))
        except:
            print('Sorry could not hear')
