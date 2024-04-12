cont = 1
somaTotal = 0
idade = maiorIdade = menorIdade = int(input("Digite sua idade:"))
somaTotal += idade
while cont< 25:
    idade = int(input("Digite sua idade:"))
    somaTotal += idade
    if idade > maiorIdade:
        maiorIdade = idade
    elif idade < menorIdade:
        menorIdade = idade
    cont += 1
media = somaTotal/cont
print("Maior Idade:",maiorIdade)
print("Menor Idade:",menorIdade)
print("Media das idades:",media)
