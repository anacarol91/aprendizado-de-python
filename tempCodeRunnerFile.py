# verificando itens em uma lista
cor_cliente= input('digite a cor desejada:')
cores=['amarelo','verde', 'vermelho', 'azul']
valores= [10,20,30,40]

duas_listas= zip(valores, cores)
print= list(duas_listas)


if cor_cliente.lower() in cores: # .lower esta colocando em letra minuscula tudo que o cliente escrever
    print('temos essa cor')

else:
    print('infelismente não temos')     


