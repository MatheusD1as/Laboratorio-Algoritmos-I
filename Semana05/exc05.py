qtdSim = 0

resposta = input("Telefonou para vítima?(SIM OU NÃO):").upper()
if resposta == "SIM":
    qtdSim = qtdSim + 1


resposta = input("Esteve no local do crime? (SIM OU NÃO):").upper()
if resposta == "SIM":
    qtdSim = qtdSim + 1


resposta = input("Mora perto da vítima? (SIM OU NÃO):").upper()
if resposta == "SIM":
    qtdSim = qtdSim + 1

resposta = input("Devia para vítima? (SIM OU NÃO):").upper()
if resposta == "SIM":
    qtdSim = qtdSim + 1

resposta = input("Já trabalhou para vítima? (SIM OU NÃO):").upper()
if resposta == "SIM":
    qtdSim = qtdSim + 1
    
if qtdSim == 2:
    print("Suspeito do crime")
elif qtdSim == 3 or qtdSim == 4:
    print("Cúmplice do crime")
elif qtdSim == 5:
    print("Assasino")
else:
    print("Inocente")
