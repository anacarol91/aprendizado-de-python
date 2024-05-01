# verificando itens em uma lista
cor_cliente= input('digite a cor desejada:')
cores=['amarelo','verde', 'vermelho', 'azul']
valores= [10,20,30,40]

duas_listas= zip(valores, cores)



if cor_cliente.lower() in cores: # .lower esta colocando em letra minuscula tudo que o cliente escrever
    print('temos essa cor')
    print(list(duas_listas))

else:
    print('infelismente não temos')     


