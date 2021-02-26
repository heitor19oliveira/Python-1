import math

a = float(input("Digite valor de a: "))
b = float(input("Digite valor de b: "))
c = float(input("Digite valor de c: "))

delta = b**2 - 4*a*c

if (delta == 0):
    x = -b / (2*a)
    print("a raiz desta equação é", x)
else:
    if delta < 0:
        print("esta equação não possui raizes reais")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("as raízes da equação são", x1, "e", x2)