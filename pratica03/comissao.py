# Calculadora de Comissão

# Entrada dos dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas no mês: "))

# Cálculo da comissão (15% sobre as vendas)
comissao = total_vendas * 0.15

# Cálculo do total a receber
total_receber = salario_fixo + comissao

# Saída formatada com duas casas decimais
print(f"TOTAL = R$ {total_receber:.2f}")