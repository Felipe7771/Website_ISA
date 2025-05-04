import subprocess
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
    
    nik_active = check_name(texto, ativaction_words)
    if nik_active:
        print("Foi ouvido NIK")
        response = "Desculpe, não compreendi a requisição"
        
        # Verificar se "Pesquisa" foi dito:
        if check_name(texto, ["pesquise", "pesquisar"]):
            # Executar o DeepSeek com a frase inteira
            try:
                texto = texto + ", diga a resposta rapida"
                # Comando para rodar o DeepSeek
                command = f"ollama run deepseek-r1:1.5b '{texto}'"
                print(command)
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                
                # Captura a saída do comando
                output = result.stdout
                print("Resultado do DeepSeek:", output)
                
                # Retornar a resposta ou processar conforme necessário
                response = output
            
            except Exception as e:
                print(f"Erro ao executar o DeepSeek: {e}")
        
        # Outras verificações...
        
        audioC.TexttoAudio(response)
        

# check_Nik("NIK, pesquisar calculate what is one plus one")