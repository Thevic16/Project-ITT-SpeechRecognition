import speech_recognition as sr

import serial


serialPort = serial.Serial(port="/dev/ttyACM0", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

r = sr.Recognizer()

with sr.Microphone() as source:
    while(1):
        print('Speak Anything : ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es-MX')
            print('You said: {}'.format(text))

            if text == "Sofía hacia adelante":
                serialPort.write(b"w \r\n")
            if text == "Sofía hacia la derecha":
                serialPort.write(b"d \r\n")
            if text == "Sofía hacia atrás":
                serialPort.write(b"s \r\n")
            if text == "Sofía hacia la izquierda":
                serialPort.write(b"a \r\n")

        except:
            print('Sorry could not hear')
