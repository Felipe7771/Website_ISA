# AI de coleta de NOTÍCIAS
# transformar tudo isso em uma função que possa ser chamada

# !!!
# Se a estrutura da pesquisa se mantiver a mesma, a coleta
# dos dados vei ocorrer conforme o esperado

import requests
from Commands.request_API import API_KEY_NEWS

def Ai_news(command):
    

    #Palavra-chave que você deseja pesquisar (pode ser qualquer coisa)
    keyword = 'brasil'

    #Definir o URL com a pesquisa personalizada
    url = f'https://newsapi.org/v2/everything?q={keyword}&language=pt&pageSize=3&apiKey={API_KEY_NEWS}'

    #Fazer a requisição GET para a NewsAPI
    response = requests.get(url)


    # APRESENTAÇÃO DOS DADOS DE TESTE,
    # alterar depois a partir do que tem que ser apresentado para o NIK
    # ou seja, retornar texto com as informações e passar para a 
    # função TexttoAudio(text) do audioConverter.py

    #Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()

        # Exibir as notícias encontradas
        for article in data['articles']:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("-" * 50)
    else:
        print(f"Erro na requisição: {response.status_code}")