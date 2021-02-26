
lista = []

while True:

    x = int(input("Digite um número: "))

    if x == 0:
        break

    lista.append(x)

for y in reversed(lista):
    print(y)
    
