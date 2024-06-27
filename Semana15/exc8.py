def celsius_para_fahrenheit(celsius):
    fahrenheit = (((9/5)*celsius) + 32)
    return fahrenheit

def main():
    celsius = float(input("Digite a temperatura em graus celsius:"))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print("A temperatura de",celsius,"graus celsius, convertida para fahrenheit fica",fahrenheit,"graus")
main()