ganho_hora = float(input("Digite o valor ganho por hora: "))

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = ganho_hora * horas_trabalhadas

print(f"Salário bruto: R$ {salario_bruto:.2f}")

imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
print(f"INSS: R$ {inss:.2f}")
print(f"Sindicato: R$ {sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")
