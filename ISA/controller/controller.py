#########################################################################
# CONTROLADOR
# INCIO DA INICIALIZAÇÃO DO CÓDIGO
#########################################################################
# responsável pelo controle do tráfico de arquivos

import os, sys
import pasteLocal as pastl
import shutil
import audioConverter as audioC
import time
      
def deleteFile(directory_path):
  # deleta os arquivos da pasta selecionada
   try:
     files = os.listdir(directory_path)
     for file in files:
       file_path = os.path.join(directory_path, file)
       if os.path.isfile(file_path):
         os.remove(file_path)
   except OSError:
        print("Algo de errado aconteceu ao tentar eliminar os arquivos do InUse")
        
        
# def checkInUseAudio():
#     #chegagem da chegada de arquivos vindo do SongSaver
#     caminho_atual = pastl.paste()
    
#     #Evitando que ocorra problemas, todos os arquivos pré-salvos no InUse são deletados
#     in_use = caminho_atual+"/InUse"
#     deleteFile(in_use)
    
#     caminho_atual = caminho_atual+"/SongSaver"
    
#     #listagem dos arquivos do SongSaver
#     arquvios = os.listdir(caminho_atual)

#     for arq in arquvios:
#         nome, estensao = os.path.splitext(arq)

#         # Se o arquivo for um áudio, retorna o nome do arquivo
#         if estensao == ".mp3" or estensao == ".wav":
#             return arq, True
        
#     return "", False


# def checkFileAudio():
#     # #chegagem da chegada de arquivos vindo do SongSaver
#     # arquivo, result = checkInUseAudio()
    
#     #se result == True, temos um arquivo de áudio para analisar
#     if result:
#           path = pastl.paste()
#           #pegar esse arquivo e mover para a pasta InUse
#           shutil.move(f'{path}/SongSaver/{arquivo}', f'{path}/InUse/') 

#           os.rename(f'{path}/InUse/{arquivo}',f'{path}/InUse/audio.wav')
#           #chame a função de áudio para texto
          
#           IN_USE_PATH = "InUse/"
#           nome_arquivo = "audio.wav"
#           audioC.AudiotoText(os.path.join(IN_USE_PATH,nome_arquivo))


# =======================================================================================
# CHEGADA DOS DADOS VINDO DO PHP
# =======================================================================================

# busca pela pasta atual
path = pastl.paste()

#Evitando que ocorra problemas, todos os arquivos pré-salvos no InUse são deletados
in_use = path+"/InUse"
deleteFile(in_use)

# pega o caminho do arquivo de audio
caminho_audio = sys.argv[1]

# pega o nome do arquivo
nome_audio = os.path.basename(caminho_audio)

#pegar esse arquivo e mover para a pasta InUse
shutil.move(f'{path}/SongSaver/{nome_audio}', f'{path}/InUse/') 

# como esse audio está em analise em InUse, podemos agora chamá-lo com um nome comum
# em função de que só entra 1 arquivo 
os.rename(f'{path}/InUse/{nome_audio}',f'{path}/InUse/audio.wav')

#chame a função de áudio para texto
IN_USE_PATH = "InUse/"
nome_arquivo = "audio.wav"
audioC.AudiotoText(os.path.join(IN_USE_PATH,nome_arquivo))
