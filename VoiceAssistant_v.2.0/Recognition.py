import os
import speech_recognition as sr

#import GPT, Syntes
from GPT import ask_gpt
from Syntes import speaker

r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

def record():
    while True and int(os.getenv('MIC')):
        print('Rec:')
        with mic as sourse:
            r.adjust_for_ambient_noise(sourse)
            audio = r.listen(sourse)
            try:
                data: str = r.recognize_google(audio, language='ru-RU').lower()

            except sr.UnknownValueError:
                data = ''
                pass
        #print(data)
        if data != '':
            print(f'You said - {data}')
            answer = ask_gpt(data)
            print(f'Answer - {answer}')
            speaker(answer)
    print('Stop Rec')
