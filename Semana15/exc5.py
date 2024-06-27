def lista(n1):
    nums = []
    soma = 0
    for i in range(n1, 0, -1):
        nums.append(i)
    for i in range(n1):
        soma += nums[i]
    return soma

def main():
    n1 = int(input("Digite um número: "))
    somaTotal = lista(n1)
    print("A soma de todos os números naturais menores ou iguais a", n1, "é igual a:", somaTotal)

main()