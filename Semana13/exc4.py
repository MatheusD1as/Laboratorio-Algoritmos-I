numeros = []
for i in range(5):
    numero = int(input("valor:"))
    numeros.append(numero)
maiorNumero = numeros[i]
menorNumero = numeros[i]
for i in range(5):
    if maiorNumero < numeros[i]:
        maiorNumero = numeros[i]
    if menorNumero > numeros[i]:
        menorNumero = numeros[i]
print("O maior número é =", maiorNumero)
print("Menor número =",menorNumero)

