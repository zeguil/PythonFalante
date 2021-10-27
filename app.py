import gtts # pip install gTTS
from playsound import playsound # pip install playsound

with open("frase.txt", 'r') as arquivo: # Abre o arquivo frase.txt no modo leitura
    for linha in arquivo: # Percorre o arquivo linha por linha
        frase = gtts.gTTS(linha, lang='pt-br') # Converte a frase para voz
        frase.save("frase.mp3") # Salva o arquivo em .mp3
        playsound("frase.mp3") # Reproduz o arquivo .mp3