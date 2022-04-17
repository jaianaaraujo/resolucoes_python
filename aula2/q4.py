a = int(input("Digite o valor de A: "))

if a == 0:
    print("A equação não é de segundo grau")

else:
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))

    delta = (b**2 - 4*a*c)

    if delta < 0:
        print("A equação não possui raiz")
    elif delta == 0:
        raiz = (-b + (delta**0.5)) / (2*a)
        print(f"A equação possui apenas uma raiz real: {raiz}")
    else:
        raiz1 = (-b + (delta**0.5)) / (2*a)
        raiz2 = (-b - (delta**0.5)) / (2*a)
        print(f"A equação possui duas raiz reais: {raiz1} e {raiz2}")