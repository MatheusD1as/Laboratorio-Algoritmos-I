salario = float(input(""))
if salario <= 1903.98:
    print("Você está isento de imposto")
elif salario >= 1903.99 and salario <= 2826.65:
    imposto = salario * 0.075
    print("imposto =",imposto)
elif salario >=2826.66  and salario <= 3751.05:
    imposto = salario * 0.15
    print("imposto =",imposto)
else:
    imposto = salario * 0.225
    print("imposto =",imposto)
