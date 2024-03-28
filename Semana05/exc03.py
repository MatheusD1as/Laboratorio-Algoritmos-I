nota1 = float(input("Nota 1 do aluno:"))
nota2 = float(input("Nota 2 do aluno:"))
freq = float(input("Digite a frequencia do aluno em '%':"))
media = (nota1 + nota2)/2
if freq >= 75:
    if media >= 7:
        print("Aluno aprovado")
    elif media >= 4 and media < 7:
        print("Aluno em exame")
    else:
        print("Aluno reprovado por nota")
else:
    print("Aluno reprovado por frequencia")
