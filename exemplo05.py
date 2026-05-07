print('====Cálculo de produtividade====')

try:

        total_produzido = float('valor total da venda: ')
        funcionarios = int(input('Total de funcionarios: '))
        mpfuncionario = total_produzido / funcionarios
        
    except Exception as e:
        print('Ops erro nos valores de entrada {e}')
    except KeyboardInterrupt:
        print('Funcionario não poder ser zero.')
    else:
        print(f'Média por funcionarios: {mpfuncionario:.2f}')
