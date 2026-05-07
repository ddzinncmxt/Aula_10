print('====banco====')

try:
         
    
        saldo = 1000
        vlrdsaque = float(input('valor do saque: '))
        retirada = saldo - vlrdsaque
        
        
        if vlrdsaque > saldo:
            print('operação improvavel,reveja o valor.')
        else:
            print(f'valor a ser retirado: {vlrdsaque}')
            print(f'valor restante: {retirada}')
except ValueError:
    print('Informe um Número.')
except KeyboardInterrupt:
    print('operação cancelada')

    

    