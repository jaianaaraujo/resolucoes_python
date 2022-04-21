numero = int(input("Digite um número"))
i = 2
while i <= numero:
    if i != numero:
        if numero % i == 0:
            print("não é primo")
            exit()
    i = i + 1
print("é primo")