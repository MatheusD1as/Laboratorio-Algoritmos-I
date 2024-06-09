vetor = []
inverso = []
for i in range(0,5):
    valor = int(input("VALOR:"))
    vetor.append(valor)
for i in range(4,-1,-1):
    inverso.append(vetor[i])
print(inverso)
