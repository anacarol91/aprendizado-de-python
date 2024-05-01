velocidade_carro = input ('qual a sua velocidade? ')
velocidade = int(velocidade_carro)

if velocidade > 110:
    print('acima da velocidade permitida')
elif velocidade <= 40:
    print('favor dirigir acima de 80 km/h')
else:
    print('velocidade ok.')
