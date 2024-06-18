def lerHora():
    hora = int(input("Digite o horário em horas:"))
    while hora < 0 or hora > 23:
        hora = int(input("Digite o horário em horas novamente ele deve estar entre 0 e 23:"))
    return hora
def lerMinutos():
    minuto = int(input("Digite o horário em minutos:"))
    while minuto < 0 or minuto > 59:
        minuto = int(input("Digite o horário em minutos novamente ele deve estar entre 0 e 59:"))
    return minuto
def conversao(hora):
    hora -= 12
    return hora
def main():
    hora = lerHora()
    minuto = lerMinutos()
    if hora > 12:
        hora = conversao(hora)
    print("Horário atualizado =",hora,":",minuto)
main()