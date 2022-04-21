numero = int(input("Digite um número"))
i = 2
while i <= numero:
    if i != numero:
        if numero % i == 0:
            print("não é primo")
            i = numero + 1
    i = i + 1

if i == numero + 1:
    print("é primo")