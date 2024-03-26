
altura = float(input("Digite a altura:"))
sexo = input("Qual o sexo da pessoa - Masculino(M) ou Feminino:").upper()

if sexo == "F":
    pesoIdeal = (62.1 * altura) - 44.7
    print("Peso ideal para você mulher:", pesoIdeal)
else:
    pesoIdeal = (72.7 * altura) - 58
    print("Peso ideal para você homem:", pesoIdeal)
    
