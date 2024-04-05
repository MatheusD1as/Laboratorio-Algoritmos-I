numero = 1
contador10 = 0
while numero != 0:
    numero = float(input("Digite um numero:"))
    if numero == 10:
        contador10 += 1
    elif numero == 0:
        print("A quantidade de 10 escritos foi de:",contador10)

        
