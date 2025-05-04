#########################################################################
# CONTROLADOR
#########################################################################
# responsável pelo controle do tráfico de arquivos

import os
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
        
        
def checkInUseAudio():
    #chegagem da chegada de arquivos vindo do SongSaver
    caminho_atual = pastl.paste()
    
    #Evitando que ocorra problemas, todos os arquivos pré-salvos no InUse são deletados
    in_use = caminho_atual+"/InUse"
    deleteFile(in_use)
    
    caminho_atual = caminho_atual+"/SongSaver"
    
    #listagem dos arquivos do SongSaver
    arquvios = os.listdir(caminho_atual)

    for arq in arquvios:
        nome, estensao = os.path.splitext(arq)

        # Se o arquivo for um áudio, retorna o nome do arquivo
        if estensao == ".mp3" or estensao == ".wav":
            return arq, True
        
    return arq, False


def checkFileAudio():
    #chegagem da chegada de arquivos vindo do SongSaver
    arquivo, result = checkInUseAudio()
    
    #se result == True, temos um arquivo de áudio para analisar
    if result:
          path = pastl.paste()
          #pegar esse arquivo e mover para a pasta InUse
          shutil.move(f'{path}/SongSaver/{arquivo}', f'{path}/InUse/') 

          os.rename(f'{path}/InUse/{arquivo}',f'{path}/InUse/audio.wav')
          #chame a função de áudio para texto
          
          IN_USE_PATH = "InUse/"
          nome_arquivo = "audio.wav"
          audioC.AudiotoText(os.path.join(IN_USE_PATH,nome_arquivo))