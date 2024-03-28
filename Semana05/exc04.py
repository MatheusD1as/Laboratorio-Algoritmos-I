nota1 = float(input("Digite a nota 1 do aluno:"))
nota2 = float(input("Digite a nota 2 do aluno:"))
media = (nota1 + nota2)/2
if media >= 9 and media <= 10:
    conceito = "A"
    print("A nota 1 aluno foi:",nota1,"A nota 2 do aluno foi:",nota2,"A media do aluno foi:",media,"O aluno teve conceito",conceito,"portanto foi APROVADO")  
elif media >= 7.5 and media < 9:
    conceito = "B"  
    print("A nota 1 aluno foi:",nota1,"A nota 2 do aluno foi:",nota2,"A media do aluno foi:",media,"O aluno teve conceito",conceito,"portanto foi APROVADO") 
elif media >= 6 and media < 7.5:
    conceito = "C"  
    print("A nota 1 aluno foi:",nota1,"A nota 2 do aluno foi:",nota2,"A media do aluno foi:",media,"O aluno teve conceito",conceito,"portanto foi APROVADO") 
elif media >= 4 and media < 6:
    conceito = "D"  
    print("A nota 1 aluno foi:",nota1,"A nota 2 do aluno foi:",nota2,"A media do aluno foi:",media,"O aluno teve conceito",conceito,"portanto foi REPROVADO") 
else:
    conceito = "E" 
    print("A nota 1 aluno foi:",nota1,"A nota 2 do aluno foi:",nota2,"A media do aluno foi:",media,"O aluno teve conceito",conceito,"portanto foi REPROVADO") 
