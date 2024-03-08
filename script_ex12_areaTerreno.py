print('-' * 30)
print('área do terreno')
print('-' * 30)


def terreno(base, altura):
    area = base * altura
    print(f'A área é {area}\n')


#Programa principal
b = float(input('Digite o comprimento do terreno: '))
a = float(input('Digite a largura do terreno: '))

terreno(b, a)


# OBS: nunca esqueça de tipar os inputs para evitar erro de compilação