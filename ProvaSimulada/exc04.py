n1 = float(input(""))
n2 = float(input(""))
n3 = float(input(""))

media = (n1 + n2 + n3)/3
if media > 9:
    print("Conceito A")
elif media >= 7 and media <=9:
    print("Conceito B")
elif media >= 5 and media <7:
    print("Conceito C")
elif media >= 3 and media <5:
    print("Conceito D")
else:
    print("Conceito E")
