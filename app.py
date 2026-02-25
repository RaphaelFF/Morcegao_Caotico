import random
import sys
import pygame
from pygame.locals import *
from configuracoes import *
from modulos.utilitarios import obter_mascara_colisao
from modulos.inicio import mostrar_animacao_bem_vindo
from modulos.jogo import jogo_principal
from modulos.fim_de_jogo import mostrar_tela_game_over

# Dicionários globais para armazenar os recursos carregados
IMAGENS, SONS, MASCARAS_COLISAO = {}, {}, {}

def main():
    global TELA, RELOGIO_FPS
    pygame.init()
    RELOGIO_FPS = pygame.time.Clock()
    TELA = pygame.display.set_mode((LARGURA_DA_TELA, ALTURA_DA_TELA))
    pygame.display.set_caption('Morcegão Caótico')
    
    # ícone da janela
    try:
        icone = pygame.image.load('assets/img/morcego-asa-aberta.png').convert_alpha()
        pygame.display.set_icon(icone)
    except FileNotFoundError:
        print("Ícone não encontrado - usando ícone padrão")
    
    # Carregamento de imagens e sons
    IMAGENS['numeros'] = tuple(pygame.image.load(f'assets/img/{i}.png').convert_alpha() for i in range(10))
    IMAGENS['fundos'] = [pygame.image.load(caminho).convert() for caminho in LISTA_FUNDOS]
    IMAGENS['fundo'] = IMAGENS['fundos'][0]
    IMAGENS['gameover'] = pygame.image.load('assets/img/gameover2.png').convert_alpha()
    IMAGENS['capa'] = pygame.image.load('assets/img/capa2.png').convert_alpha()
    IMAGENS['base'] = pygame.image.load('assets/img/base2.png').convert_alpha()

    # Sons
    extensao = '.wav' if 'win' in sys.platform else '.ogg'
    SONS['morrer'] = pygame.mixer.Sound(f'assets/audio/die{extensao}')
    SONS['bater'] = pygame.mixer.Sound(f'assets/audio/hit{extensao}')
    SONS['ponto'] = pygame.mixer.Sound(f'assets/audio/ponto{extensao}')
    SONS['swoosh'] = pygame.mixer.Sound(f'assets/audio/swoosh{extensao}')
    SONS['asa'] = pygame.mixer.Sound(f'assets/audio/bater-asas{extensao}')

    while True:
        # Sorteio de Fundo e Personagem
        indice_fundo = random.randint(0, len(LISTA_FUNDOS) - 1)
        IMAGENS['fundo'] = pygame.image.load(LISTA_FUNDOS[indice_fundo]).convert()

        indice_jogador = random.randint(0, len(LISTA_JOGADORES) - 1)
        IMAGENS['jogador'] = (
            pygame.image.load(LISTA_JOGADORES[indice_jogador][0]).convert_alpha(),
            pygame.image.load(LISTA_JOGADORES[indice_jogador][1]).convert_alpha(),
            pygame.image.load(LISTA_JOGADORES[indice_jogador][2]).convert_alpha(),
        )

        # Configuração de Canos e Máscaras
        indice_cano = random.randint(0, len(LISTA_CANOS) - 1)
        IMAGENS['cano'] = (
            pygame.transform.flip(pygame.image.load(LISTA_CANOS[indice_cano]).convert_alpha(), False, True),
            pygame.image.load(LISTA_CANOS[indice_cano]).convert_alpha(),
        )

        MASCARAS_COLISAO['cano'] = (obter_mascara_colisao(IMAGENS['cano'][0]), obter_mascara_colisao(IMAGENS['cano'][1]))
        MASCARAS_COLISAO['jogador'] = [obter_mascara_colisao(img) for img in IMAGENS['jogador']]

        # --- FLUXO DO JOGO ---
        
        # 1. Tela Inicial
        info_movimento = mostrar_animacao_bem_vindo(TELA, RELOGIO_FPS, IMAGENS, SONS)
        
        # 2. Partida
        info_colisao = jogo_principal(TELA, RELOGIO_FPS, IMAGENS, SONS, MASCARAS_COLISAO, info_movimento)
        
        # 3. Tela de Game Over
        mostrar_tela_game_over(TELA, RELOGIO_FPS, IMAGENS, SONS, info_colisao)

if __name__ == '__main__':
    main()