sph = 35
hrs = float(input("Digite o total de horas que você trabalha no mês:"))
slrM = 35 * hrs
if slrM < 1000:
    slrAumentado = slrM + 300
    print("Seu salário mensal é de:", slrAumentado)
else:
    print("Seu salário mensal é de:", slrM)
