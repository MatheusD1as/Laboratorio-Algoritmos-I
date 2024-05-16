n1 = int(input("n1:"))
n2 = int(input("n2:"))
while n1 > n2:
    print("O primeiro número precisa ser menor")
    n1 = int(input("n1:"))
    n2 = int(input("n2:"))
if n1 % 2 == 0:
    for contador in range(n1+2,n2,2): ## +2 , pois o exercício pede os pares dentro do intervalo ou seja não leva em conta o valor inicia ou seja se o valor inicial for
                                      ## 2 e o final for 100 o primeiro numero par dentro desse intervalo será 4 pois não deve-se levar em conta o 2
        print(contador)
else:
    for contador in range(n1+1,n2,2):
        print(contador)
