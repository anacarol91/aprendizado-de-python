# Funções 
# - DRY - don't repeat yourself
# - Xargs - vários argumentos

# Criar uma função que soma vários números

def soma(*numeros):
    resultado= 0
    for num in numeros:
        resultado += num
    return resultado

x= soma(350,193,250,193)

print(x)



