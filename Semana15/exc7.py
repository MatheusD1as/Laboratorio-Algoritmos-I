def lerA(i, jornalA):
    jornalA.append(i)
    return jornalA

def lerB(i, jornalB):
    jornalB.append(i)
    return jornalB

def lerC(i, jornalC):
    jornalC.append(i)
    return jornalC
def crescente(porcA,porcB,porcC):
    if porcB >= porcA and porcA >= porcC:
        print(f'''Porcentagem do jornal B ={porcB}
Porcentagem jornal A ={porcA}
Porcentagem jornal C ={porcC}''')
    elif porcB >= porcC and porcC > porcA:
        print(f'''Porcentagem do jornal B ={porcB}
Porcentagem jornal C ={porcC}
Porcentagem jornal A ={porcA}''')        
    elif porcC >= porcA and porcA >= porcB:
        print(f'''Porcentagem do jornal C ={porcC}
Porcentagem jornal A ={porcA}
Porcentagem jornal B ={porcB}''')        
    elif porcC >= porcB and porcB >= porcA:
        print(f'''Porcentagem do jornal C ={porcC}
Porcentagem jornal B ={porcB}
Porcentagem jornal A ={porcA}''')  
    elif porcA >= porcC and porcC > porcB:
        print(f'''Porcentagem do jornal A ={porcA}
Porcentagem jornal C ={porcC}
Porcentagem jornal B ={porcB}''') 
    else:
                print(f'''Porcentagem do jornal A ={porcA}
Porcentagem jornal B ={porcB}
Porcentagem jornal C ={porcC}''') 

def main():
    jornalA = []
    jornalB = []
    jornalC = []

    for i in range(20):
        r = input("Digite o jornal que prefere ler (A, B, ou C): ").upper()
        
        if r == "A":
            jornalA = lerA(i, jornalA)
        elif r == "B":
            jornalB = lerB(i, jornalB)
        elif r == "C":
            jornalC = lerC(i, jornalC)
            print(jornalC)
        else:
            print("Opção inválida. Digite A, B ou C.")

    porcA = (len(jornalA) / 20) * 100
    porcB = (len(jornalB) / 20) * 100
    porcC = (len(jornalC) / 20) * 100
    
    crescente(porcA, porcB, porcC)
main()