valoresA = []
valoresB = []
valoresC = []
tamanho = int(input("Digite o tamanho da listagem:"))
for i in range(tamanho):
    valorA = int(input("Insira um valor na lista A:"))
    valoresA.append(valorA)
    valorB = int(input("Insira um valor na lista B:"))
    valoresB.append(valorB)
for i in range(tamanho):
    valoresC.append(valoresA[i] + valoresB[i])
print("Lista A:",valoresA)
print("Lista B:",valoresB)
print("Lista C:",valoresC)