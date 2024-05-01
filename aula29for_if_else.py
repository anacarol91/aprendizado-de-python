# usar o For com o If e Else
#simular mensagem de envio de email no maximo 3x

compra_confirmada= True
dados_compra= 'compra confirmada de 15,00 e pronta para entrega'

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('detalhes por email')
        break
else:
    print('falha na compra')    