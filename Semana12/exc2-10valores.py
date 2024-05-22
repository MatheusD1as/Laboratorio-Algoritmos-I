valores=[]
maior100 = 0
for i in range(0,10):
    valor = int(input("Digite um valor:"))
    valores.append(valor)
valoresMaior100 = []
for i in range(0,10):
    if valores[i]>100:
        maior100 += 1
        valoresMaior100.append(valores[i]) 
print("Quantidade de valores maiores que 100:",maior100)
print("Todos os valores maiores que 100:", valoresMaior100)
