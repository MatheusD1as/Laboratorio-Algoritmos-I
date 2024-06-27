def primo(n1):
    nPrimo = 0
    for i in range(2,int(n1/2)):
        if n1 % i == 0:
            nPrimo = 1
            return False
    if nPrimo == 0:
        return True
def main():
    n1 = int(input("N1:"))
    condicao = primo(n1)
    print(condicao)
main()