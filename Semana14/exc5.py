def menu():
    print('''1 - Sacar dinheiro 
2 - Depositar dinheiro
3 - Mostrar saldo
4 - Sair''')
    opc = int(input("Digite sua opção:"))
    return opc
def saque(saldo):
    saq = float(input("Digite o saque que irá realizar:"))
    if saldo > saq:
        saldo -= saq   
    else:
        print("Seu saldo é menor que o valor que quer sacar")  
    return saldo 
def deposito():
    dep = float(input("Digite o valor que irá depositar:"))
    return dep
def mostraSaldo(saldo):
    print("Seu saldo é:",saldo,"R$")
def main():
    saldo = 0
    opc =0
    while opc != 4:
        opc = menu()
        if opc == 1:
            saldo = saque(saldo)
            mostraSaldo(saldo)
        elif opc == 2:
            saldo += deposito()
            mostraSaldo(saldo)
        elif opc == 3:
            mostraSaldo(saldo)

main()
