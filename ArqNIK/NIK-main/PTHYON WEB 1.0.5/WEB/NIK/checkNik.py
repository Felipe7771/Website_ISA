#########################################################################
# CHECAGEM NIK
#########################################################################
# responsável por verificar se NIK foi chamado no áudio

import os,time
import Commands.ai_ollama as ollama
import Commands.hour as hour
import Commands.music as music
import Commands.news as news
import Commands.weather as weather
import controller as ctrl
import pasteLocal as pastl
import audioConverter as audioC

def check_name(text,list):
    # lista: parametros de pesquisa
    # texto: valor procurado
    for nik in list:
        if nik in text:
            return True
    
    return False

def check_item_name(text,list):
    # As palavras do texto seram divididas
    words_of_text = text.split()
    # A leitura será feita de trás para frente para previnir correções da fala do usuário no áudio
    words_of_text = words_of_text[::-1]

    for word in words_of_text:
        for item in list:
            if word == item:
                return True

    return False

def check_Nik(texto):
    texto = texto.lower()
    path = pastl.paste()
    ativaction_words = ['niq','nique','nike','nik','nic','nick','nyc','neek','nikke','nyk','nyq','nyque',
                        'nyke','nykke','nyck','knick','nicke','nikki','fique','rick','vick','mik']
    
    nik_active = check_name(texto,ativaction_words)
    
    if nik_active:
            print("Foi ouvido NIK")
            #nik foi ativado
            #terminar código depois
            response = "Desculpe, não compreendi a requisição"
            
            # ================================================================
            # FELIPE: não seria mais intuitivo colocar a forma de pesquisa por IA como a última condição? já que normalmente você não pergunta a uma
            # alexa pesquisar, mas já faz a pergunta sem a palavra "pesquisar"
            # ================================================================

            #verificar se "Pesquisa" foi dito:
            if check_item_name(texto,["pesquise","pesquisar"]):
                response = ollama.Ai_ollama(texto)
            
            #verificar se "Horas" foi dito:
            elif check_item_name(texto,["horas","dia","dia da semana","mês","mes","ano","horário","horario"]):
                print("vendo horas")
                time.sleep(3.0)
                response = hour.Ai_hour(texto)
            
            #verificar se "Musica" foi dito:
            elif check_item_name(texto,["toque a musica"]):
                response = music.Ai_music(texto)
            
            #verificar se "noticias" foi dito:
            elif check_item_name(texto,["noticias","noticia"]):
                response = news.Ai_news(texto)
            
            #verificar se "Clima" foi dito:
            elif check_item_name(texto,["clima","previsao do tempo","previsao","previsão","previsão do tempo","tempo","previzao"]):
                response = weather.Ai_weather(texto)
            
            else:
                response = "Não foi entendido sua questão"

            audioC.TexttoAudio(response)
    # não importa o resultado
    # sempre que a análise do áudio dentro do InUse for encerrafa, ela será excluida
    path = path + "\InUse"
    ctrl.deleteFile(path)
