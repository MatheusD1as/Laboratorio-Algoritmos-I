n = 0
somaIdade = 0
while n < 15:
    idade = int(input("Digite sua idade:"))
    somaIdade += idade
    n += 1
media = somaIdade/15
if media >= 0 and media <= 25:
    print("Turma jovem")
elif media >= 26 and media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
