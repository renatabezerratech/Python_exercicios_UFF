def soma(* valores):
    s = 0
    for num in valores:
        s += num  # s = s + num
    print(f'Somando os valores {valores} temos {s}')  # f significa formatar


soma (4, 5)