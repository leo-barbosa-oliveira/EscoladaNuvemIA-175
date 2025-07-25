# 6- Calculadora de salário por horas trabalhadas

# Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.

# Entrada:

# O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:


# Número do funcionário (numero_funcionario).

# Quantidade de horas trabalhadas (horas_trabalhadas).

# Valor recebido por hora (valor_por_hora).

# Entrada dos dados
numero_funcionario = int(input("Digite o número do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora (R$): "))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibindo os resultados
print(f"NÚMERO DO FUNCIONÁRIO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")
