salarioHora = float(input("Salario por hora: "))
horasTrabalhadas = float(input("Horas trabalhadas: "))

# alterar as númerações e atribuir em uma variável
totalSalarioBruto = salarioHora * horasTrabalhadas
valorInss = totalSalarioBruto * 0.11
valorImpostoRenda = totalSalarioBruto * 0.08
valorSindicato = totalSalarioBruto * 0.05
totalSalarioLiquido = totalSalarioBruto - valorInss - valorImpostoRenda - valorSindicato

print("Salario bruto: ", totalSalarioBruto)
print("Valor INSS: ", valorInss)
print("Valor Imposto de Renda: ", valorImpostoRenda)
print("Valor Sindicato: ", valorSindicato)
print("Salario liquido: ", totalSalarioLiquido)
