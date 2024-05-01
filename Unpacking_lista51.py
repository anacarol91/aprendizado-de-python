# Armazenar mais de uma informação em variáveis
# Manter a sequencia dos dados em uma variável

produtos= ['arroz','feijão','laranja','banana', 1, 2, 3]
#index     0        1         2         3
'''item1= produtos[0]
item2= produtos[1]
item3= produtos[2]
item4= produtos[3]'''

item1, item2, item3, item4, *outros = produtos

print(item4, item1, item3)
print(outros)