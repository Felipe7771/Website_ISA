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

def check_name(texto,list):
    # lista: parametros de pesquisa
    # texto: valor procurado
    for nik in list:
        if nik in texto:
            return True
    
    return False

def check_Nik(texto):
    texto = texto.lower()
    path = pastl.paste()
    ativaction_words = ['niq','nique','nike','nik','nic','nick','nyc','neek','nikke','nyk','nyq','nyque',
                        'nyke','nykke','nyck','knick','nicke','nikki','fique','rick']
    
    nik_active = check_name(texto,ativaction_words)
    
    if nik_active:
            print("Foi ouvido NIK")
            #nik foi ativado
            #terminar código depois
            reponse = "Desculpe, não compreendi a requisição"
            
            #verificar se "Pesquisa" foi dito:
            if check_name(texto,["pesquise","pesquisar"]):
                response = ollama.Ai_ollama(texto)
            
            #verificar se "Horas" foi dito:
            elif check_name(texto,["horas","dia","dia da semana","mês","mes","ano","horário","horario"]):
                print("vendo horas")
                time.sleep(3.0)
                response = hour.Ai_hour(texto)
            
            #verificar se "Musica" foi dito:
            elif check_name(texto,["toque a musica"]):
                response = music.Ai_music(texto)
            
            #verificar se "noticias" foi dito:
            elif check_name(texto,["noticias","noticia"]):
                response = news.Ai_news(texto)
            
            #verificar se "Clima" foi dito:
            elif check_name(texto,["clima","previsao do tempo","previsao","previsão","previsão do tempo","tempo"]):
                response = weather.Ai_weather(texto)
            
            else:
                response = "Não foi entendido sua questão"

            audioC.TexttoAudio(response)
    # não importa o resultado
    # sempre que a análise do áudio dentro do InUse for encerrafa, ela será excluida
    path = path + "\InUse"
    ctrl.deleteFile(path)