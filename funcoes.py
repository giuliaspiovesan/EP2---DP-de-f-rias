def define_posicoes(dic):
    l = dic['linha']
    col = dic['coluna']
    ori = dic['orientacao']
    tam = dic['tamanho']
    i = 1
    saida = []
    if ori == 'vertical':
        while i <= tam:
            saida.append([l, col])
            l += 1
            i += 1
    else:
        while i <= tam:
            saida.append([l, col])
            col += 1
            i += 1
    return saida

def preenche_frota(dic_infos, nome, frota):
    posicoes = define_posicoes(dic_infos)
    dic_navio = {}
    dic_navio['tipo'] = nome
    dic_navio['posicoes'] = posicoes
    frota.append(dic_navio)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro