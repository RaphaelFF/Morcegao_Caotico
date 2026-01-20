import pygame
from configuracoes import LARGURA_DA_TELA, ALTURA_DA_TELA, BASE_Y

def mostrar_pontuacao(TELA, pontuacao, IMAGENS_NUMEROS):
    digitos = [int(x) for x in list(str(pontuacao))]
    largura_total = sum(IMAGENS_NUMEROS[d].get_width() for d in digitos)
    deslocamento_x = (LARGURA_DA_TELA - largura_total) / 2

    for digito in digitos:
        TELA.blit(IMAGENS_NUMEROS[digito], (deslocamento_x, ALTURA_DA_TELA * 0.1))
        deslocamento_x += IMAGENS_NUMEROS[digito].get_width()

def tremulacao_jogador(tremulacao):
    if abs(tremulacao['val']) == 8:
        tremulacao['dir'] *= -1
    tremulacao['val'] += tremulacao['dir']