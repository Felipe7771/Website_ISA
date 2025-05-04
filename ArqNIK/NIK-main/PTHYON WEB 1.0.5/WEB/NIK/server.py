#########################################################################
# SERVIDOR
#########################################################################
# responsável pela inicialização do servidor para o gerenciamento dos dados
# é o primeiro a ser ligado

import http.server
import socketserver
import webbrowser
import os, time
import sys
import pasteLocal as pastl
import controller as contrl


# Define a porta que o servidor vai usar
PORT = 8000

# Define o diretório que será servido

# Obtém o caminho completo do diretório atual
caminho_atual = pastl.paste()

DIRECTORY = caminho_atual

# Muda para o diretório especificado
os.chdir(DIRECTORY)

# Cria o handler para servir os arquivos
Handler = http.server.SimpleHTTPRequestHandler

# Inicia o servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor iniciado na porta {PORT}")
    print(f"Acesse em: http://localhost:{PORT}")
    
    # Abre o navegador automaticamente
    #webbrowser.open_new_tab(f"http://localhost:{PORT}")
    
    # Mantém o servidor rodando
    print("Seridor Rodadndo!")
    
    
    while True: 
        #chegagem eterna de arquivos de áudio chegos do esp 32
        contrl.checkFileAudio()
        # time.sleep(10000.0) #linha de teste
        os.system('cls')
    httpd.serve_forever()


