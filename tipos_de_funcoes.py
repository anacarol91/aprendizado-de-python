#tipos de funções
# realizam uma TAREFA ou
# RETRN calculam e retonam um valor ( ARMAZENA )
# a tarefa utiliza o print que só vai imprimir o resultado na tela 
# e não vai armazenar , jáo o retrn vai armazenar a inf e só aparece se 'chamar'

def cliente1(nome):
    print(f'ola {nome}')


def cliente2(nome):
    return f'olá {nome}'

# print(cliente2('hugo'))

x = cliente1('Ana')
y = cliente2('Hugo')
print(x)