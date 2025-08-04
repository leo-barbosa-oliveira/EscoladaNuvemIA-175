# Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
# Permitir que o usuário informe o preço do produto e o percentual de desconto.
# Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
# Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

def calcular_preco_com_desconto(preco: float, desconto_percentual: float) -> float:
    """
    Calcula o preço final de um produto após aplicar o desconto.

    Parâmetros:
        preco (float): Preço original do produto.
        desconto_percentual (float): Percentual de desconto (ex: 10 para 10%).

    Retorna:
        float: Preço final com desconto aplicado.
    """
    desconto = preco * (desconto_percentual / 100)
    preco_final = preco - desconto
    return preco_final


# Entrada do usuário
preco_original = float(input("Digite o preço do produto: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

# Cálculo
preco_com_desconto = calcular_preco_com_desconto(preco_original, percentual_desconto)

# Exibição do resultado com duas casas decimais
print(f"\nPreço final com desconto: R$ {preco_com_desconto:.2f}")
