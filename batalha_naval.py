# 1 - Define Posições
def define_posicoes (linha, coluna, orientacao, tamanho):
    lista = []

    if orientacao == 'vertical':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha+i)
            posicao.append(coluna)
            lista.append(posicao)

    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicao = []
            posicao.append(linha)
            posicao.append(coluna+i)
            lista.append(posicao)


    return lista
    
# 2 - Preenche frota
def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):


    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))

    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]

    
    return frota

# 3 - faz jogada
def faz_jogada(tabuleiro, linha, coluna):
    posicao = tabuleiro[linha][coluna]

    if posicao == 1:
        tabuleiro[linha][coluna] = 'X'

    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

# 4 - posiciona frota
def posiciona_frota(frota):

    tabuleiro = [[0 for i in range(10)] for j in range(10)]
    
    for tipo, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                tabuleiro[linha][coluna] = 1
    
    return tabuleiro

# 5 - quantas embarcações afundadas?
def afundados (frota, tabuleiro):
    contador = 0

    for tipo, posicoes in frota.items():
        for posicao in posicoes:
            for linha, coluna in posicao:
                if tabuleiro[linha][coluna] == 'X':
                    continua = True

                else:
                    continua = False
                    break

            if continua:
                contador += 1
    
    return contador

