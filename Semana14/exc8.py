def prencher():
    num = [1,2,3,4,5,6,7,8,9,10]
    return num

def mostrar(num):
    numInverso = []
    for i in range(9, -1, -1):
        numInverso.append(num[i])
    print(numInverso)

def main():
    num = prencher()
    print(num)
    mostrar(num)

main()