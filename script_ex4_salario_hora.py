func = int(input('Digite sua matrícula: '))
horas = int(input('Digite quantas horas foram trabalhadas: '))
valorhora = float(input('Digite o valor da hora de trabalho: '))
salario = horas * valorhora
print('Funcionário {}'.format (func))
print('Esse mês seu salário é de R$ %4.2f' %(salario))


