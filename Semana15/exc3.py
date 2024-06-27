def dobro(n1):
    dobro = n1 * 2
    return dobro
def main():
    n1 = float(input("Digite um valor:"))
    multiplicador = dobro(n1)
    print("O dobro de",n1,"é",multiplicador)
    

main()