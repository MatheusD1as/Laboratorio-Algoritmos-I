import random
lista = []
pares = []
for i in range(0,10):
    numAleat = random.randint(1,100)
    lista.append(numAleat)
    if lista[i] % 2 == 0:
        pares.append(lista[i])
print(lista)
print(pares)
