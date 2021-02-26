def computador_escolhe_jogada(n, m):
    print("\nVez do computador!")

    if(n <= m):
        return n
    else:
        retirar = n % (m + 1)
        if (retirar > 0):
            return retirar
        else:
            return m
    
        
def usuario_escolhe_jogada(n, m):
    print("\nSua Vez!")
    retirar = 0
    while retirar == 0:
        retirar = int(input("Quantas peças irá tirar? "))

        if retirar > n or retirar < 1 or retirar > m:
            retirar = 0
            print("Oops! Jogada inválida! Tente de novo.")

    return retirar


def partida():

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    vez_computador = True

    if((n % (m + 1) == 0)):
        vez_computador = False

    while n > 0:
        if vez_computador:
            retirar = computador_escolhe_jogada(n, m)
            vez_computador = False
            print("O computador retirou {} peças.".format(retirar))
        else:
            retirar = usuario_escolhe_jogada(n, m)
            vez_computador = True
            print("Você retirou {} peças.".format(retirar))

        n = n - retirar

        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam apenas {} peças no tabuleiro.\n".format(n))

    if vez_computador:
        print("Você ganhou!")
    else:
        print("Fim do jogo! O computador ganhou!")
            
            
            


        
        
    

    


