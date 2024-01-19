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
