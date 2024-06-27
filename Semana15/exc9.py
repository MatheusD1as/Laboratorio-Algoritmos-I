def array(tamanho):
    lista = []
    for i in range(tamanho):
        num = int(input("Digite o elemento que quer inserir"))
        lista.append(num)
    return lista 
def menor_item(lista):
    menor = lista[0]
    for num in lista:
        if num < menor:
            menor = num
    return menor

def maior_item(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num 
    return maior       

def main():
    tamanho = int(input("Digite o tamanho da lista que irá fazer: "))
    lista = array(tamanho)
    maior = maior_item(lista)
    menor = menor_item(lista)
    print("Maior =", maior)
    print("Menor =", menor)
main()