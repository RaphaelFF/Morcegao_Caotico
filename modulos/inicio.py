import pygame
import sys
from pygame.locals import *
from itertools import cycle
from configuracoes import LARGURA_DA_TELA, ALTURA_DA_TELA, BASE_Y, FPS
from modulos.interface import tremulacao_jogador

def mostrar_animacao_bem_vindo(TELA, RELOGIO_FPS, IMAGENS, SONS):
    gerador_indice_jogador = cycle([0, 1, 2, 1])
    indice_jogador = 0
    iteracao_loop = 0

    posicao_passaro_x = int(LARGURA_DA_TELA * 0.2)
    posicao_passaro_y = int((ALTURA_DA_TELA - IMAGENS['jogador'][0].get_height()) / 2)

    capa_x = int((LARGURA_DA_TELA - IMAGENS['capa'].get_width()) / 2)
    capa_y = int(ALTURA_DA_TELA * 0)

    base_x = 0
    deslocamento_base = IMAGENS['base'].get_width() - IMAGENS['fundo'].get_width()

    # Variável para o efeito de flutuação
    valores_tremulacao = {'val': 0, 'dir': 1}

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                # O jogador apertou para iniciar
                SONS['asa'].play()
                return {
                    'y_jogador': posicao_passaro_y + valores_tremulacao['val'],
                    'x_base': base_x,
                    'gerador_indice_jogador': gerador_indice_jogador,
                }

        # Atualiza a asa do morcego
        if (iteracao_loop + 1) % 5 == 0:
            indice_jogador = next(gerador_indice_jogador)
        
        iteracao_loop = (iteracao_loop + 1) % 30
        base_x -= 4  # Velocidade fixa de menu
        base_x -= 4  
        deslocamento_base = IMAGENS['base'].get_width() - LARGURA_DA_TELA
        if base_x <= -deslocamento_base:
            base_x = 0
        
        # Chama a função de flutuação 
        tremulacao_jogador(valores_tremulacao)

        # Desenha na tela
        TELA.blit(IMAGENS['fundo'], (0, 0))
        TELA.blit(IMAGENS['jogador'][indice_jogador],
                    (posicao_passaro_x, posicao_passaro_y + valores_tremulacao['val']))
        
        TELA.blit(IMAGENS['base'], (base_x, BASE_Y))
        TELA.blit(IMAGENS['capa'], (capa_x, capa_y))

        pygame.display.update()
        RELOGIO_FPS.tick(FPS)