#########################################################################
# CONVERTOR DE ÁUDIO
#########################################################################
# responsável pela conversão dos áudios


#########################################################################
# O QUE ESTÁ FALTANDO?
#########################################################################
# Terminar a função de transformar texto em áudio

# Mudar a voz do áudio para MASCULINO, ou teremos que mudar o nome da marca para FEMININO

# salvar a resposta em um arquivo e salvar na pasta esp32
#########################################################################

import speech_recognition as sr 
import checkNik as checkN
import pyttsx3
# import gtts
#converter o audio do GravacaoVoz em texto, caso a palavra Pesquisar for falada

# função de audio para texto
def AudiotoText(nome_arquivo):
    r = sr.Recognizer()

    with sr.AudioFile(nome_arquivo) as source:
        audio = r.record(source)  # Lê o arquivo de áudio
    try:
        texto = r.recognize_google(audio, language='pt-BR')  # Reconhece o áudio
        print("Texto reconhecido:", texto)
        
        # Verifica se a palavra "NIK" foi mencionada
        checkN.check_Nik(texto)
        
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala: {e}")



def TexttoAudio(text):
    print(f"texto par audio: {text}")
    # time.sleep(1.0)

    # # Criação do objeto gTTS
    # tts = gtts.gTTS(text=text, lang='pt-br')  

    # # Salvando o áudio em um arquivo
    # tts.save("Esp32/command.mp3")

    # # Opcional: Reproduzir o áudio (apenas em sistemas que suportam)
    # os.system("start command.mp3")


    # ===================================================================================
    #tranformar audio em texto
    #Inicializa o mecanismo de conversão de texto em fala
    engine = pyttsx3.init()

    #Define a taxa de fala (opcional)
    engine.setProperty('rate', 150)  # Aumente ou diminua a taxa conforme necessário

    #Define o volume (opcional)
    engine.setProperty('volume', 1)  # Volume de 0.0 a 1.0

    #Define a voz (opcional)
    voices = engine.getProperty('voices')
    #Seleciona a voz masculina (geralmente a primeira voz é masculina)
    engine.setProperty('voice', voices[0].id)

    #Converte o texto em fala
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    
    # ============================================================
    # LEMBRETE
    # quando for salvar o arquivo de audio de resposta, salvar como:
    # Na pasta WEB/NIK/Esp32/
    # Nome do arquivo: response.wav
    # ============================================================
    
    
    # se não ocorreu erro, o código cria um arquivo
    # para sinalizar ao php que foi completado o código python
    create_file = open("WEB/NIK/Esp32/result.txt", "a")