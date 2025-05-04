#########################################################################
# COPIADOR DE ÁUDIO - ajuda de Desenvolvimento
#########################################################################
# responsável por facilitar a tranferência de arquivos áudios pré salvos
# para o SongSaver

import os, shutil
import pasteLocal as pasteL

path = pasteL.paste()
arquivo = 'audio.wav'

try:
    shutil.copy(f'{path}/{arquivo}', f'{path}/SongSaver/')
    print("arquivo foi copiado com sucesso")
except OSError:
    print("verifique se o nome do arquivo existe no diretório")
