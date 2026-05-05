print('====Cálculo de produtividade====')

try:

        total_produzido = float('valor total da venda: ')
        funcionarios = int(input('Total de funcionarios: '))
        mpfuncionario = total_produzido / funcionarios
        
    except (ValueError, TypeError):
        print('o valor precisa ser numerico.')
    except ZeroDivisionError:
        print('Funcionario não poder ser zero.')
    else:
        print(f'Média por funcionarios: {mpfuncionario:.2f}')
