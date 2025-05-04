#########################################################################
# AI DE NOTÍCIAS
#########################################################################
# responsável por trazer as notícias mais recentes ao usuário

# !!!
# Se a estrutura da pesquisa se mantiver a mesma, a coleta
# dos dados vei ocorrer conforme o esperado

import requests
from request_API import API_KEY_NEWS

def Ai_news(command):
    

    #Palavra-chave que você deseja pesquisar (pode ser qualquer coisa)

    # ==================
    # TESTE DEFINIDO COMO
    keyword = 'politica'

    #Definir o URL com a pesquisa personalizada
    url = f'https://newsapi.org/v2/everything?q={keyword}&language=pt&pageSize=3&apiKey={API_KEY_NEWS}'

    #Fazer a requisição GET para a NewsAPI
    response = requests.get(url)


    # APRESENTAÇÃO DOS DADOS DE TESTE,
    # alterar depois a partir do que tem que ser apresentado para o NIK
    # ou seja, retornar texto com as informações e passar para a 
    # função TexttoAudio(text) do audioConverter.py

    #Verificar se a requisição foi bem-sucedida
    return_response = ""

    if response.status_code == 200:
        data = response.json()
        return_response = f'Consegui encontrar algumas notícias sobre {keyword}.'

        # Exibir as notícias encontradas
        for article in data['articles']:

            return_response = return_response + str(article['title']) + ',' + str(article['description']) + '. '

        return return_response
    else:
        print(f"Erro na requisição: {response.status_code}")
        return 'Não consegui acessar as notícias, por favor, pergunte mais tarde'
    

print(Ai_news("Quais são as notícias"))