import pygame
from pygame.locals import *

FPS = 30
LARGURA_DA_TELA = 288
ALTURA_DA_TELA = 512
BASE_Y = ALTURA_DA_TELA * 0.79 
ESPACO_TUBO = 120 
VELOCIDADE_BASE = -4
TRANSICAO = 10 # qunatidade de pontuacao para a transicao de, velocidade, troca de cenario, troca de cano


LISTA_JOGADORES = (
    (
        'assets/img/asa-fechada.png',
        'assets/img/asa-aberta.png',
        'assets/img/asa-fechada.png',
    ),
    (
        'assets/img/asa-fechada.png',
        'assets/img/asa-aberta.png',
        'assets/img/asa-fechada.png',
    ),
    (
        'assets/img/asa-fechada.png',
        'assets/img/asa-aberta.png',
        'assets/img/asa-fechada.png',
    ),
)

# Lista de fundos disponíveis
LISTA_FUNDOS = (
    'assets/img/fundo1.png',
    'assets/img/cenario-verde.png', 
    'assets/img/cenario-cemiterio.png', 
)

# Lista de variações de canos
LISTA_CANOS = (
    'assets/img/cano-roxo.png',
    'assets/img/cano-blue.png',
    'assets/img/cano-t.png',
    'assets/img/cano-vermelho.png',
    
)