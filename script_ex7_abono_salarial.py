""" O programa a seguir calcula o abono salarial que uma
empresa concederá aos seus funcionários com mais de um
ano de tempo de serviço. Os que têm menos de dez anos
ganharão abono de 10%. Os demais ganharão de 25%"""

salario = float(input(“Diga seu salário atual: ”))
tempo = int(input(“Diga quantos anos completos tem de serviço: ”))
if tempo<1:
print(“Seu salário se mantém o mesmo:”, salario)
else:
if tempo<10:
salario = salario * 1.10
else:
salario = salario * 1.25
print(“Seu novo salário, com abono:”, salario)
