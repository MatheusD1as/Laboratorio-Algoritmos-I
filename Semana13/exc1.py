vetor= [1,2,3,4,5,6,7,8,9,10]
vetorInverso = []
for i in range(len(vetor),0,-1):
    vetorInverso.append(vetor[i-1])
print(vetorInverso)
