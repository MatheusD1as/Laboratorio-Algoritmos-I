vetor = []
opc = 0
while opc != 5:
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3- Listar itens")
    print("4 -  Retirar todos os itens")
    print("5 -  Sair")
    opc = int(input("Digite sua opção:"))
    if opc == 1:
        valor = float(input("Digite o valor que quer inseir:"))
        vetor.append(valor)
    elif opc == 2:
        vetor.remove(float(input("Digite o valor que quer deletar:")))
    elif opc == 3:
        print(vetor)
    elif opc == 4:
        vetor = []
    elif opc == 5:
        print("Obrigado por usar este programa")
    else:
        print("erro")

