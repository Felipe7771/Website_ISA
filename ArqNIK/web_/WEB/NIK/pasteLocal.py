#########################################################################
# PASTA LOCAL
#########################################################################
# responsável pelO retorno do caminho absoluto do arquivo

import os

def paste():
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    return caminho_atual


