qtdPessoas = 0
maior18 = 0
while qtdPessoas < 10:
   qtdPessoas += 1
   idade = int(input("idade:"))
   if idade >= 18:
      maior18 += 1
print("Quantidade de idades maiores ou iguais de 18 =",maior18)  
