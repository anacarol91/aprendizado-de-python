#default= aquele qu evc define o valor no parametro
# non-default = aquele que vc ñ define o valor no parametro
#tem uma ordem para funcionar.. o default sempre tem que vir depois do non-default

def boas_vindas(nome, quantidade=6): # quantidade=6 é um default
    print(f'Ola {nome} !')
    print(f'temos {str(quantidade)} noots em estoque.')

