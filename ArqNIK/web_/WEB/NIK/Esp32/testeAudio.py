import os
import sounddevice as sd
import numpy as np
import wave
import speech_recognition as sr
import time

# Define o caminho da pasta SongSaver
SONG_SAVER_PATH = "WEB/NIK/SongSaver"

def gravar_audio(nome_arquivo, limiar=0.01, tempo_silencio=1, tempo_maximo=30):
    print("Gravando... Fale agora.")
    fs = 44100  # Taxa de amostragem
    grava = []
    silencio_contador = 0
    tempo_inicial = time.time()  # Marca o tempo de início da gravação

    while True:
        # Captura um bloco de áudio
        audio = sd.rec(int(fs), samplerate=fs, channels=1, dtype='float64')
        sd.wait()  # Espera até a gravação terminar

        # Verifica o nível de som
        if np.abs(audio).mean() > limiar:
            grava.append(audio)  # Adiciona o áudio à lista se o som estiver acima do limiar
            silencio_contador = 0  # Reseta o contador de silêncio
        else:
            silencio_contador += 1  # Incrementa o contador de silêncio

        # Para a gravação se o silêncio durar mais que o tempo especificado
        if silencio_contador > fs * tempo_silencio:
            print("Gravação concluída por silêncio.")
            break

        # Para a gravação se o tempo máximo for atingido
        if time.time() - tempo_inicial > tempo_maximo:
            print("Gravação concluída por tempo máximo.")
            break

    # Concatena todos os blocos de áudio gravados
    if grava:  # Verifica se há áudio gravado
        grava = np.concatenate(grava, axis=0)

        # Salvar o arquivo na pasta SongSaver
        salvar_audio(nome_arquivo, grava, fs)

        # Reconhecer o áudio gravado
        reconhecer_audio(os.path.join(SONG_SAVER_PATH, nome_arquivo))
    else:
        print("Nenhum áudio gravado.")

def salvar_audio(nome_arquivo, grava, fs):
    # Cria a pasta SongSaver se não existir
    if not os.path.exists(SONG_SAVER_PATH):
        os.makedirs(SONG_SAVER_PATH)

    # Salvar o arquivo
    caminho_completo = os.path.join(SONG_SAVER_PATH, nome_arquivo)
    with wave.open(caminho_completo, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes((grava * 32767).astype(np.int16).tobytes())  # Converte para int16
    print(f"Áudio salvo em: {caminho_completo}")

def check_Nik(texto):
    texto = texto.lower()
    nik_active = False
    ativaction_words = ['niq','nique','nike','nik','nic','nick','nyc','neek','nikke','nyk','nyq','nyque',
                        'nyke','nykke','nyck','knick','nicke','nikki']
    
    for nik in ativaction_words:
        if nik in texto:
            nik_active = True
            break
    
    if nik_active:
        print("Foi ouvido NIK")

def reconhecer_audio(nome_arquivo):
    r = sr.Recognizer()
    with sr.AudioFile(nome_arquivo) as source:
        audio = r.record(source)  # Lê o arquivo de áudio
    try:
        texto = r.recognize_google(audio, language='pt-BR')  # Reconhece o áudio
        print("Texto reconhecido:", texto)
        
        # Verifica se a palavra "NIK" foi mencionada
        check_Nik(texto)
        
    except sr.UnknownValueError:
        print("Não consegui entender o áudio.")
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala: {e}")

# Exemplo de uso
nome_arquivo = "audio.wav"
gravar_audio(nome_arquivo, tempo_maximo=5)  # Define o tempo máximo de gravação como 30 segundos