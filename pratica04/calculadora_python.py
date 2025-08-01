# Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:



# A calculadora deve solicitar ao usuário que insira dois números e uma operação.

# As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

# O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

# Trate os seguintes erros:

# Entrada inválida (não numérica) para os números

# Divisão por zero

# Operação inválida

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def obter_operacao():
    while True:
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        if operacao in ['+', '-', '*', '/']:
            return operacao
        else:
            print("Operação inválida. Tente novamente.")

def calcular(n1, n2, operacao):
    try:
        if operacao == '+':
            return n1 + n2
        elif operacao == '-':
            return n1 - n2
        elif operacao == '*':
            return n1 * n2
        elif operacao == '/':
            if n2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            return n1 / n2
    except ZeroDivisionError as e:
        print(e)
        return None

# Loop principal
while True:
    numero1 = obter_numero("Digite o primeiro número: ")
    numero2 = obter_numero("Digite o segundo número: ")
    operacao = obter_operacao()

    resultado = calcular(numero1, numero2, operacao)

    if resultado is not None:
        print(f"Resultado: {numero1} {operacao} {numero2} = {resultado}")
        break  # encerra o loop após uma operação válida
    else:
        print("Vamos tentar novamente.\n")