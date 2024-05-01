# obj: criar um texto com variaveis 
# que o resultado seja : 
# A ana carolina tem 32 anos e mora no rio de janeiro
# o nome , a idade e o lugar seram variaveis 

nome = 'ana carolina'
idade = 32
idade = str(idade)
cidade = 'rio de janeiro'
# dentro do print não consegue ler 2 tipos de variaveis , tem que tranformar em iguais 
# pode usar print('A ' + nome + ' tem ' + str(idade) + ' anos e mora no ' + cidade + '.')
# ou transformar idade  = 32   idade = str(idade)

print('A ' + nome + ' tem ' + idade + ' anos e mora no ' + cidade + '.')

print('a ' + nome + ' está' + ' no ' + cidade)