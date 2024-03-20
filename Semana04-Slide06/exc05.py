print("### CARTEIRA DE CONDUÇÃO ###")
print("Escolha o tipo de categoria de carteira que irá tirar")
print("A - Motos e triciclos")
print("B - Carros de passeio")
print("C - Veículos de carga acima de 3,5 ton.")
print("D - Veículos com + de 8 passageiros")
print("E - Veículos com unidade acoplada acima de 6 ton.")
categoria = input("Digite sua escolha de categoria:").upper()
if categoria == "A":
    print("Você escolhe a categoria A - Motos e triciclos")
elif categoria == "B":
    print("Você escolhe a categoria B - Carros de passeio")
elif categoria == "C":
    print("Você escolhe a categoria C - Veículos de carga acima de 3,5 ton.")
elif categoria == "D":
    print("Você escolhe a categoria D - Veículos com + de 8 passageiros")
elif categoria == "E":
    print("Você escolhe a categoria E - Veículos com unidade acoplada acima de 6 ton.")
else:
    print("Você digitou uma categoria inválida")
    
