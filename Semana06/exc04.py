qtdPessoas = 0
somaIdade = 0
somaPeso = 0
maiorIdade = 0
pessoas10a30 = 0
while qtdPessoas <= 7:
    idade = float(input("Idade:"))
    peso = float(input("Peso:"))
    qtdPessoas += 1
    somaIdade += idade
    mediaIdade = somaIdade/7
    if idade >= 18:
        maiorIdade += 1
    if idade >= 10 and idade <= 30:
        pessoas10a30 += 1
print("Média de idade =",mediaIdade)
print("Maiores de idade =",maiorIdade)
print("Porcentagem de pessoas entre 10 e 30 anos é de:", (pessoas10a30/7) * (100),"%")

