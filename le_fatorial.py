def le_fatorial():

    x = int(input("Digite um número inteiro: "))

    while(x >= 0):

        fat = 1

        while(x > 1):

            fat = fat * x
            x = x - 1

        print(fat)
        x = int(input("Digite um número inteiro: "))
