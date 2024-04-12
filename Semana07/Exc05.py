idade = int(input("Digite sua idade:"))
salario = float(input("Digite seu salário:"))
sexo = input("Digite o seu sexo 'M' para masculino e 'F' para feminino:").upper()
EstadoCivil = input("Digite seu estado civil 'S' para Solteiro 'C' para casado 'V' para viúvo e 'D' para divorciado: ").upper()
while (idade < 0) or (idade > 150): 
    idade = int(input("Digite sua idade:"))
while (salario < 0):  
    salario = float(input("Digite seu salário:"))
while ((sexo != "M") and (sexo != "F")): 
    sexo = input("Digite o seu sexo 'M' para masculino e 'F' para feminino:").upper()
while((EstadoCivil != "S") and (EstadoCivil != "C") and (EstadoCivil != "V") and (EstadoCivil != "D")):  
    EstadoCivil = input("Digite seu estado civil 'S' para Solteiro 'C' para casado 'V' para viúvo e 'D' para divorciado: ").upper()
    
