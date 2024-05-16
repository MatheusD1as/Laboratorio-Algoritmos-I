par = 0
impar = 0
zero = 0
for contador in range (0,10):
    valor = int(input("Digite um número inteiro:"))
    if valor == 0:
        zero += 1
    elif valor % 2 == 0 :
        par += 1
    elif valor % 2 == 1: 
        impar += 1
   
print("Valores pares:",par)
print("Valores impares:",impar)
print("Valores = 0:",zero)
