lcomprados = float(input('Quantos litros?'))
tipo = str(input("""
                 Qual tipo você quer?
                 [1] Gasolina
                 [2] Alcool
                 """))
vAlcool = 1.90
vGasolina = 2.50
print('=*' * 20)
if tipo == '2' and lcomprados <=20:
    desconto = vAlcool - 0.03 *lcomprados
    valorTotal = desconto * lcomprados
    print('Valor total: {:.2f}'.format(valorTotal))
elif tipo == '2' and lcomprados >= 20:
    desconto = vAlcool - 0.05 * lcomprados
    valorTotal = desconto * lcomprados
    print('Valor total: {:.2f}'.format(valorTotal))
elif tipo == '1' and lcomprados <= 20:
    desconto = vAlcool - 0.04 * lcomprados
    valorTotal = desconto * lcomprados
    print('Valor total: {:.2f}'.format(valorTotal))
elif tipo == '1' and lcomprados >= 20:
    desconto = vAlcool - 0.06 *lcomprados
    valorTotal = desconto * lcomprados
    print('Valor total: {:.2f}'.format(valorTotal))
