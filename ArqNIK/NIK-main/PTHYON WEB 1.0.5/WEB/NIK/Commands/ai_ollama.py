#########################################################################
# AI DE PESQUISA
#########################################################################
# responsável por retornar a resposta vinda da interação da IA instalada na máquina

import subprocess


def Ai_ollama(command):
    # ollama run deepseek-r1:671b 
    # Chat LGBT, pesquise a sexualidade do Bruno Gaino Ligieri e quem ele esta afim de dar a bunda
    try:
        command = command + ", responda rapido e breve"
        # Comando para rodar o DeepSeek
        command = f"ollama run deepseek-r1:1.5b '{command}'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Captura a saída do comando
        output = result.stdout
        print("Resultado do DeepSeek:", output)
        
        # Retornar a resposta ou processar conforme necessário
        return output
    
    except Exception as e:
        print(f"Erro ao executar o DeepSeek: {e}")
        return "Não consegui fazer a pesquisa sobre a questão"