import random

# PARA TESTAS O SEU CÓDIGO NA ACADEMIA PYTHON SERÁ NECESSÁRIO COLAR AS FUNÇÕES DESENVOLVIDAS AQUI!!!
import funcoes 

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    '''
    tabuleiro_jogador: tabuleiro do jogador
    tabuleiro_oponente: tabuleiro do oponente
    Função monta uma string com a representação dos tabuleiros do jogador e do oponente.
    O tabuleiro do jogador é representado por um tabuleiro com as posições dos navios.
    O tabuleiro do oponente é representado por um tabuleiro com as posições que o jogador já atirou.
    '''

    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item)
                                  for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join(
            [info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    texto += '_______________________________      _______________________________\n'
    return texto


def gerando_frota_automaticamente():
    '''
    Função gera uma frota de navios de forma aleatória.
    '''
    quantidades = {
        "submarino": {
            "quantidade": 4,
            "tamanho": 1
        },
        "destroyer": {
            "quantidade": 3,
            "tamanho": 2
        },
        "navio-tanque": {
            "quantidade": 2,
            "tamanho": 3
        },
        "porta-aviões": {
            "quantidade": 1,
            "tamanho": 4
        }
    }

    frota = []

    for nome_navio, info in quantidades.items():
        for _ in range(info["quantidade"]):
            dados_de_posicionamento = {
                "tamanho": info["tamanho"],
            }
            dados_de_posicionamento["orientacao"] = random.choice(
                ["vertical", "horizontal"])
            dados_de_posicionamento["linha"] = random.randint(0, 9)
            dados_de_posicionamento["coluna"] = random.randint(0, 9)

            while not funcoes.posicao_valida(dados_de_posicionamento, frota):
                dados_de_posicionamento["orientacao"] = random.choice(
                    ["vertical", "horizontal"])
                dados_de_posicionamento["linha"] = random.randint(0, 9)
                dados_de_posicionamento["coluna"] = random.randint(0, 9)

            funcoes.preenche_frota(dados_de_posicionamento, nome_navio, frota)

    return frota


# Gerando frota de forma aleatório para jogadores
frota_jogador = gerando_frota_automaticamente()
frota_oponente = gerando_frota_automaticamente()

# Criando tabuleiro com as frotas posicionadas
tabuleiro_jogador = funcoes.posiciona_frota(frota_jogador)
tabuleiro_oponente = funcoes.posiciona_frota(frota_oponente)
jogando = True
#Função para validar as entradas do jogador:
def entrada(n):
    if n in range(0,10):
        return True
    return False    

entradas = []
entradas_opo = []
while jogando:
    # Imprimindo tabuleiro
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    pergunta = True
    while pergunta:
        linha = int(input('Digite a linha: '))
        while not entrada(linha):
            print('Linha inválida!')
            linha = int(input('Digite a linha: '))
        coluna = int(input('Digite a coluna: '))
        while not entrada(coluna):
            print('Coluna inválida!')
            coluna = int(input('Digite a coluna: '))

        
        tiro = [linha, coluna]
        if tiro not in entradas:
            entradas.append(tiro)
            tabuleiro_oponente = funcoes.faz_jogada(tabuleiro_oponente, linha, coluna)
            pergunta = False
        else:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')

    if funcoes.afundados(frota_oponente, tabuleiro_oponente) == len(frota_oponente):
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
        break
    
    sorteia = True
    while sorteia:
        linha_opo = random.randint(0,9)
        coluna_opo = random.randint(0,9)
        opo = [linha_opo, coluna_opo]
        if opo not in entradas_opo:
            entradas_opo.append(opo)
            tabuleiro_jogador = funcoes.faz_jogada(tabuleiro_jogador, linha_opo, coluna_opo)
            print(f'Seu oponente está atacando na linha {linha_opo} e coluna {coluna_opo}')
            sorteia = False
    
    if funcoes.afundados(frota_jogador, tabuleiro_jogador) == len(frota_jogador):
        print('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False
    