# a) 
i = 0
while i != 4:
    i += 1
    print("*" * i)

# b)
print('-' * 21)
i = 1
j = 3
while i != 7:
    print("*" * i)
    i += 2
    if i == 7:
        while j != -1:
            print("*" *  j)
            j -= 2