soma = 1

i = 1

while i <= 100:
    j = i
    fat_i = 1
    while j != 1:
        j -= 1
        fat_i += fat_i * j

    soma = soma + (1 / fat_i)
    i += 1

print(soma)