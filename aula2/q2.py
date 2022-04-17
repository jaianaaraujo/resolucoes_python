classificacao = 0

pergunta0 = input("Telefonou para a vítima?")
if pergunta0 == "sim":
    classificacao += 1
pergunta1 = input("Esteve no local do crime?")
if pergunta1 == "sim":
    classificacao += 1
pergunta2 = input("Mora perto da vítima?")
if pergunta2 == "sim":
    classificacao += 1
pergunta3 = input("Devia para a vítima?")
if pergunta3 == "sim":
    classificacao += 1
pergunta4 = input("Já trabalhou com a vítima?")
if pergunta4 == "sim":
    classificacao += 1

if classificacao <= 1:
    print('Inocente')
elif classificacao == 2:
    print('Suspeita')
elif classificacao <= 4:
    print('Cúmplice')
elif classificacao >= 5:
    print('Assasino')