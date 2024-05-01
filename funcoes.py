'''def boas_vindas():
    print('Ola Ana!')
    print('temos 5 noots em estoque.')



def somar_dois_numeros():
    numero1=10
    numero2=5
    resultado= numero1 + numero2
    print(resultado)


def somar_dois_numeros2():
    numero1=10
    numero2=8
    resultado= numero1 + numero2
    print(resultado)


somar_dois_numeros()
somar_dois_numeros2()
'''
def boas_vindas(nome, quantidade): #asrametro dentro do parenteses
    print(f'Ola {nome} !')
    print(f'temos {str(quantidade)} noots em estoque.')

boas_vindas('Ana', 6) # argumentos quando chama a função
boas_vindas('Hugo', 5)
boas_vindas('Pedro', 4)
