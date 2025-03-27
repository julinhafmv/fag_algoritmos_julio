import os

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(f"{linha[0]} | {linha[1]} | {linha[2]}")
        print("----------")

def realizar_jogada():
    while True:
        try:
            linha = int(input("Selecione uma linha: "))
            coluna = int(input("Selecione uma coluna: "))
            return linha , coluna
        except:
            print("Valor inválido")

def verificar_vencedor(tabuleiro):
        #verificar linha
        for linha in tabuleiro:
            if linha[0] == linha[1] == linha[2] != " ":
                return linha[0]
        #verificar coluna
        for coluna in range(3):
            if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
                return tabuleiro[0][coluna]
        #verificar diagonal
        for diagonal in tabuleiro:
            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
                return tabuleiro[2][0]
def jogo_da_velha():
    #inicializar o jogo
   
    tabuleiro = ([" "," "," "],[" "," "," "],[" "," "," "])
    jogador = "X"

    while True:
        os.system ("cls" if os.name == "nt" else "clear")
        #imprimir o tabuleiro
        imprimir_tabuleiro(tabuleiro)
        
        #realizar a jogada
        linha, coluna = realizar_jogada()

        #atualizar o tabuleiro
        if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
            continue
        tabuleiro[linha][coluna] = jogador

        #trocar jogador
        if jogador == "X":
            jogador= "O"
        else:
            jogador = "X"
        

jogo_da_velha()