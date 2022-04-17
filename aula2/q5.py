r1 = float(input('Qual a primeira medida? '))
r2 = float(input('Qual a segunda medida? '))
r3 = float(input('Qual a terceira medida? '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('Podem formar triangulo')
    if r1 == r2 == r3:
        print(' EQUILÁTERO: todos os lados iguais')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO: todos os lados diferentes')
    else:
        print('ISÓSCELES: dois lados iguais, um diferente')
else:
    print('Não podem formar triangulo')
