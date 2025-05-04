# AI de coleta do CLIMA
# transformar tudo isso em uma função que possa ser chamada

# !!!
# Se a estrutura da pesquisa se mantiver a mesma, a coleta
# dos dados vei ocorrer conforme o esperado

import requests
from Commands.request_API import API_KEY_WEATHER

def Ai_weather(command):

    # OU colocar com fixo "jundiai" OU perguntar ao usuário sua cidade
    #nome da cidade
    city_name = "sao paulo"

    # OpenWeather
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY_WEATHER}"

    print(link)
    requisicao = requests.get(link)

    weather_time = requisicao.json()
    description = weather_time['weather'][0]['description']
    temp = weather_time['main']['temp'] - 273.15
    temp_max = weather_time['main']['temp_max'] - 273.15
    temp_min = weather_time['main']['temp_min'] - 273.15

    # APRESENTAÇÃO DOS DADOS DE TESTE,
    # alterar depois a partir do que tem que ser apresentado para o NIK
    # ou seja, retornar texto com as informações e passar para a 
    # função TexttoAudio(text) do audioConverter.py

    print(f"Descrição: {description}, Temperatura: {temp}ºC\n temp_max: {temp_max}\n temp_min: {temp_min}")