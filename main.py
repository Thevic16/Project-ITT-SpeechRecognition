import speech_recognition as sr
import serial

serialPort = serial.Serial(port="/dev/ttyACM0", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


r = sr.Recognizer()
with sr.Microphone() as source:
    while(1):
        print('Speak Anything : ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=4)
        try:
            text = r.recognize_google(audio, language='es-DO')
            text_str = format(text)
            print('You said: '+text_str)


            if "Sofía" in text_str and "adelante" in text_str:
                serialPort.write(b"w \r\n")
            elif "Sofía" in text_str and "derecha" in text_str:
                serialPort.write(b"d \r\n")
            elif "Sofía" in text_str and "atrás" in text_str:
                serialPort.write(b"s \r\n")
            elif "Sofía" in text_str and "izquierda" in text_str:
                serialPort.write(b"a \r\n")

        except Exception as ex:
            print('Sorry could not hear \n')
            print("Error occured \n")
            print(ex)

