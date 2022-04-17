""" Recebe um número float fracionado e retorna o inteiro maior mais proximo. 
    Exemplo: roundUp(3.1) -> 4
    
    float -> int
"""
def roundUp(n):
    if int(n) == n:
        return int(n)
    return int(n + 1)

area = float(input("Digite a quantidade de metros quadrados da àrea a ser pintada: "))

""" 1 litro de tinta pinta 6m². 
o Galão tem 18L e custa 80,00, a lata tem 3.6L e custa R$ 25,00. """

tintaUtilizada = area / 6
galoes = roundUp(tintaUtilizada / 18)
latas = roundUp(tintaUtilizada / 3.6)

galoesMistura = 0
latasMistura = 0
totalMistura = 0

for i in range(1, galoes + 1):
    if tintaUtilizada - totalMistura < 18:
        # Caso o restante de tinta não possa ser preenchida com um galão
        # o restante é completado com latas
        for j in range(1, latas + 1):
            if tintaUtilizada - totalMistura > 3.6:
                totalMistura += 3.6
                latasMistura += 1
            else:
                totalMistura += 3.6
                latasMistura += 1
                break
    else:
        totalMistura += 18
        galoesMistura += 1

valorMistura = (latasMistura * 25) + (galoesMistura * 80)

# Calcula se a decisão de completar com latas foi econômica
# ou não, caso não seja, retira latas e adiciona um galão
if valorMistura > galoes * 80:
    galoesMistura +=1 
    latasMistura = 0
    valorMistura = galoesMistura * 80

print("Somente Latas ou somente Galões:")
print("Comprando somente latas irá gastar", latas * 25)
print("Comprando somente galões irá gastar R$", galoes * 80)
print("")
print("Mistura:")
print("Comprando mistura irá gastar R$", valorMistura)