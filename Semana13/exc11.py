lista = []
distinto = 0
for i in range(5):
    valor = int(input("Digite um elemento:"))
    if valor in lista:
        distinto += 1 
    lista.append(valor)
if distinto < 1:
    print("Todos os elementos são distintos")
else:
    print("Nem todos os elementos são distintos")