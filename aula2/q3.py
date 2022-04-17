numero = int(input("Digite um número menor que 1000: "))
if numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    if centenas != 0:
        if centenas == 1:
            cent = "centena"
        else:
            cent = "centenas"

    if dezenas != 0:
        if dezenas == 1:
            dez = "dezena"
        else:
            dez = "dezenas"

    if unidades != 0:
        if unidades == 1:
            uni = "unidade"
        else:
            uni = "unidades"

    if centenas != 0 and dezenas != 0 and unidades != 0:
        print(f"{numero} = {centenas} {cent}, {dezenas} {dez} e {unidades} {uni}")
    elif centenas != 0 and dezenas != 0:
        print(f"{numero} = {centenas} {cent} e {dezenas} {dez}")
    elif centenas != 0 and unidades != 0:
        print(f"{numero} = {centenas} {cent} e {unidades} {uni}")
    elif dezenas != 0 and unidades != 0:
        print(f"{numero} = {dezenas} {dez} e {unidades} {uni}")
    elif centenas != 0:
        print(f"{numero} = {centenas} {cent}")
    elif dezenas != 0:
        print(f"{numero} = {dezenas} {dez}")
    elif unidades != 0:
        print(f"{numero} = {unidades} {uni}")
    else:
        print(f"{numero} = zero")
else:
    print("Número inválido")