import pygame
import random
from configuracoes import LARGURA_DA_TELA, BASE_Y, ESPACO_TUBO

def obter_mascara_colisao(imagem):
    return pygame.mask.from_surface(imagem)

def colisao_pixel(ret1, ret2, mascara1, mascara2):
    distancia_x = ret2.x - ret1.x
    distancia_y = ret2.y - ret1.y
    return mascara1.overlap(mascara2, (distancia_x, distancia_y))

def obter_cano_aleatorio(IMAGENS_CANO):
    posicao_gap_y = random.randrange(0, int(BASE_Y * 0.6 - ESPACO_TUBO))
    posicao_gap_y += int(BASE_Y * 0.2)
    altura_cano = IMAGENS_CANO[0].get_height()
    posicao_cano_x = LARGURA_DA_TELA + 10

    return [
        {'x': posicao_cano_x, 'y': posicao_gap_y - altura_cano},  # cano superior
        {'x': posicao_cano_x, 'y': posicao_gap_y + ESPACO_TUBO},  # cano inferior
    ]

def verificar_colisao(jogador, canos_superiores, canos_inferiores, IMAGENS, MASCARAS_COLISAO):
    # 1. Checa colisão com o chão
    if jogador['y'] + IMAGENS['jogador'][0].get_height() >= BASE_Y - 1:
        return [True, True]
    
    # 2. Checa colisão com os canos
    retangulo_jogador = pygame.Rect(jogador['x'], jogador['y'], IMAGENS['jogador'][0].get_width(), IMAGENS['jogador'][0].get_height())
    
    for c_sup, c_inf in zip(canos_superiores, canos_inferiores):
        ret_sup = pygame.Rect(c_sup['x'], c_sup['y'], IMAGENS['cano'][0].get_width(), IMAGENS['cano'][0].get_height())
        ret_inf = pygame.Rect(c_inf['x'], c_inf['y'], IMAGENS['cano'][1].get_width(), IMAGENS['cano'][1].get_height())

        if colisao_pixel(retangulo_jogador, ret_sup, MASCARAS_COLISAO['jogador'][jogador['index']], MASCARAS_COLISAO['cano'][0]) or \
           colisao_pixel(retangulo_jogador, ret_inf, MASCARAS_COLISAO['jogador'][jogador['index']], MASCARAS_COLISAO['cano'][1]):
            return [True, False]

    return [False, False]