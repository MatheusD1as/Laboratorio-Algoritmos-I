print('''1 - Inserir item
2 - Listar itens
3 - Retirar item
4- Retirar todos os itens
5 - Contar quantos itens são maiores que um valor X (onde X é informado pelo usuário)
6 - Verificar se um determinado número (informado pelo usuário) está presente no array
7 - Encontrar o maior e o menor item do array
8 - Sair
''')
itens = []
opc = 0
maior = 0
menor = 0
maiorItem = 0
menorItem = 0
while opc != 8:
    opc = int(input("Digite sua opção:"))
    if opc == 1:
        item = int(input("Insira um número no array:"))
        while item % 2 == 1:
            item = int(input("O item só pode ser parar insira novamente:"))
        if item % 2 == 0:
            itens.append(item)
    elif opc == 2:
        print(itens)
    elif opc == 3:
        remove = int(input("Digite o item que quer remover:"))
        while remove not in itens:
            remove = int(input("Digite o item que quer remover que esteja na lista:"))
        if remove in itens:
            itens.remove(remove)
            print("Item removido")
    elif opc == 4:
        itens = []
    elif opc == 5:
        x = int(input("Digite o valor que quer comparar se é maior ou menor com os itens:"))
        for i in itens:
            if i > x:
                print(i,">",x)
                maior += 1
            elif i < x:
                print(i,"<",x)
                menor += 1
        print(maior,"item/itens é/são maior/maiores que",x,"e",menor,"itens/item são/é menor/menores que",x)
    elif opc == 6:
        num = int(input("Digite número para verificar se ele está dentro dos itens :"))
        if num in itens:
            print("Está na lista")
        else:
            print("Não está na lista")
    elif opc == 7:
            for i in range(0,len(itens)):
                if i == 0:
                    itens[i] = maiorItem
                    itens[i] = menorItem
                if maiorItem < itens[i]:
                    maiorItem = itens[i]
                if menorItem > itens[i]:
                    menorItem = itens[i]
            print("Menor item =",menorItem)
            print("Maior item =",maiorItem)
    elif opc == 8:
        print("Obrigado por usar o programa ;)")
    
                    
                   

    
        