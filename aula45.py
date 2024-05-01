# ** são vário parametros e váris argumentos


def agencia(**carro):
    return carro

c= agencia(Marca='fiat', modelo= 'Brava', cor="cinza", motor= 1.6)
print(c)
