#quando vc cria 2 loops, o de fora se chama Outer loop
# e o de dentro se chama inner loop

for numero1 in range(1,6):
    print('Produto ' + str (numero1))
    for numero2 in range(5):
        print(numero1 , numero2)

