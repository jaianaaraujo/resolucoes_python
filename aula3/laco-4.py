# a)

i = 0
somatorio = 0
while i != 1000:
    i += 1
    somatorio = somatorio + (1 / i)

print(somatorio)

# b)

n = int(input("Digite um número: "))
i = 0
somatorio = 0

while i <= n:
    somatorio = somatorio + (1 / (2 ** i))
    i += 1

print(somatorio)