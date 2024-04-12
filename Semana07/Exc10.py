cont = 1
produto = 1
somaProduto = 0 
while produto != 0:
    produto = float(input(""))
    somaProduto += produto
    print("Produto",cont,": R$",produto) 
    cont += 1
dinheiro = float(input('Dinheiro que irá pagar'))
troco = dinheiro - somaProduto
print("Total:",somaProduto)
print("Dinheiro:",dinheiro)
print("Troco:",troco)
