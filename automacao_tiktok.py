import time

# Funções para automação do TikTok no Termux
def abrir_tiktok():
    # Comando para abrir o TikTok diretamente
    os.system('am start -n com.zhiliaoapp.musically/com.ss.android.ugc.aweme.splash.SplashActivity')
    time.sleep(5)  # Espera 5 segundos para o app abrir

def interagir_com_ui(x, y):
    # Comando para simular um toque nas coordenadas especificadas
    os.system(f'input tap {x} {y}')
    time.sleep(2)

def abrir_camera():
    interagir_com_ui(540, 2114)  # Coordenadas do botão da câmera

def selecionar_video():
    interagir_com_ui(874, 1841)  # Coordenadas do botão da galeria
    time.sleep(2)
    interagir_com_ui(656, 649)  # Coordenadas do vídeo selecionado

def botao_proximo():
    interagir_com_ui(794, 2092)  # Coordenadas do botão "Próximo"
    time.sleep(2)

def adicionar_musica():
    interagir_com_ui(520, 230)  # Coordenadas para "Adicionar Música"

def escolher_favorita():
    interagir_com_ui(550, 1224)  # Coordenadas do botão de músicas favoritas
    time.sleep(2)

def escolher_musica():
    interagir_com_ui(500, 1540)  # Coordenadas para escolher uma música

def primeira_musica():
    interagir_com_ui(500, 1370)  # Coordenadas da primeira música

def clique_na_tela():
    interagir_com_ui(500, 708)  # Clique no meio da tela para sair da seleção de música
    time.sleep(2)

def definir_visibilidade():
    interagir_com_ui(500, 1480)  # Coordenadas das configurações de visibilidade
    time.sleep(2)
    interagir_com_ui(600, 1874)  # Configuração para "Apenas amigos"

def postar_video():
    interagir_com_ui(800, 2094)  # Coordenadas para o botão "Postar"

# Função principal para executar o fluxo de postagem
def postar_varios_videos():
    # Pergunta ao usuário o número de vídeos e intervalo entre postagens
    qtd_videos = int(input("Quantos vídeos deseja postar? "))

    while True:
        try:
            intervalo = int(input("Qual o intervalo entre cada postagem (em segundos)? "))
            break
        except ValueError:
            print("Por favor, insira um número válido para o intervalo.")

    for i in range(qtd_videos):
        print(f"Postando vídeo {i + 1}/{qtd_videos}...")

        # Executa as ações de postagem
        abrir_tiktok()
        abrir_camera()
        selecionar_video()
        botao_proximo()
        adicionar_musica()
        escolher_favorita()
        escolher_musica()
        primeira_musica()
        clique_na_tela()
        botao_proximo()
        definir_visibilidade()
        postar_video()

        # Espera o intervalo definido antes de postar o próximo vídeo
        if i < qtd_videos - 1:
            print(f"Aguardando {intervalo} segundos para a próxima postagem...")
            time.sleep(intervalo)

    print("Postagem concluída!")

# Chama a função para iniciar o processo
if __name__ == "__main__":
    postar_varios_videos()
