def fatorial(x):
    fat = 1

    while(x > 1):

        fat = fat * x
        x = x - 1

    print(fat)

def main():

    y = int(input("Digite um número inteiro: "))
   
    while(y >= 0):

        resp = fatorial(y)

        print(resp)
        y = int(input("Digite um número inteiro: "))


        
        
    
