import random
lista = []
par = 0
impar = 0
for i in range(10):
    numAleat = random.randint(1,50)
    lista.append(numAleat)
for i in range(10):
    if lista[i] % 2 == 0:
        par += 1
    elif lista[i] % 2 == 1:
        impar += 1
print(lista)
print("Quantidade de numeros pares =",par)
print("Quantidade de numeros impares =",impar)
