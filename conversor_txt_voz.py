import pyttsx3
import fitz  # PyMuPDF

# inicializa o motor de voz
motor_voz = pyttsx3.init()

motor_voz.setProperty('rate', 150) # velocidade da fala

voz = motor_voz.getProperty('voices')
motor_voz.setProperty('voice', voz[0].id) # voz feminino

arquivo = 'livro1.pdf'
documento = fitz.open(arquivo)
texto = ""

for pagina in documento:
    texto += pagina.get_text("text") + "\n" # Extrai o texto de cada página

if not texto:
    print("Não foi possível extrair o texto do arquivo")
else:
    numero1 = int(input("Digite 1 se deseja ouvir o texto\nDigite 2 para salvar o aúdio(1 ou 2): \n"))
    if numero1 == 1:
        motor_voz.say(texto) # Lê o texto
        motor_voz.runAndWait() # Aguarda a conclusão
    elif numero1 == 2:
        arquivo_audio = "audio.mp3" # Nome do arquivo de saída
        motor_voz.save_to_file(texto, arquivo_audio) # Salva o áudio
        motor_voz.runAndWait() # Aguarda a conclusão
        if motor_voz:
            print("Arquivo de aúdio foi salvo com sucesso!")

# ler o conteúdo do arquivo EM TXT
# with open('livro1.txt', 'r') as arquivo:
#     texto = arquivo.read()
