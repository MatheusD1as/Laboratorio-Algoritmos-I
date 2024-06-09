valores = []
for i in range(5):
    valor = int(input("Digite um valor para o array:"))
    valores.append(valor)
teste = int(input("Digite um valor para verificar se ele está presente no array:"))
for i in range(5):
    if valores[i] == teste:
        print("Valor está presente no Array")
        break
else:
    print("Valor não está presente no array")
