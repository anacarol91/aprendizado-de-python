# diferenças entre  wheli loop; for loop; IF ELSE
# if/else; só roda uma vez a logica verdadiro/ falso
# for loop; gira a quantidade de vezes que por ordenado 
# wheli loop para a logica de acordo com a condicional colocada

valor = int(input('digite o valor do seu produto: '))

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor do seu produto será de R${valor}')
    break
    