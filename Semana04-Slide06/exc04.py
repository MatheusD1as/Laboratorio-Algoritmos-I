print("#### CALCULADORA ####")
n1 = float(input("Digite o primeiro valor:"))
n2 = float(input("Digite o segundo valor:"))
print("Escolha qual operação deseja fazer")
print("1 - Somar os dois valores")
print("2 - Subtrair os dois valores")
print("3 - Multiplicar os dois valores")
print("4 - Dividir os dois valores")
operador = float(input("Digite a sua opção:"))
if operador == 1:
    resultado = n1 + n2
    print("Resultado da soma:",resultado)
elif operador == 2:
    resultado = n1 - n2
    print("Resultado da subtração:",resultado)
elif operador == 3:
    resultado = n1 * n2
    print("Resultado da multiplicação:",resultado)
elif operador == 4:
    resultado = n1/n2
    print("O resultado da divisão:",resultado)
else:
    print("Opção inválida!")
