vetorA = []
vetorB = []
for i in range(0,10):
    valorA = int(input("VALOR:"))
    vetorA.append(valorA)
for i in range(9,-1,-1):
    vetorB.append(vetorA[i])
print(vetorB)
