def lerCelsius():
    celsius = float(input("Digite a temperatura em graus celsius:"))
    return celsius
def Fconverter(celsius):
    fahrenheit = (((9/5)*celsius) + 32)
    return fahrenheit
def main():
    celsius = lerCelsius()
    fahrenheit = Fconverter(celsius)
    print("A temperatura de",celsius,"graus celsius, convertida para fahrenheit fica",fahrenheit,"graus")
main()