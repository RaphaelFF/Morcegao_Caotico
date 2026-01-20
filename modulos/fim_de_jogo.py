import pygame, sys
from pygame.locals import *
from configuracoes import *
from modulos.interface import mostrar_pontuacao

def mostrar_tela_game_over(TELA, RELOGIO_FPS, IMAGENS, SONS, info_colisao):
    pontuacao = info_colisao['pontuacao']
    posicao_passaro_x = LARGURA_DA_TELA * 0.2
    posicao_passaro_y = info_colisao['y']
    altura_passaro = IMAGENS['jogador'][0].get_height()
    velocidade_passaro_y = info_colisao['velocidade_y_jogador']
    aceleracao_passaro_y = 2
    base_x = info_colisao['x_base']
    canos_superiores = info_colisao['canos_superiores']
    canos_inferiores = info_colisao['canos_inferiores']

    # Sons de impacto
    SONS['bater'].play()
    if not info_colisao['colisao_chao']:
        SONS['morrer'].play()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN and (event.key in [K_SPACE, K_UP]):
                # Se o morcego já caiu no chão, pode reiniciar
                if posicao_passaro_y + altura_passaro >= BASE_Y - 1:
                    return

        # Física da queda após morrer
        if posicao_passaro_y + altura_passaro < BASE_Y - 1:
            posicao_passaro_y += min(velocidade_passaro_y, BASE_Y - posicao_passaro_y - altura_passaro)
            if velocidade_passaro_y < 15:
                velocidade_passaro_y += aceleracao_passaro_y

        # Desenha o cenário parado (morte)
        TELA.blit(IMAGENS['fundo'], (0,0))
        for c_sup, c_inf in zip(canos_superiores, canos_inferiores):
            TELA.blit(IMAGENS['cano'][0], (c_sup['x'], c_sup['y']))
            TELA.blit(IMAGENS['cano'][1], (c_inf['x'], c_inf['y']))
        
        TELA.blit(IMAGENS['base'], (base_x, BASE_Y))
        mostrar_pontuacao(TELA, pontuacao, IMAGENS['numeros'])
        
        # Centraliza a imagem de Game Over
        gameover_x = (LARGURA_DA_TELA - IMAGENS['gameover'].get_width()) / 2
        TELA.blit(IMAGENS['gameover'], (gameover_x, ALTURA_DA_TELA * 0.4))
        
        # Desenha o morcego na posição da morte
        TELA.blit(IMAGENS['jogador'][1], (posicao_passaro_x, posicao_passaro_y))

        pygame.display.update()
        RELOGIO_FPS.tick(FPS)