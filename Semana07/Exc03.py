n = int(input("Digite um número: "))
cont = 2
primoV = 0
while cont < int(n/2) +1:
    if n % cont == 0:
        primoV = 1
        break
    cont += 1
if primoV == 0:
    print("é primo")
else:
    print("Não É primo")
   
