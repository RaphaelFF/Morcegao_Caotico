from itertools import cycle
import random
import sys
import pygame
from pygame.locals import *

# Configurações do Jogo
FPS = 30
LARGURA_DA_TELA = 288
ALTURA_DA_TELA = 512
ESPACO_TUBO = 100 
BASE_Y = ALTURA_DA_TELA * 0.79

# Dicionários de imagens, sons e máscaras de colisão
IMAGENS, SONS, MASCARAS_COLISAO = {}, {}, {}

# Listas de Ativos
LISTA_JOGADORES = (
    ('assets/img/morcego-asa-aberta.png', 'assets/img/morcego-asa-fechada.png', 'assets/img/morcego-asa-aberta.png'),
 
)

LISTA_FUNDOS = ('assets/img/fundo1.png', 'assets/img/fundo1.png')
LISTA_CANOS = ('assets/img/pipe-green.png', 'assets/img/pipe-red.png')

def main():
    global TELA, RELOGIO_FPS
    pygame.init()
    RELOGIO_FPS = pygame.time.Clock()
    TELA = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
    pygame.display.set_caption('Morcegão Caotico')

    # Carregamento de imagens básicas
    IMAGENS['numeros'] = tuple(pygame.image.load(f'assets/img/{i}.png').convert_alpha() for i in range(10))
    IMAGENS['gameover'] = pygame.image.load('assets/img/gameover.png').convert_alpha()
    IMAGENS['mensagem'] = pygame.image.load('assets/img/message.png').convert_alpha()
    IMAGENS['base'] = pygame.image.load('assets/img/base.png').convert_alpha()

    # Configuração de sons conforme a plataforma
    ext = '.wav' if 'win' in sys.platform else '.ogg'
    for som in ['morrer', 'bater', 'ponto', 'swoosh', 'asa']:
        # Mapeia os nomes internos para os nomes dos arquivos
        nome_arquivo = 'die' if som == 'morrer' else 'hit' if som == 'bater' else 'point' if som == 'ponto' else som
        SONS[som] = pygame.mixer.Sound(f'assets/audio/{nome_arquivo}{ext}')

    while True:
        # Seleciona imagens aleatórias para começar cada ciclo
        indice_fundo = random.randint(0, len(LISTA_FUNDOS) - 1)
        IMAGENS['fundo'] = pygame.image.load(LISTA_FUNDOS[indice_fundo]).convert()

        indice_jogador = random.randint(0, len(LISTA_JOGADORES) - 1)
        IMAGENS['jogador'] = (
            pygame.image.load(LISTA_JOGADORES[indice_jogador][0]).convert_alpha(),
            pygame.image.load(LISTA_JOGADORES[indice_jogador][1]).convert_alpha(),
            pygame.image.load(LISTA_JOGADORES[indice_jogador][2]).convert_alpha(),
        )

        # Chama a tela de boas-vindas
        info_movimento = mostrar_animacao_bem_vindo()
        
        
        print("Iniciando partida...") 

def mostrar_animacao_bem_vindo():
    gerador_indice_jogador = cycle([0, 1, 2, 1])
    indice_jogador = 0
    iteracao_loop = 0

    posicao_passaro_x = int(LARGURA_DA_TELA * 0.2)
    posicao_passaro_y = int((ALTURA_DA_TELA - IMAGENS['jogador'][0].get_height()) / 2)

    mensagem_x = int((LARGURA_DA_TELA - IMAGENS['mensagem'].get_width()) / 2)
    mensagem_y = int(ALTURA_DA_TELA * 0.12)

    base_x = 0
    deslocamento_base = IMAGENS['base'].get_width() - IMAGENS['fundo'].get_width()

    # Tremulação do pássaro (sobe e desce suavemente)
    valores_tremulacao = {'val': 0, 'dir': 1}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                SONS['asa'].play()
                return {
                    'y_jogador': posicao_passaro_y + valores_tremulacao['val'],
                    'x_base': base_x,
                    'gerador_indice_jogador': gerador_indice_jogador,
                }

        # Atualiza índice da asa e posição da base para dar efeito de movimento
        if (iteracao_loop + 1) % 5 == 0:
            indice_jogador = next(gerador_indice_jogador)
        iteracao_loop = (iteracao_loop + 1) % 30
        base_x = -((-base_x + 4) % deslocamento_base)
        tremulacao_jogador(valores_tremulacao)

        # Desenha tudo na tela
        TELA.blit(IMAGENS['fundo'], (0,0))
        TELA.blit(IMAGENS['jogador'][indice_jogador],
                    (posicao_passaro_x, posicao_passaro_y + valores_tremulacao['val']))
        TELA.blit(IMAGENS['mensagem'], (mensagem_x, mensagem_y))
        TELA.blit(IMAGENS['base'], (base_x, BASE_Y))

        pygame.display.update()
        RELOGIO_FPS.tick(FPS)

def tremulacao_jogador(tremulacao):
    """Oscila o valor de tremulacao['val'] entre 8 e -8"""
    if abs(tremulacao['val']) == 8:
        tremulacao['dir'] *= -1

    if tremulacao['dir'] == 1:
         tremulacao['val'] += 1
    else:
        tremulacao['val'] -= 1

if __name__ == '__main__':
    main()