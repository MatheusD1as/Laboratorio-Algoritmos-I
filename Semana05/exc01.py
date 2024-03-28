nome = input("Digite o nome do Funcionário:")
slrio = float(input("Digite o salário do funcionário:"))
tmpSvc = int(input("Digite o tempo de serviço do funcionário em anos:"))
if tmpSvc >= 5:
    if slrio <= 2000:
        slrio *= 1.1
        print("O funcionário",nome,"tem direito a aumento de 10'%' do salário ficando com um salário final de",slrio,)
    elif slrio > 2000:
        slrio *= 1.05
        print("O funcionário",nome,"tem direito a aumento de 5 '%' do salário ficando com um salário final de",slrio,)
else:
    print("O funcionário ainda não tem tempo suficiente de serviço para receber o aumento")
