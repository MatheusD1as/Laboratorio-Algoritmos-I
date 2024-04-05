saldoAtual = float(input("Digite o seu saldo atual:"))
opcao = 0
while opcao != 4:
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    if opcao == 1:
        saque = float(input("Digite o saque que irá fazer:"))
        saldoAtual -= saque
        print("Seu novo saldo é de:",saldoAtual)
    elif opcao == 2:
        deposito = float(input("Digite o valor do depósito:"))
        saldoAtual += deposito
        print("Seu novo saldo agora é:", saldoAtual)
    elif opcao == 3:
        print("Seu saldo é de", saldoAtual)
    elif opcao == 4:
        print("Até mais")
    else:
        print("Opção inválida Digite novamente")
    
