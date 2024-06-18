def lerNotas():
    notas = []
    for i in range(5):
        nota = float(input(f"Digite a nota de número {i+1}:"))
        notas.append(nota)
    return notas
def mediaNotas(notas):
    soma = 0
    for i in range (5):
        soma += notas[i]
    media = soma/len(notas)
    return media

def situacao(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 4.0 and media < 7.0:
        return "Recuperação"
    else:
        return "Reprovado"
    
def main():
    notas = lerNotas()
    medianotas = mediaNotas(notas)
    resultado = situacao(medianotas)
    print("A média das notas é:", medianotas)
    print("A situação do aluno é:", resultado)
main()