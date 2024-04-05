saldoAtual = float(input(""))
opcao = int(input(""))
if opcao == 1:
    vlrSaque = float(input(""))
    if saldoAtual < vlrSaque:
        print("Saque inválido")
    else:
        saldoAtual -= vlrSaque
elif opcao == 2:
    deposito = float(input(""))
    saldoAtual += deposito
elif opcao == 3:
    print(saldoAtual)
else:
    print("opção inválida")
