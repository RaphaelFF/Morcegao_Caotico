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
    ('assets/img/redbird-upflap.png', 'assets/img/redbird-midflap.png', 'assets/img/redbird-downflap.png'),
    ('assets/img/bluebird-upflap.png', 'assets/img/bluebird-midflap.png', 'assets/img/bluebird-downflap.png'),
    ('assets/img/yellowbird-upflap.png', 'assets/img/yellowbird-midflap.png', 'assets/img/yellowbird-downflap.png'),
)

LISTA_FUNDOS = ('assets/img/background-day.png', 'assets/img/background-night.png')
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

    print("Setup concluído com sucesso!")

if __name__ == '__main__':
    main()