habitantes = 0
somaSalario = 0
maiorIdade = 0
menorIdade = 1000
mulheres10k = 0
while habitantes <= 10:
    idade = int(input("Idade:"))
    print("Digite seu sexo M/F:")
    sexo =input("Sexo:").upper()
    salario = float(input("Salário:"))
    habitantes += 1
    somaSalario += salario
    mediaSalario = somaSalario/10
    if idade > maiorIdade:
       maiorIdade = idade 
    if idade < menorIdade:
        idade = menorIdade  
    if sexo == "F" and salario <=10000:
        mulheres10k += 1
print("Média salarial:",mediaSalario)
print("Maior idade =",maiorIdade,"e menor idade =", menorIdade)
print("Quantidade de mulheres com salário até 10.000 =",mulheres10k)
