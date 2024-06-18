def somaImposto():
    taxaImposto = float(input("Digite a porcentagem da taxa:"))
    custo = float(input("Digite o custo sem imposto do item:"))
    vf = (custo *(+1 +(taxaImposto/100)))
    print("O valor de custo antes do imposto era de", custo,"R$ e agora com uma taxa de", taxaImposto,'%'"o valor passa a ser de",vf,"R$")
def main():
    somaImposto()
main()