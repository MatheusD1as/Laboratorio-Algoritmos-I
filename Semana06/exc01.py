qtdPessoas = 0
somaAltura = 0
somaIdade = 0
opcao = 0

while opcao != 3:
    print("1 - Cadastrar pessoa")
    print("2 - Media parcial da idade")
    print("3 - Sair")
    int(input("Digite a opção:"))
    if opcao == 1:
        idade = int(input("Digite a idade da pessoa:"))
        altura = float(input("Digite a altura da pessoa:"))
        somaAltura += altura
        somaIdade += idade
        qtdPessoas += 1
        print(somaIdade,somaAltura,qtdPessoas)
    elif opcao == 2:
        if qtdPessoas == 0:
            print("Nenhuma pessoa cadastrada!")
        else:
            mediaAlt = somaAltura / qtdPessoas
            mediaIdade = somaIdade / qtdPessoas
            print("Media parcial de alturas:", mediaAlt)
            print("Media parcial de idade:", mediaIdade)
    elif opcao == 3:
        if qtdPessoas == 0:
            print("Nenhuma pessoa cadastrada!")
        else:
            mediaAlt = somaAltura / qtdPessoas
            mediaIdade = somaIdade / qtdPessoas
            print("Media final de alturas:", mediaAlt)
            print("Media fianl de idade:", mediaIdade)
    else:
        print("Opção inválida digite novamente")
    
