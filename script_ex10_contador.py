
contador = 0
while True:
    numeros = input("Digite os números inteiros a serem lidos: ")
    if numeros == "":
        break
    try:
            contador += 1
    except ValueError:
            print("Entrada inválida")

print("Você digitou", contador, "números.")

 
