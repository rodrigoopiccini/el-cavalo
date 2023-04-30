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


frota = {'navio-tanque': [[[6, 1], [6, 2], [6, 3]]]}
nome_navio = 'navio-tanque'
linha = 4
coluna = 7
orientacao = 'vertical'
tamanho = 3

resultado = preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
print(resultado)


# 3 - faz jogada

def faz_jogada(tabuleiro, linha, coluna):
    posicao = tabuleiro[linha][coluna]

    if posicao == 1:
        tabuleiro[linha][coluna] = 'X'

    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

