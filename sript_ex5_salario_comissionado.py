nome = input('Digite seu nome: ')
salarioFixo = float(input('Digite seu salário fixo: '))
vendas = float(input('Digite suas vendas: '))
comissao = (vendas * 15)/100
salario_comissionado = salarioFixo + comissao
print('{}'.format(nome))
print('O valor a receber esse mês é de %.2f' %(salario_comissionado))
    
