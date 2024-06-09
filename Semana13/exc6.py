lista = []
resultado = []
constante = float(input("Digite o valor constante"))
for i in range(6):
    lista.append(float(input("Digite qual valor quer a atribuir a lista:")))
    resultado.append(constante*lista[i])
print(lista)
print(resultado)    