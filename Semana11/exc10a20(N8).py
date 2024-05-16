contador = 0
contador10a20 = 0
for valor in range(0,10):
    valor = float(input("Digite um valor:"))
    if valor < 10 or valor > 20:
        contador += 1
    else:
        contador10a20 += 1
print("Valores fora do intervalo:",contador)
print("Valores dentro do intervalo:",contador10a20)
