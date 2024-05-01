# while loops 
# while = enguanto ...
#excelente para loops dependentes de uma condição

# criar uma promoção que o preço vai decaido 

valor= 100
dia = 0

while valor > 20:
    dia += 1
    print(f' no dia {dia} o produto vai ser R${valor}')
    print(valor)    
    valor -= 5

    
