#########################################################################
# AI DE CLIMA
#########################################################################
# responsável por retornar o clima e temperatura do ambiente determinado

# !!!
# Se a estrutura da pesquisa se mantiver a mesma, a coleta
# dos dados vei ocorrer conforme o esperado

import requests
from request_API import API_KEY_WEATHER

def Ai_weather(command):

    # OU colocar com fixo "jundiai" OU perguntar ao usuário sua cidade
    #nome da cidade

    # =======================
    # TESTE DEFINIDO COMO
    city_name = "sao paulo"

    # OpenWeather
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY_WEATHER}&lang=pt_br"

    print(link)
    requisicao = requests.get(link)

    if requisicao.status_code == 200:
        weather_time = requisicao.json()
        description = weather_time['weather'][0]['description']
        temp = weather_time['main']['temp'] - 273.15
        temp_max = weather_time['main']['temp_max'] - 273.15
        temp_min = weather_time['main']['temp_min'] - 273.15

        #arredondamento dos valores de temperatura
        temp = round(temp,2)
        temp_max = round(temp_max,2)
        temp_min = round(temp_min,2)

        # APRESENTAÇÃO DOS DADOS DE TESTE,
        # alterar depois a partir do que tem que ser apresentado para o NIK
        # ou seja, retornar texto com as informações e passar para a 
        # função TexttoAudio(text) do audioConverter.py

        return f"Na região de {city_name} em Brasil, o tempo está {description} com temperatura de {temp} graus celcius, com máxima de {temp_max} e mínima de {temp_min}"
    
    else:
        print(f"Erro na requisição: {requisicao.status_code}")
        return 'Não consegui acessar o clima, por favor, pergunte mais tarde'
    
print(Ai_weather("qual o clima de hoje?"))

