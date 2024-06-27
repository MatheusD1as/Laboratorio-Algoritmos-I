def resposta():
    respostas = []
    for i in range(20):
        resp = input("Digite a sua resposta SIM | NÃO: ").upper()
        respostas.append(resp)
    return respostas
def somaRespostasSim(respostas):
    sim = 0
    for i in range(20):
        if respostas[i] == "SIM":
            sim += 1
    return sim
def somaRespostasNao(respostas):
    nao = 0
    for i in range(20):
        if respostas[i] == "NÃO":
            nao += 1
    return nao
def main():
    respostas = resposta()
    sim = somaRespostasSim(respostas)
    nao = somaRespostasNao(respostas)
    print("O número de pessoas que disse sim foi de:",sim," e o número de pessoas que disse não foi de:",nao)
main()