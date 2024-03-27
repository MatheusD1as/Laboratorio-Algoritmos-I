idade = int(input("Digite a sua idade:"))

if idade >= 18 and idade < 70:
    print("Obrigado a votar")
elif idade >= 16 or idade > 70:
    print("Voto facultativo")
else:
    print("Não pode votar")
