
valorDaPeca = float(input("Digite o valor da peça que irá comprar:"))

print("##### LOJA DE ROUPA ######")
print("Escolha a forma de pagamento")
print("1 - à vista")
print("2 - parcelado em 2x")
print("3 - parcelado em 3x")

opcao = int(input("Digite a opção:"))

if opcao == 1:
    print("Você efetuou a compra à vista e pagou",valorDaPeca,"R$")
elif opcao == 2:
    parcela = valorDaPeca / 2
    print("Você parcelou a sua compra em 2x de:", parcela,"R$,totalizando um valor de:", valorDaPeca,"R$")
elif opcao == 3:
    parcela = valorDaPeca / 3
    print("Você parcelou a sua compra em 3x de:", parcela,"R$, totalizando um valor de:", valorDaPeca,"R$")
else:
    print("Opção de inválida")
