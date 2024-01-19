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

def posiciona_frota(frota):
    grade = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    for navio in frota:
        posicoes = navio['posicoes']
        for coord in posicoes:
            linha = coord[0]
            col = coord[1]
            grade[linha][col] = 1
    return grade

def afundados(frota, tabuleiro):
    conta_afun = 0
    for navio in frota:
        posicoes = navio['posicoes']
        tamanho = len(posicoes)
        afundou = True 
        if tamanho == 1:
            linha = posicoes[0][0]
            coluna = posicoes[0][1]
            if tabuleiro[linha][coluna] != 'X':
                afundou = False
        elif tamanho >= 2:
            for coord in posicoes:
                linha = coord[0]
                coluna = coord[1]
                if tabuleiro[linha][coluna] != 'X':
                    afundou = False
                    break  
        if afundou:
            conta_afun += 1
    return conta_afun