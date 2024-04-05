age = int(input(""))
if age >= 0 and age<=11:
    print("Categoria = Criança")
elif age >= 12 and age<=17:
    print("Categoria = Adolescente")
elif age >= 18 and age<=64:
    print("Categotia = Adulto")
else:
    print("Categoria = Idoso")
