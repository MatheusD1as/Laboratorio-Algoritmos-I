n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))
if n1 > n2 and n1 > n3:
    print("maior =", n1)
elif n2 > n3 and n2 > n1:
    print("maior =", n2)
elif n3 > n1 and n3 > n2:
    print("maior =", n3)
else:
    print("Você digitou dois ou mais valores iguais")
