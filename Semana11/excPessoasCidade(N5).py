maiorIdade = 0
SexFemIda18a35olhoVcabeloLouro = 0
olhoA = 0
olhoV = 0
olhoC = 0
cabeloL = 0
cabeloC = 0
cabeloP = 0
sexoM = 0
sexoF = 0
maiorIdade = -1
for pessoas in range(0,14):
    sexo = input("Digite seu sexo F | M  :").upper()
    olho = input("Digite a cor dos seus olhos A(azuis) | V(verdes) | C(castanhos):").upper()
    cabelo = input("Digite a cor do seu cabelo L(louro) | C(castanho) | P(preto):").upper()
    idade = int(input("Digite sua idade:"))
    if maiorIdade < idade:
        maiorIdade = idade
    if sexo == "F" and (idade >= 18 and idade <=35) and olho == "V" and cabelo == "L":
        SexFemIda18a35olhoVcabeloLouro += 1
    if olho == "A":
        olhoA += 1
    if olho == "V":
        olhoV += 1
    if olho == "C":
        olhoC += 1
    if cabelo == "L":
        cabeloL += 1
    if cabelo == "C":
        cabeloC += 1
    if cabelo == "P":
        cabeloP += 1
    if sexo == "M":
        sexoM += 1
    if sexo == "F":
        sexoF += 1
print("Maior idade =",maiorIdade)
print("A quantidade de indivíduos do sexo feminino, cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros é =",SexFemIda18a35olhoVcabeloLouro)
print("Porcentagem de olhos azuis =",(olhoA/15)*100)
print("Porcentagem de olhos verdes =",(olhoV/15)*100)
print("Porcentagem de olhos castanhos =",(olhoC/15)*100)
print("Porcentagem de cabelos loiros =",(cabeloL/15)*100)
print("Porcentagem de cabelos castanhos =",(cabeloC/15)*100)
print("Porcentagem de cabelos pretos =",(cabeloP/15)*100)
print("Porcentagem do sexo masculino =",(sexoM/15)*100)
print("Porcentagem do sexo feminino =",(sexoF/15)*100)
