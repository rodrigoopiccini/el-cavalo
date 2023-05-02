# 1 - Define Posições
import random

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

# 6 - posição válida
def posicao_valida (frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes (linha, coluna, orientacao, tamanho)

    if orientacao == 'vertical' and 10 - linha < tamanho:
        return False
    
    if orientacao == 'horizontal' and 10 - coluna < tamanho:
        return False
    

    for posicao in posicoes:
        linha = posicao[0]
        coluna = posicao[1]

        for tipo, posicoes in frota.items():
            for posicao in posicoes:
                for linha_frota, coluna_frota in posicao:
                    if linha == linha_frota and coluna == coluna_frota:
                        return False
                    
    return True


# 7 - posicionando frota
embarcacoes = {1: ['porta-aviões', 4], 2:['navio-tanque', 3], 3:['navio-tanque', 3], 4:['contratorpedeiro', 2], 5:['contratorpedeiro', 2], 6:['contratorpedeiro', 2], 7: ['submarino',1], 8: ['submarino',1], 9: ['submarino',1], 10: ['submarino',1]}
frota = {}
i = 1
while i <= len(embarcacoes):
    nome = embarcacoes[i][0]
    tamanho = embarcacoes[i][1]
    
    print ('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome, tamanho))
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))

    if nome != 'submarino':
        orientacao = int(input('Vertical(1) ou Horizontal(2): '))
        
    if orientacao == 1:
        orientacao = 'vertical'
    elif orientacao == 2:
        orientacao = 'horizontal'

    valido = posicao_valida (frota, linha, coluna, orientacao, tamanho)

    if valido == False:
        print('Esta posição não está válida!')
    
    else:
        lista_posicoes = define_posicoes (linha, coluna, orientacao, tamanho)
        frota = preenche_frota (frota, nome, linha, coluna, orientacao, tamanho)
        i += 1

# 8 - jogadas do jogador
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota) 

lista_linha_coluna_ataque_anterior = []
jogando = True
while jogando:
    def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
        texto = ''
        texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
        texto += '_______________________________      _______________________________\n'
        
        for linha in range(len(tabuleiro_jogador)):
            jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
            oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
            texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
            
        return texto
    
    print (monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha_coluna_invalida = True
    while linha_coluna_invalida:

        linha_invalida = True

        while linha_invalida:
            linha_atacar = int(input('Linha de ataque: '))
            if linha_atacar > 9 or linha_atacar < 0:
                print ('Linha inválida!')
                
            else:
                linha_invalida = False
        
        coluna_invalida = True
    
        while coluna_invalida:
            coluna_atacar = int(input('Coluna de ataque: '))
            if coluna_atacar > 9 or coluna_atacar < 0:
                print ('Coluna inválida!')
                
            else:
                coluna_invalida = False
        
        lista_linha_coluna_ataque = [linha_atacar]
        lista_linha_coluna_ataque. append(coluna_atacar)
        
        if lista_linha_coluna_ataque in lista_linha_coluna_ataque_anterior:
            print ('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(linha_atacar, coluna_atacar))
            
        else:
            lista_linha_coluna_ataque_anterior.append(lista_linha_coluna_ataque)
            linha_coluna_invalida = False

    novo_tabuleiro = faz_jogada(tabuleiro_oponente, linha_atacar, coluna_atacar)
    quantos_afundados = afundados (frota_oponente, novo_tabuleiro)

    if quantos_afundados == 10:
        print ('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

# jogadas do oponente
    lista_linha_coluna_ataque_oponente_anterior = []

    linha_coluna_oponente_invalida = True
    while linha_coluna_oponente_invalida:
        linha_ataque_oponente = random.randint(0,9)
        coluna_ataque_oponente = random.randint(0,9)
        
        lista_linha_coluna_ataque_oponente = [linha_ataque_oponente]
        lista_linha_coluna_ataque_oponente.append(coluna_ataque_oponente)
        
        if lista_linha_coluna_ataque_oponente not in lista_linha_coluna_ataque_oponente_anterior:
            lista_linha_coluna_ataque_oponente_anterior.append(lista_linha_coluna_ataque_oponente)
            linha_coluna_oponente_invalida = False
            print('Seu oponente está atacando na linha {0} e coluna {1}'.format(linha_ataque_oponente, coluna_ataque_oponente))

    novo_tabuleiro = faz_jogada(tabuleiro_jogador, linha_ataque_oponente, coluna_ataque_oponente)
    quantos_afundados = afundados (frota, novo_tabuleiro)

    if quantos_afundados == 10:
        print ('Xi! O oponente derrubou toda a sua frota =(')
        jogando = False













    
