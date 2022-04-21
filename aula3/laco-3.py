numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

i = 1
mdc = 0
# Calcula o MDC

while True:
    if numero1 % i == 0 and numero2 % i == 0:
        mdc = i
    i += 1
    if i > numero1 or i > numero2:
        break

print(mdc)