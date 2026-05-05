#calculo de produtividade


print('====Cálculo de produtividade====')

try:
    total_produzido = float('valor total da venda: ')
    funcionarios = int(input('Total de funcionarios: '))
    mpfuncionario = total_produzido / funcionarios
    print(f'Média por funcionarios: {mpfuncionario:.2f}')
except ValueError:
    print('Informe um Número.')
except ZeroDivisionError:
    print('Funcionario não poder ser zero.')
    

