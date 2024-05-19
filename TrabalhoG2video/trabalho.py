torcedor = 0
tv = 0
estadio = 0
somaIdade = 0
somaIdadeTv = 0
somaIdadeEstadio = 0
somaPeso = 0

while torcedor < 300:
    print("###  Menu ###")
    print("Opção 1 - Entrevistar torcedor")
    print("Opção 2 - Apresentar resultado parcial")
    print("Opção 3 - Sair")
    opc = int(input("Digite a opção:"))
    if opc == 1:
        nome = input("Nome:")
        idade = int(input("Idade:"))
        peso = float(input("Peso:"))
        timeCoracao = input("Time do coração:")
        print("Onde prefere assistir aos jogos:")
        print("1 - Assistir na TV")
        print("2 - Assistir no Estádio")
        opc2 = int(input("Digite a preferência do torcedor:"))
        if opc2 == 1:
            tv += 1
            somaIdadeTv += idade
        elif opc2 == 2:
            estadio += 1
            somaIdadeEstadio += idade
        if torcedor == 0:
            primeiroNome = nome
            menorPeso = peso
            maiorIdade = idade
            maisMagro = nome
            maisVelho = nome
        if menorPeso > peso:
            menorPeso = peso
            maisMagro = nome
        if maiorIdade < idade:
            maiorIdade = idade
            maisVelho = nome
        ultimoNome = nome
        somaIdade += idade 
        somaPeso += peso
        torcedor += 1
    elif opc == 2:
        print("A média parcial das idades dos torcedores é de:",somaIdade/torcedor)
        print("O nome do torcedor mais magro é:",maisMagro)
        print("O nome do torcedor mais velho é:",maisVelho)
        print("Porcentagem de pessoas que preferem assistir na TV =",(tv/torcedor)*100,"%")
        print("Porcentagem de pessoas que preferem assistir no estadio =",(estadio/torcedor)*100,"%")
        print("Total de pessoas que preferem assistir na TV =", tv)
        print("Total de pessoas que preferem assistir no estádio =", estadio)
    elif opc == 3:
        print("A média das idades dos torcedores é de:",somaIdade/torcedor)
        print("O nome do primeiro torcedor entrevistado é:",primeiroNome)
        print("O nome do último torcedor entrevistado é:",ultimoNome)
        print("A média dos pesos dos torcedores é de:",somaPeso/torcedor)
        print("A média da idade dos torcedores que assistem pela TV é de:",somaIdadeTv/tv)
        print("A média da idade dos torcedores que assistem no estádio é de:",somaIdadeEstadio/estadio)
        break
    else:
        print("Erro")
