numeros = []
maior30 = 0
soma30 = 0
soma = 0
for i in range(0,4):
   numero = int(input("Numero:"))
   soma += numero
   numeros.append(numero)
for i in range(0,4):
   if numeros[i] > 30:
        maior30 += 1
        soma30 += numeros[i]
print("Quantidade de numeros maiores que 30: ",maior30)
print("Soma dos numeros maiores que 30:",soma30)
print("Soma de todos os numeros:",soma)
