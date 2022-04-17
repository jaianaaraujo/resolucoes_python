quilosPeixe = float(input("Digite a quantidade de quilos de peixe: "))

if quilosPeixe > 50:
    quilosExcendentes = quilosPeixe - 50
else:
    quilosExcendentes = 0
    
multa = quilosExcendentes * 4

print("quilos", quilosPeixe)
print("quilos excessantes", quilosExcendentes)
print("multa", multa)