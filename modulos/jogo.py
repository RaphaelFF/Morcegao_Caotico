import pygame, sys
from pygame.locals import *
from configuracoes import *
from modulos.utilitarios import obter_cano_aleatorio, verificar_colisao
from modulos.interface import mostrar_pontuacao

def jogo_principal(TELA, RELOGIO_FPS, IMAGENS, SONS, MASCARAS_COLISAO, info_movimento):
    alpha_transicao = 0  
    fundo_antigo_indice = 0
    pontuacao = indice_jogador = iteracao_loop = 0
    gerador_indice_jogador = info_movimento['gerador_indice_jogador']
    
    # Posições iniciais vindas da tela de boas-vindas
    posicao_passaro_x = int(LARGURA_DA_TELA * 0.2)
    posicao_passaro_y = info_movimento['y_jogador']
    base_x = info_movimento['x_base']
    deslocamento_base = IMAGENS['base'].get_width() - IMAGENS['fundo'].get_width()

    # Gerar canos iniciais
    novo_cano1 = obter_cano_aleatorio(IMAGENS['cano'])
    novo_cano2 = obter_cano_aleatorio(IMAGENS['cano'])

    canos_superiores = [
        {'x': LARGURA_DA_TELA + 200, 'y': novo_cano1[0]['y'], 'passou': False},
        {'x': LARGURA_DA_TELA + 200 + (LARGURA_DA_TELA / 2), 'y': novo_cano2[0]['y'], 'passou': False}
    ]
    canos_inferiores = [
        {'x': LARGURA_DA_TELA + 200, 'y': novo_cano1[1]['y'], 'passou': False},
        {'x': LARGURA_DA_TELA + 200 + (LARGURA_DA_TELA / 2), 'y': novo_cano2[1]['y'], 'passou': False},
    ]

    # Variáveis de física
    velocidade_passaro_y = -9
    velocidade_max_passaro_y = 10
    aceleracao_passaro_y = 1
    aceleracao_batida_asa = -9
    bateu_asa = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit(); sys.exit()
            if event.type == KEYDOWN and (event.key in [K_SPACE, K_UP]):
                if posicao_passaro_y > -2 * IMAGENS['jogador'][0].get_height():
                    velocidade_passaro_y = aceleracao_batida_asa
                    bateu_asa = True
                    SONS['asa'].play()

        # Verifica Colisões
        status_colisao = verificar_colisao(
            {'x': posicao_passaro_x, 'y': posicao_passaro_y, 'index': indice_jogador},
            canos_superiores, canos_inferiores, IMAGENS, MASCARAS_COLISAO
        )
        
        if status_colisao[0]: # Se colidiu
            return {
                'y': posicao_passaro_y,
                'colisao_chao': status_colisao[1],
                'x_base': base_x,
                'canos_superiores': canos_superiores,
                'canos_inferiores': canos_inferiores,
                'pontuacao': pontuacao,
                'velocidade_y_jogador': velocidade_passaro_y
            }

        # Lógica da Pontuação
        centro_jogador = posicao_passaro_x + IMAGENS['jogador'][0].get_width() / 2

        for c_sup in canos_superiores:
            centro_cano = c_sup['x'] + IMAGENS['cano'][0].get_width() / 2
            
            # Se o centro do jogador passou o centro do cano e o cano ainda não deu ponto
            if centro_cano <= centro_jogador and not c_sup['passou']:
                pontuacao += 1
                c_sup['passou'] = True # Marca para não pontuar de novo
                SONS['ponto'].play()

        # Gravidade do pássaro
        if velocidade_passaro_y < velocidade_max_passaro_y and not bateu_asa:
            velocidade_passaro_y += aceleracao_passaro_y
        if bateu_asa:
            bateu_asa = False
        
        altura_passaro = IMAGENS['jogador'][indice_jogador].get_height()
        posicao_passaro_y += min(velocidade_passaro_y, BASE_Y - posicao_passaro_y - altura_passaro)

        # Movimenta Canos
        nivel_velocidade = pontuacao // 2
        velocidade_atual = VELOCIDADE_BASE - nivel_velocidade 

        for c_sup, c_inf in zip(canos_superiores, canos_inferiores):
            c_sup['x'] += velocidade_atual
            c_inf['x'] += velocidade_atual

        # Adiciona novos canos e remove os antigos
        if canos_superiores[-1]['x'] < LARGURA_DA_TELA / 2:
            novo_cano = obter_cano_aleatorio(IMAGENS['cano'])
            canos_superiores.append(novo_cano[0])
            canos_inferiores.append(novo_cano[1])

        if canos_superiores[0]['x'] < -IMAGENS['cano'][0].get_width():
            canos_superiores.pop(0)
            canos_inferiores.pop(0)
            
        # Atualiza índices e movimentos
        if (iteracao_loop + 1) % 3 == 0:
            indice_jogador = next(gerador_indice_jogador)
        iteracao_loop = (iteracao_loop + 1) % 30
        base_x = -((-base_x - velocidade_atual) % deslocamento_base)

        # Lógica de transição suave
        indice_cenario = (pontuacao // 2) % len(IMAGENS['fundos']) 
        # Desenha sempre o fundo antigo por baixo
        TELA.blit(IMAGENS['fundos'][fundo_antigo_indice], (0, 0))
        if indice_cenario != fundo_antigo_indice:
            fundo_novo = IMAGENS['fundos'][indice_cenario].copy()
            fundo_novo.set_alpha(alpha_transicao)
            TELA.blit(fundo_novo, (0, 0))
            
            alpha_transicao += 5  
            
            if alpha_transicao >= 255:
                fundo_antigo_indice = indice_cenario
                alpha_transicao = 0
                
        for c_sup, c_inf in zip(canos_superiores, canos_inferiores):
            TELA.blit(IMAGENS['cano'][0], (c_sup['x'], c_sup['y']))
            TELA.blit(IMAGENS['cano'][1], (c_inf['x'], c_inf['y']))

        TELA.blit(IMAGENS['base'], (base_x, BASE_Y))
        mostrar_pontuacao(TELA, pontuacao, IMAGENS['numeros'])
        TELA.blit(IMAGENS['jogador'][indice_jogador], (posicao_passaro_x, posicao_passaro_y))

        pygame.display.update()
        RELOGIO_FPS.tick(FPS)