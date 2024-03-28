print("### FRUTEIRA DO MATHEUS ###")
print("Escolha qual tipo de fruta irá comprar")
print("Morango opção '1' ")
print("Maçã opção '2' ")
fruta = int(input("Digite qual sua opção:"))
kgs = float(input("Digite quantos quilogramas de fruta irá comprar:"))
if fruta == 1 and kgs <= 5:
    vlrcompra = kgs * 2.50
    print("O valor a pagar pelo morango será de",vlrcompra,"R$")
elif fruta == 1 and kgs > 5:
    vlrcompra = kgs * 2.20
    if vlrcompra > 25 or kgs > 8:
        vlrcompra *= 0.9
        print("O valor a pagar pelo morango será de",vlrcompra,"R$")
    else:
        print("O valor a pagar pelo morango será de",vlrcompra,"R$")
elif fruta == 2 and kgs <= 5:
     vlrcompra = kgs * 1.80
     print("O valor a pagar pela maçã será de",vlrcompra,"R$")
elif fruta == 2 and kgs > 5:
    vlrcompra = kgs * 1.50
    if vlrcompra > 25 or kgs > 8:
        vlrcompra *= 0.9
        print("O valor a pagar pela maçã será de",vlrcompra,"R$")
    else:
        print("O valor a pagar pela maçã será de",vlrcompra,"R$")
else:
    print("Você escolheu uma opção inválida")
