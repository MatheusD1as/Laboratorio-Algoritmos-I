qtdMoradores = 0
elevadorA = 0
elevadorB = 0
elevadorC = 0
while qtdMoradores < 10:
    elevador = input("Qual elevador utiliza mais 'A' 'B' ou 'C':").upper()
    qtdMoradores += 1
    if elevador == "A":
        elevadorA += 1
    elif elevador == "B":
        elevadorB += 1
    elif elevador == "C":
        elevadorC += 1
print("Elevador A =",elevadorA,"Pessoas ; Elevador B =",elevadorB,";Elevador C =",elevadorC,"Pessoas")
print("Porcentagem que usa elevador A =",(elevadorA/10)*100)
print("Porcentagem que usa elevador B =",(elevadorB/10)*100)
print("Porcentagem que usa elevador C =",(elevadorC/10)*100)
