lista1 = []
lista2 = []
lista3 = []
for i in range(5):
    lista1.append(int(input("Digite um elemento inteiro para lista 1:")))
for i in range(5):
    lista2.append(int(input("Digite um elemento inteiro para lista 2:")))
for i in range(5):
    lista3.append(lista1[i]*lista2[i])
print(lista1)
print(lista2)
print(lista3)
