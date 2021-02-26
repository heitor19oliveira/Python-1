

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

while(altura > 0):

    t = 0

    while(t < largura):
        print("#", end ='')
        t = t + 1

    altura = altura - 1
    print()
