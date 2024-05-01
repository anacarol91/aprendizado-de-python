# Arrays , quando quiser criar uma lista muito grande
# tem que especificar o tipo de arrays. 'i' para integer 
# 'u' para string e 'f' para float.
# existem outras array em uma lista . jogando na internet.
# tomar cuidado para não colocar o tipo errado.

from array import array

letras=['a','b','c','d']
numero_i= [10,20,30,40]
numero_f= [1.2, 2.2, 3.2]

letras= array ('u',['a','b','c','d'])
numero_i= array('i',[10,20,30,40])
numero_f= array('f',[1.2, 2.2, 3.2])

print(letras)
print(numero_i)
print(numero_f)
