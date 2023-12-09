import os, webbrowser, sys, subprocess, pyttsx3, requests
from Syntes_pyttsx3 import speaker
import json
import WeatherToken

try:
	import requests
except:
	pass


def browser():
    webbrowser.open('https://www.youtube.com', new=2)


def weather():
    try:
        params = {'q': 'Saint Petersburg', 'units': 'metric', 'lang': 'ru', 'appid': f'{WeatherToken.TOKEN}'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        w = response.json()
        speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    # отключение бота
    sys.exit()


def passive():
    # функция заглушка при простом диалоге с ботом
    pass

# if __name__ == '__main__':
#     weather()
