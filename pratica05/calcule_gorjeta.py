# Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
# # Retorna: float: O valor da gorjeta calculada

def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta com base no total da conta e na porcentagem desejada.

    Parâmetros:
        valor_conta (float): O valor total da conta.
        porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%).

    Retorna:
        float: O valor da gorjeta calculada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


# Exemplo de uso
valor_total = float(input("Digite o valor total da conta: R$ "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))

valor_da_gorjeta = calcular_gorjeta(valor_total, porcentagem)
print(f"\nA gorjeta é: R$ {valor_da_gorjeta:.2f}")

