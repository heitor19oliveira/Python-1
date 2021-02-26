

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

l = largura
a = altura

while(altura > 0):

    t = 0

    while(t < largura):

        if(altura == (a) or t == (l - 1) or altura == 1 or t == 0):
            print("#", end = '')
        else:
            print(" ", end = '')
        t = t + 1

    altura = altura - 1
    print()
