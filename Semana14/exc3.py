def lerLaranjas(laranjas):
    laranjas = int(input("Digite quantas laranjas comprou:"))
    return laranjas
def laranjaPreco(laranjas):
    if laranjas <= 12:
        preco = 0.40 * laranjas
    elif laranjas >12:
         preco = 0.25 * laranjas
    return preco        
def main():
    laranjas= 0
    preco = 0
    laranjas = lerLaranjas(laranjas)
    preco = laranjaPreco(laranjas)
    print("O total da compra foi de:",preco)
main()

    